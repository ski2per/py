"""
LOAN进件的模块
Author: wei.zhang001
Date: 2020-04-21
"""


def loan_data(apply_fund_amount, proCityAreaDic):
    """
    返回loan的进件数据
    :return: 
    """
    return {
            # 交易信息
            "trade.isTrade": 0,
            "trade.houseTradeChannel": None,
            "trade.businessNo": None,
            "trade.search": None,
            "trade.tradeType": 0,
            "trade.tradeSignTime": "2020-04-01 00:00:00",
            "trade.tradeOrgan": None,
            "trade.agentName": None,
            "trade.agentId": None,
            "trade.agentDepartmentName": None,
            "trade.advisorName": None,
            "trade.advisorId": None,
            "trade.advisorDepartmentName": None,
            "trade.tradeContractNo": "100004658392",

            # 买房信息
            "buyers[].buyerName": "张坚强",
            "buyers[].buyerIdType": 0,
            "buyers[].buyerIdNo": "310115199008076338",
            "buyers[].buyerContact": "15719486308",
            "buyers[].buyerSex": 0,
            "buyers[].buyerCompanyLegal": None,
            "buyers[].buyerCompanyLegalType": None,
            "buyers[].buyerCompanyLegalNo": None,
            "buyers[].buyerCompanyLegalContact": "",
            "buyers[].buyerType": None,
            "buyers[].buyerMarriage": 1,
            "buyers[].buyerMateName": None,
            "buyers[].buyerMateContact": None,
            "buyers[].buyerInBj": None,
            "buyers[].buyerMateIdType": None,
            "buyers[].buyerMateIdNo": None,
            "buyers[].eachMate": None,
            

            # 买方代理人
            "buyerAgents[].agentName": "张五十",
            "buyerAgents[].idType": 0,
            "buyerAgents[].idNo": "310115199008076338",
            "buyerAgents[].agentContact": "15719486308",

            # 卖方信息
            "sellers[].sellerName": "霍迷",
            "sellers[].sellerIdType": "0",
            "sellers[].sellerIdNo": "511028199202280011",
            "sellers[].sellerContact": "15312340112",
            "sellers[].sellerSex": "0",
            "sellers[].postalAddress": "爽肤水",
            "sellers[].assetDivision": "",
            "sellers[].sellerCompanyLegal": None,
            "sellers[].sellerCompanyLegalType": None,
            "sellers[].sellerCompanyLegalNo": None,
            "sellers[].sellerCompanyLegalContact": None,
            "sellers[].divorceType": None,
            "sellers[].sellerMarriage": None,
            "sellers[].sellerMateName": None,
            "sellers[].sellerMateContact": None,
            "sellers[].sellerInBj": None,
            "sellers[].sellerMateIdType": None,
            "sellers[].sellerMateIdNo": None,
            "sellers[].eachMate": None,

            # 卖方代理人
            "sellerAgents[].agentName": "霍迷",
            "sellerAgents[].idType": "0",
            "sellerAgents[].idNo": "511028199202280011",
            "sellerAgents[].agentContact": "15312340112",

            # 房屋信息
            "houses[].buildingName": "林语城",
            "houses[].propertyAddress": "成都市区",
            "houses[].planOfUse": "0",
            "houses[].houseTitleDeedNo": "1234567890",
            "houses[].province": proCityAreaDic["provCode"],
            "houses[].city": proCityAreaDic["cityCode"],
            "houses[].district": proCityAreaDic["areaCode"],
            "houses[].buildArea": "100",
            "houses[].houseNature": "0",
            # 原借款人信息
            "houses[].houseOrgBorrowInfos[].personName": "",
            "houses[].houseShareInfos[].personName": "",
            "houses[].houseOrgBorrowInfos[].idType": "",
            "houses[].houseShareInfos[].idType": "",
            "houses[].houseShareInfos[].idNo": "",
            "houses[].houseOrgBorrowInfos[].idNo": "",
            # 是否抵贷不一
            "houses[].isPledgeLoan": "0",

            "houses[].certificateOfLand": "1",
            "houses[].houseShareInfos[].tel": "",
            "houses[].houseOrgBorrowInfos[].tel": "",
            "houses[].pledgeType": "0",
            "houses[].houseShareInfos[].propertyNo": "",
            "houses[].certificateNo": "0987654321",
            "houses[].pledgeTypeInfo": "0",
            "houses[].pledgeOrg": None,
            "houses[].pledgeAmount": None,
            "houses[].ownerName": "张仲临",
            "houses[].ownerIdType": "0",
            "houses[].ownerIdNo": "11010219960208151X",
            "houses[].ownerTel": "13261456346",
            "houses[].shareInfo": 0,
            "houses[].tradeHouse": 1,
            "houses[].lianjiaHouse": None,
            "houses[].housePropertyDate": "2019-02-16 14:52:12",
            "houses[].province": "210000",
            "houses[].orientation": "0,1",
            "houses[].buildYear": "2015",
            "houses[].nineGrid": "1",
            "houses[].evaluateAmount": "100000",
            "houses[].applyPledgeDate": "2019-02-16 14:52:12",
            "houses[].pledgeTypeOther": None,
            "houses[].propertyNo": "007",

            # 用资信息
            "capitalUse.applyFundAmount": apply_fund_amount,
            "capitalUse.applyFundUse": "test",
            "capitalUse.applyReceiptTime": "2019-02-16 14:52:12",
            "capitalUse.applyFundPracticalUse": "0",
            "capitalUse.applyFundRefundType": "1,2",
            "capitalUse.applyFundTerm": "90",
            "capitalUse.safePattern": "N",
            "capitalUse.redeemHouseType": "INSTRUCT",

            # 收款人账户信息
            "receiveAccount[].bankCardName": "张仲临",
            "receiveAccount[].bankCardNo": "4563510100892552062",
            "receiveAccount[].bankName": "中国银行",
            "receiveAccount[].bankBranchName": "草桥支行",
            "receiveAccount[].idType": "0",
            "receiveAccount[].idCardNo": "11010219960208151X",
            "receiveAccount[].tel": "13261456346",

            # 资金架构
            "loanCapital.productType": "0",
            "loanCapital.regulateType": "0",
            "loanCapital.regulateAmount": "100000",
            "loanCapital.loanBank": None,
            "loanCapital.loanBankBranch": None,
            "loanCapital.loanAmount": None,
            "loanCapital.downPaymentAmount": "300000",
            "loanCapital.bondAmount": "50000",
            "loanCapital.propertyDepositAmount": "500",
            "loanCapital.censusRegisterDepositAmount": "500",
            "loanCapital.netAmount": "1000000",
            "loanCapital.houseCapitalAmount": "351000",

            # 赎楼信息
            "redeemHouse.pledgeAgencyType": "0",
            "redeemHouse.pledgeRightType": "1",
            "redeemHouse.bankName": "建设银行",
            "redeemHouse.lender": "",
            "redeemHouse.branchName": "天府支行",
            "redeemHouse.mortgagor": "",
            "redeemHouse.accountManager": "王",
            "redeemHouse.loanHeader": "",
            "redeemHouse.accountManagerTel": "13900000000",
            "redeemHouse.loanHeaderTel": "13900000000",
            "redeemHouse.financialOrg": "",
            "redeemHouse.financialOrgBranch": "",
            "redeemHouse.propertyPledgeInfo": "0",
            "redeemHouse.isOrderRepayment": "0",
            "redeemHouse.orderRepaymentDate": None,
            "redeemHouse.houseProvince": proCityAreaDic["provCode"],
            "redeemHouse.houseCity": proCityAreaDic["cityCode"],
            "redeemHouse.houseDistrict": proCityAreaDic["areaCode"],
            "redeemHouse.debtsOrgProvince": proCityAreaDic["provCode"],
            "redeemHouse.debtsOrgCity": proCityAreaDic["cityCode"],
            "redeemHouse.debtsOrgArea": proCityAreaDic["areaCode"],

            # 借款人
            "borrowers[].name": "张仲临",
            "borrowers[].idType": 0,
            "borrowers[].idNo": "11010219960208151X",
            "borrowers[].contact": "13261456346",
            "borrowers[].sex": 1,
            "borrowers[].age": "30",
            "borrowers[].bornDate": "",
            "borrowers[].occupation": "",
            "borrowers[].workunit": "",
            "borrowers[].companyPosition": "贝壳金控",
            "borrowers[].postalAddress": "四川成都武侯大道",
            "borrowers[].unitAddress": "",
            "borrowers[].marriage": "1",
            "borrowers[].monthlyIncome": "",
            "borrowers[].mateName": "",
            "borrowers[].mateContact": "",
            "orrowers[].mateIdType": "",
            "borrowers[].mateIdNo": "",
            "borrowers[].mateUnitAddress": "",
            "borrowers[].mateMonthIncome": "",
            "borrowers[].eachMate": "",
            "borrowers[].ifAddCommonBorrower": "",
            "borrowers[].mateUnit": "",
            "borrowers[].inBj": "",
            "borrowers[].idCardDueDate": "2030-02-16 14:52:12",
            "borrowers[].nationality": "",
            "borrowers[].companyLegalType": None,
            "borrowers[].companyLegal": None,
            "borrowers[].companyLegalNo": None,
            "borrowers[].companyLegalContact": None,
            "borrowers[].borrowRelation": "",
            "borrowers[].companey": "",
            "borrowers[].mateIdType":"",
            "borrowers[].divorceType": "",
            "borrowers[].assetDivision": "",
            "borrowers[].commonBorrowers[].commonBorrowerName": "",
            "borrowers[].commonBorrowers[].commonBorrowerIdType": "",
            "borrowers[].commonBorrowers[].commonBorrowerIdNo": "",
            "borrowers[].commonBorrowers[].commonBorrowerContact": "",
            "borrowers[].commonBorrowers[].relationshipWithMortgagor": ""

    }


if __name__ == '__main__':
    print(loan_data().get("trade.isTrade1"))
    if "trade.isTrade" in loan_data():
        print(loan_data()["trade.isTrade"])
    else:
        print(123)