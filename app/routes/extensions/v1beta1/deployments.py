import logging
import json

from flask import Blueprint, request, Response

from app.resources.deployments import create_item, delete_item
from app.resources.deployments import deployments as items

logger = logging.getLogger(__name__)
extensions_v1beta1_deployments = Blueprint("extensions_v1beta1_deployments", __name__)


@extensions_v1beta1_deployments.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/deployments", methods=["POST"]
)
def post_deploy(namespace):
    deploy = json.loads(request.data)
    create_item(namespace, deploy)
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

    found, item = delete_item(namespace, deployment_name)

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
