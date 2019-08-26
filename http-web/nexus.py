import re
import time
import requests

nexus_username = 'admin'
nexus_password = 'zdsys8301'
nexus_base_url = 'http://172.16.101.214:8081'


def get_resources(url):

    response = requests.get(url, auth=(nexus_username, nexus_password))
    if not response.status_code == 200:
        print("Error getting {}".format(url))
        return {}
    else:
        return response.json()


def list_repos():
    repo_url = '{}/service/rest/v1/repositories'.format(nexus_base_url)
    return get_resources(repo_url)


def list_components(repo_name, filter_regexp=r""):
    # Use 'filter_regexp' to filter component by name
    all_components = []
    components_url = '{}/service/rest/v1/components?repository={}'.format(nexus_base_url, repo_name)
    tmp = get_resources(components_url)
    all_components += tmp['items']

    while tmp['continuationToken']:
        new_url = '{}&continuationToken={}'.format(components_url, tmp['continuationToken'])
        tmp = get_resources(new_url)
        all_components += tmp['items']

    if filter_regexp:

        filtered_components = list(filter(lambda x: re.match(filter_regexp, x['name']), all_components))
        return filtered_components

    else:
        return all_components


def delete_component(component_id):
    component_delete_url = '{}/service/rest/v1/components/{}'.format(nexus_base_url, component_id)
    response = requests.delete(component_delete_url, auth=(nexus_username, nexus_password))
    if response.status_code == 204:
        print('Delete component({}) successfully'.format(component_id))
    else:
        print('Delete component({}) unsuccessfully'.format(component_id))


if __name__ == '__main__':
    components = list_components('zdsys', filter_regexp=r'.+\-building')
    for component in components:
        print(component['id'])
        delete_component(component['id'])
        time.sleep(2)


