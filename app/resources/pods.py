import datetime
import uuid

items = {}


def create_item(namespace, item):
    global items

    if namespace not in items:
        items[namespace] = []

    formated_item = {}

    if "metadata" in item:
        formated_item["metadata"] = item["metadata"]
        formated_item["metadata"][
            "selfLink"
        ] = f'/api/v1/namespaces/{namespace}/pods/{item["metadata"]["name"]}'
        formated_item["metadata"]["uid"] = str(uuid.uuid4())
        formated_item["metadata"]["resourceVersion"] = "103524551"
        formated_item["metadata"][
            "creationTimestamp"
        ] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if "spec" in item:
        formated_item["spec"] = item["spec"]

    formated_item["status"] = {
        "phase": "Running",
        "conditions": [
            {
                "type": "Initialized",
                "status": "True",
                "lastProbeTime": None,
                "lastTransitionTime": "2021-02-06T01:47:52Z",
            },
            {
                "type": "Ready",
                "status": "True",
                "lastProbeTime": None,
                "lastTransitionTime": "2021-02-08T14:45:05Z",
            },
            {
                "type": "ContainersReady",
                "status": "True",
                "lastProbeTime": None,
                "lastTransitionTime": "2021-02-08T14:45:05Z",
            },
            {
                "type": "PodScheduled",
                "status": "True",
                "lastProbeTime": None,
                "lastTransitionTime": "2021-02-06T01:47:51Z",
            },
        ],
        "hostIP": "10.20.4.91",
        "podIP": "10.20.4.154",
        "startTime": "2021-02-06T01:47:52Z",
        "containerStatuses": [
            {
                "name": "app",
                "state": {"running": {"startedAt": "2021-02-08T14:44:39Z"}},
                "lastState": {
                    "terminated": {
                        "exitCode": 137,
                        "reason": "Error",
                        "startedAt": "2021-02-06T22:26:28Z",
                        "finishedAt": "2021-02-08T14:44:37Z",
                        "containerID": "docker://1a2c158e0182bc4f9db9f75b61c680c8dee38cbf62d09c054a95cf314d004f20",
                    }
                },
                "ready": True,
                "restartCount": 2,
                "image": "plataformproductionacr.azurecr.io/app:7513",
                "imageID": "docker-pullable://plataformproductionacr.azurecr.io/app@sha256:c86f51fdc36e49378c762e965d8d3412f36657a89c71f1984ec34ccc53cf0ae2",
                "containerID": "docker://fef3c93c47cf1d1c086f6350352dd915e9c083536f278b776da6efb11d518d32",
            }
        ],
        "qosClass": "Burstable",
    }

    items[namespace].append(formated_item)
