import time
import docker
import requests
import json
import pprint


FLANNEL_NETWORK = 'wtf'
SWARM_NETWORK = ''
CONTAINER_FILTER = ''
CONSUL_API = 'http://172.16.101.216:8500/v1'
CONSUL_REGISTER_API = '/agent/service/register'
CONSUL_DEREGISTER_API = '/agent/service/deregister/'

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def register(service):
    resp = requests.put('{}{}'.format(CONSUL_API, CONSUL_REGISTER_API), data=json.dumps(service))
    if resp.status_code == 200:
        print("Service {} registration succeed".format(service['Name']))
    else:
        print("service {} registration failed".format(service['Name']))
        print(resp.text)
        print(service)

def deregister(service_id):
    resp = requests.put('{}{}{}'.format(CONSUL_API, CONSUL_DEREGISTER_API, service_id))
    if resp.status_code == 200:
        print("service deregistration succeed")
    else:
        print("service deregistration failed")
        print(resp.text)

# Unregister exited containers which joined FLANNEL_NETWORK from Consul
def deregister_container():
    for container in client.containers.list(filters={'status': 'exited'}):
        joined_networks = container.attrs['NetworkSettings']['Networks']
        if FLANNEL_NETWORK not in joined_networks.keys():
            continue
        service_id = container.id
        deregister(service_id)


def register_container():
    for container in client.containers.list():
        joined_networks = container.attrs['NetworkSettings']['Networks']
        if FLANNEL_NETWORK not in joined_networks.keys():
            continue

        service = {
            'ID': container.id,
            'Address': joined_networks[FLANNEL_NETWORK]['IPAddress']
        }

        try:
            container_name = container.labels['com.docker.compose.service']
        except KeyError:
            # When container was run by 'docker run' command
            container_name = container.name

        service['Name'] = container_name
        register(service)

if __name__ == '__main__':
    while True:
        deregister_container()
        register_container()
        time.sleep(2)
    # deregister_container()
# for network in client.networks.list():
#     print(network)
