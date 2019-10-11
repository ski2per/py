import re
import json
import time
import shutil
import requests


class Nexus:
    def __init__(self):
        self.username = 'admin'
        self.password = 'zdsys8301'
        self.base_url = 'http://172.16.101.214:8081'

    def _fetch_url(self, url):
        response = requests.get(url, auth=(self.username, self.password))
        if not response.status_code == 200:
            print("Error getting {}".format(url))
            return {}
        else:
            return response.json()

    def list_repos(self):
        repo_url = '{}/service/rest/v1/repositories'.format(self.base_url)
        return self._fetch_url(repo_url)

    def list_components(self, repo_name, filter_regexp=r""):
        # Use 'filter_regexp' to filter component by name
        all_components = []
        components_url = '{}/service/rest/v1/components?repository={}'.format(self.base_url, repo_name)
        tmp = self._fetch_url(components_url)
        if tmp:
            all_components += tmp['items']
        else:
            return []

        while tmp['continuationToken']:
            new_url = '{}&continuationToken={}'.format(components_url, tmp['continuationToken'])
            tmp = self._fetch_url(new_url)
            all_components += tmp['items']

        if filter_regexp:

            filtered_components = list(filter(lambda x: re.match(filter_regexp, x['name']), all_components))
            return filtered_components

        else:
            return all_components

    def delete_component(self, component_id):
        component_url = '{}/service/rest/v1/components/{}'.format(self.base_url, component_id)
        response = requests.delete(component_url, auth=(self.username, self.password))
        if response.status_code == 204:
            print('Delete component({}) successfully'.format(component_id))
        else:
            print('Delete component({}) unsuccessfully'.format(component_id))

    def list_component(self, component_id):
        component_url = '{}/service/rest/v1/components/{}'.format(self.base_url, component_id)
        return self._fetch_url(component_url)

    def upload_component(self, repo_name, data: dict):
        components_url = '{}/service/rest/v1/components?repository={}'.format(self.base_url, repo_name)

        pass


if __name__ == '__main__':
    nexus = Nexus()
    # components = nexus.list_components('zdsys', filter_regexp=r'.+\-building')
    # for component in components:
    #    print(component['id'])
    #    delete_component(component['id'])
    #    time.sleep(2)

    cid = 'bWF2ZW4taG9zdGVkOjM2ZTNkZWM4ZGU1MjhjOWIzMGVmMTUzMWUzY2I1MDVk'
    # cid = 'bWF2ZW4taG9zdGVkOjE4ZGRlY2NkZmI0OTFlY2I2NDMxMmU3MDkxM2Y3ZDE1'

    # components = nexus.list_components('maven-hosted')
    # for comp in components:
    #     print(comp)

    foo = nexus.list_component(cid)
    print(foo)
    url = 'http://172.16.101.214:8081/repository/maven-hosted/com/wish30/1.6/wish30-1.6.jar'
    local_filename = url.split('/')[-1]
    file = open('wish30-1.6.jar', 'rb')
    form_data = {
        'maven2.groupID': foo['group'],
        'maven2.artifactId': foo['name'],
        'maven2.version': foo['version'],
        'maven2.generate-pom': 'false',
        'maven2.asset1': file,
        'maven2.asset1.extension': 'jar'
    }

    print(form_data)
    headers = {
        'Content-type': 'multipart/form-data, boundary=xxxxxxxxxxxxxxxxxoooooooooooo',
    }
    # r = requests.post('http://nexus.ted.mighty/service/rest/v1/components?repository=m2-hosted', verify=False,
    #                   auth=('user', 'user'), data=form_data)
    r = requests.post('http://nexus.ted.mighty/service/rest/v1/components?repository=m2-hosted',
                      auth=('user', 'user'), data=form_data)
    print(r.status_code)

    #with requests.get(url, stream=True) as r:
    #    with open(local_filename, 'wb') as f:
    #        shutil.copyfileobj(r.raw, f)

