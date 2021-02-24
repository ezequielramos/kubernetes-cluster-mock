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
        formated_item["metadata"]["namespace"] = namespace
        formated_item["metadata"][
            "selfLink"
        ] = f'/apis/extensions/v1beta1/namespaces/{namespace}/deployments/{item["metadata"]["name"]}'
        formated_item["metadata"]["uid"] = str(uuid.uuid4())
        formated_item["metadata"]["resourceVersion"] = "105981762"
        formated_item["metadata"][
            "creationTimestamp"
        ] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if "spec" in item:
        formated_item["spec"] = item["spec"]

    formated_item["status"] = {
        "observedGeneration": 4,
        "replicas": 1,
        "updatedReplicas": 1,
        "readyReplicas": 1,
        "availableReplicas": 1,
        "conditions": [
            {
                "type": "Available",
                "status": "True",
                "lastUpdateTime": "2021-02-16T08:46:20Z",
                "lastTransitionTime": "2021-02-16T08:46:20Z",
                "reason": "MinimumReplicasAvailable",
                "message": "Deployment has minimum availability.",
            }
        ],
    }

    items[namespace].append(formated_item)
