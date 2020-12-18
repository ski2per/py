from kubernetes import client, config, watch
config.load_kube_config()


v1_api = client.CoreV1Api()
networking_api = client.NetworkingV1beta1Api()

watcher = watch.Watch()

for event in watcher.stream(networking_api.list_ingress_for_all_namespaces):
    event_type = event["type"].lower()
    event_obj_spec = event["object"].spec

    if event_type in ["added", "deleted"]:
        for rule in event_obj_spec.rules:
            if rule.host.endswith("cetcxl.local"):
                print(event_type, rule.host)
