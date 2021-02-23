import logging
import json
import datetime
import uuid

from flask import Blueprint, request, Response

from app.resources.deployments import items

logger = logging.getLogger(__name__)
extensions_v1beta1_deployments = Blueprint("extensions_v1beta1_deployments", __name__)


@extensions_v1beta1_deployments.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/deployments", methods=["POST"]
)
def post_deploy(namespace):
    new_ingress = json.loads(request.data)
    if namespace not in items:
        items[namespace] = []

    formated_new_ingress = {}

    if "metadata" in new_ingress:
        formated_new_ingress["metadata"] = new_ingress["metadata"]
        formated_new_ingress["metadata"][
            "selfLink"
        ] = f'/apis/extensions/v1beta1/namespaces/{namespace}/deployments/{new_ingress["metadata"]["name"]}'
        formated_new_ingress["metadata"]["uid"] = str(uuid.uuid4())
        formated_new_ingress["metadata"]["resourceVersion"] = "105981762"
        formated_new_ingress["metadata"][
            "creationTimestamp"
        ] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if "spec" in new_ingress:
        formated_new_ingress["spec"] = new_ingress["spec"]

    formated_new_ingress["status"] = {
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

    print(formated_new_ingress)

    # if "status" in new_ingress:
    #     formated_new_ingress["status"] = new_ingress["status"]

    items[namespace].append(formated_new_ingress)
    return ""


@extensions_v1beta1_deployments.route(
    "/apis/extensions/v1beta1/deployments", methods=["GET"]
)
def get_all_namespaced_deploys():
    ret_items = []
    for namespace in items:
        ret_items += items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "PodList",
                "apiVersion": "v1",
                "metadata": {
                    "selfLink": "/apis/extensions/v1beta1/namespaces/production/pods",
                    "resourceVersion": "103529284",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@extensions_v1beta1_deployments.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/deployments", methods=["GET"]
)
def get_deploys(namespace):

    ret_items = []

    if namespace in items:
        ret_items = items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "DeploymentList",
                "apiVersion": "extensions/v1beta1",
                "metadata": {
                    "selfLink": f"/apis/extensions/v1beta1/namespaces/{namespace}/deployments",
                    "resourceVersion": "108445344",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@extensions_v1beta1_deployments.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/deployments/<deployment_name>",
    methods=["DELETE"],
)
def delete_deploy(namespace, deployment_name):

    found = False

    if namespace in items:
        for item in items[namespace]:
            if item["metadata"]["name"] == deployment_name:
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
                "name": deployment_name,
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
            "message": f'pods "{deployment_name}" not found',
            "reason": "NotFound",
            "details": {"name": deployment_name, "kind": "pods"},
            "code": 404,
        }

    return Response(response=json.dumps(ret), status=200, mimetype="application/json")
