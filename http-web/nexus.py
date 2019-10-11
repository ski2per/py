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

    # To be optimized
    def transfer_maven_componemt(self):
        source = 'maven-hosted'
        components = self.list_components(source, r'rate')
        cid = 'bWF2ZW4taG9zdGVkOjM2ZTNkZWM4ZGU1MjhjOWIyZmFiNTdlNDAyM2Y3YmI5'
        component = self.list_component(cid)
        components = [component]
        for comp in components:
            source_url = comp['assets'][0]['downloadUrl']
            with requests.get(source_url, stream=True) as r:
                with open('tmp.jar', 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            with open('tmp.jar', 'rb') as jar:
                form_data = {
                    'maven2.groupId': (None, comp['group']),
                    'maven2.artifactId': (None, comp['name']),
                    'maven2.version': (None, comp['version']),
                    'maven2.generate-pom': (None, 'false'),
                    'maven2.asset1': jar,
                    'maven2.asset1.extension': (None, 'jar')
                }
                r = requests.post('https://nexus.ted.mighty/service/rest/v1/components?repository=m2-hosted', verify=False,
                                  auth=('user', 'user'), files=form_data)
                print(r.status_code)


if __name__ == '__main__':
    nexus = Nexus()
    # components = nexus.list_components('zdsys', filter_regexp=r'.+\-building')
    # for component in components:
    #    print(component['id'])
    #    delete_component(component['id'])
    #    time.sleep(2)

    nexus.transfer_maven_componemt()




    # foo = nexus.list_component(cid)
    # print(foo)
    # url = 'http://172.16.101.214:8081/repository/maven-hosted/com/wish30/1.6/wish30-1.6.jar'
    # local_filename = url.split('/')[-1]
    #
    #

