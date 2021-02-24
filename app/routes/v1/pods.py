import logging
import json
import datetime
import uuid

from flask import Blueprint, request, Response

from app.resources.pods import items

logger = logging.getLogger(__name__)
v1_pods = Blueprint("v1_pods", __name__)


@v1_pods.route("/api/v1/namespaces/<namespace>/pods", methods=["POST"])
def post_pods(namespace):
    new_ingress = json.loads(request.data)
    if namespace not in items:
        items[namespace] = []

    formated_new_ingress = {}

    if "metadata" in new_ingress:
        formated_new_ingress["metadata"] = new_ingress["metadata"]
        formated_new_ingress["metadata"][
            "selfLink"
        ] = f'/api/v1/namespaces/{namespace}/pods/{new_ingress["metadata"]["name"]}'
        formated_new_ingress["metadata"]["uid"] = str(uuid.uuid4())
        formated_new_ingress["metadata"]["resourceVersion"] = "103524551"
        formated_new_ingress["metadata"][
            "creationTimestamp"
        ] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if "spec" in new_ingress:
        formated_new_ingress["spec"] = new_ingress["spec"]

    formated_new_ingress["status"] = {
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

    # if "status" in new_ingress:
    #     formated_new_ingress["status"] = new_ingress["status"]

    items[namespace].append(new_ingress)
    return ""


@v1_pods.route("/api/v1/pods", methods=["GET"])
def get_all_namespaced_pods():
    ret_items = []
    for namespace in items:
        ret_items += items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "PodList",
                "apiVersion": "v1",
                "metadata": {
                    "selfLink": "/api/v1/namespaces/production/pods",
                    "resourceVersion": "103529284",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@v1_pods.route("/api/v1/namespaces/<namespace>/pods", methods=["GET"])
def get_pods(namespace):

    ret_items = []

    if namespace in items:
        ret_items = items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "PodList",
                "apiVersion": "v1",
                "metadata": {
                    "selfLink": "/api/v1/namespaces/production/pods",
                    "resourceVersion": "103529284",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@v1_pods.route("/api/v1/namespaces/<namespace>/pods/<pod_name>", methods=["DELETE"])
def delete_pods(namespace, pod_name):

    found = False

    if namespace in items:
        for item in items[namespace]:
            if item["metadata"]["name"] == pod_name:
                found = True
                items[namespace].remove(item)
                break

    if found:
        ret = {
            "kind": "Status",
            "apiVersion": "v1",
            "metadata": {},
            "status": "Success",
            "details": {
                "name": pod_name,
                "kind": "pods",
                "uid": item["metadata"]["uid"],
            },
        }
    else:
        ret = {
            "kind": "Status",
            "apiVersion": "v1",
            "metadata": {},
            "status": "Failure",
            "message": f'pods "{pod_name}" not found',
            "reason": "NotFound",
            "details": {"name": pod_name, "kind": "pods"},
            "code": 404,
        }

    return Response(response=json.dumps(ret), status=200, mimetype="application/json")
