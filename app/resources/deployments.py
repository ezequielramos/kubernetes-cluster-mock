import datetime
import uuid
from typing import Tuple
import copy

from app.resources.pods import create_item as create_pod
from app.resources.pods import delete_item_through_parent

deployments = {}


def create_item(namespace, item):
    global deployments

    if namespace not in deployments:
        deployments[namespace] = []

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

    deployments[namespace].append(formated_item)

    pod = copy.deepcopy(item["spec"]["template"])
    pod["metadata"]["name"] = (
        item["metadata"]["name"] + "-" + str(uuid.uuid4()).split("-")[0]
    )

    create_pod(namespace, pod, formated_item["metadata"]["selfLink"])


def delete_item(namespace: str, name: str) -> Tuple[bool, dict]:
    global deployments

    if namespace in deployments:
        for item in deployments[namespace]:
            import json

            if item["metadata"]["name"] == name:
                delete_item_through_parent(namespace, item["metadata"]["selfLink"])
                deployments[namespace].remove(item)
                return True, item

    return False, None
