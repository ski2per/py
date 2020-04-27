"""
LOAN进件的模块
Author: wei.zhang001
Date: 2020-04-06
"""
import random
from base.requestlib import RequestApi
from base.ssoLogin import Login
import json
from business.createLoan.data.loan_data import loan_data
from business.createLoan.action.productRequest import Product
from business.mysql.housingloan_sql import HousingLoanSQL
from base import com
from business.createLoan.action.cmsRequest import Cms


class LoanRun(object):
    """
    进件模块
    """
    def __init__(self, cookie, loan_no, city_code, product_code=None):
        cf = com.get_config()
        self.host = cf.get("HTTP_CMS", "host")
        self.cookie = cookie
        self.loan_no = loan_no
        self.city_code = city_code
        # 小7造单没有金融单产品，通过数据库查询得到产品code
        if product_code:
            self.product_code = product_code
        else:
            self.product_code = HousingLoanSQL().get_product_by_loan(self.loan_no)
        self.loan_data = loan_data(self.get_apply_fund_amount(), self.proCityArea(self.city_code))

    def submit_loan_data(self):
        """
        得到所有列表
        :param loan_no:
        :return:
        """
        url = "https://alpha.test.bkjk-inc.com/api/crm/api/1.0/loan/{}/template".format(self.loan_no)
        result = RequestApi().get(url=url, cookies=self.cookie)
        for process_node in result["processNodes"][0]["templateNodes"]:
            if process_node["processNodeName"] == "上传备件":
                # 如果是上传备件就略过
                pass
            else:
                self.get_loan_modules(process_node=process_node["processCode"], node_node=process_node["nodeId"],
                                      process_relation_id=process_node["id"])
                break

    def get_loan_modules(self, process_node, node_node, process_relation_id):
        """
        得到所有的具体数据
        :param process_node:
        :param node_node:
        :param process_relation_id:
        :return:
        """
        url = "https://heimdall.test.bkjk.com/financebill/loanModules"
        data = {"processRelationId": process_relation_id, "lft": False}
        result = RequestApi().post(url=url, json=data, cookies=self.cookie)
        for module in result["data"]:
            # 得到这个模板所需要填写的内容
            module_data = self._get_module_value(module, process_relation_id, process_node, node_node)
        self.submit_loan_modules(data=module_data)

    def _get_module_value(self, module, process_relation_id, process_node, node_node):
        """
        返回对应的数据值
        :return:
        """
        new_data = {}
        # 老数据
        old_info = self.get_node_info(process_relation_id=process_relation_id)
        print("以前的数据", json.dumps(old_info))
        for config in module["configs"]:
            # 判断是否必填的值
            if "rules" in config:
                value_path = config["valuePath"]
                # 得到需要填写的key
                # 有些路径没有.
                if len(value_path.split(".")) == 2:
                    # 得到的key
                    module_key = value_path.split(".")[1]
                    module_path = value_path.split(".")[0]
                    print("要填写的key ", value_path)
                    if module_path.endswith("[]"):
                            new_data[module_path[0:-2]].append({module_key: self.loan_data.get(value_path)})
                    else:
                            new_data.update({module_key: self.loan_data.get(value_path)})
                            new_data[module_path] = {module_key: self.loan_data.get(value_path)}
        print("填充的数据", new_data)
        print("test")
        # print("填写后的数据", json.dumps(old_info))
        # old_info["processCode"] = process_node
        # old_info["nodeCode"] = node_node
        # old_info["processRelationId"] = process_relation_id
        # old_info["isCommit"] = True

        return old_info

    def get_node_info(self, process_relation_id):
        """
        得到模块的老数据
        :param key:
        :param id:
        :return:
        """
        url = "https://alpha.test.bkjk-inc.com/api/crm/api/1.0/loan/{}/{}".format(self.loan_no, process_relation_id)
        old_info = RequestApi().get(url=url, cookies=self.cookie)
        return old_info

    def submit_loan_modules(self, data):
        """
        提交数据
        :return:
        """
        url = "https://alpha.test.bkjk-inc.com/api/crm/api/1.0/loan-modules"
        print("提交的进件数据 = ", json.dumps(data))
        result = RequestApi().post(url=url, json=data, cookies=self.cookie)
        print("提交的数据结果为 = ", json.dumps(result))

    def get_apply_fund_amount(self):
        """
        得到进件的金额
        :return:
        """
        apply_fund_amount, _ = Product().get_borrowing_amount(self.product_code)
        return apply_fund_amount

    def proCityArea(self, cityCode):
        """
        通过城市code去查询省code及区cod
        :param cityCode:
        :return:
        """
        proCityAreaDic = {}
        response = Cms().getPorByCityCode(cityCode)
        proCityAreaDic["provCode"] = response["code"]
        proCityAreaDic["provName"] = response["name"]

        response = Cms().getAreaByCityCode(cityCode)
        length = len(response)
        proCityAreaDic["areaCode"] = response[random.randint(0,length-1)]["code"]
        proCityAreaDic["areaName"] = response[random.randint(0, length - 1)]["name"]

        proCityAreaDic["cityCode"] = cityCode
        proCityAreaDic["cityName"] = self.get_city_name(cityCode)
        return proCityAreaDic

    def get_city_name(self, city_code):
        """
        得到城市的名字
        """
        url = "https://heimdall.test.bkjk.com/api/1.0/datasource/CITIES"
        data = {"cityCode": city_code}
        result = RequestApi().post(url=url, json=data, cookies=self.cookie)
        return result["data"][0]["value"]


if __name__ == '__main__':
    user_id = "shibo.wen"
    loan_no = "JR010158796724605963"
    city_code = "110000"
    from base.ssoLogin import Login
    cookie = Login(user_id).login()
    ss = LoanRun(cookie=cookie, loan_no=loan_no, city_code=city_code)
    ss.submit_loan_data()
    # ss.get_id_info(key='buyers[]', process_relation_id=12801)
