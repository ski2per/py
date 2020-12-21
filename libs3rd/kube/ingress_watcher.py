from kubernetes import client, config, watch
config.load_kube_config()

bind9_file_map = {
    "cetcxl.local": "db.cetcxl.local",
    "dev.cetcxl.local": "db.dev.cetcxl.local",
    "devops.cetcxl.local": "db.devops.cetcxl.local",
}

def extract_host_domain(text: str) -> tuple:
    return tuple(text.split(".", 1))


v1_api = client.CoreV1Api()
networking_api = client.NetworkingV1beta1Api()

watcher = watch.Watch()

for event in watcher.stream(networking_api.list_ingress_for_all_namespaces):
    event_type = event["type"].lower()
    event_obj_spec = event["object"].spec

    if event_type in ["added", "deleted"]:
        for rule in event_obj_spec.rules:
            if rule.host.endswith("cetcxl.local"):
                host, domain = extract_host_domain(rule.host)
                print(event_type, host,  bind9_file_map[domain])
