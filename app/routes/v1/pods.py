import logging
import json
import datetime
import uuid

from flask import Blueprint, request, Response

from app.resources.pods import items, create_item

logger = logging.getLogger(__name__)
v1_pods = Blueprint("v1_pods", __name__)


@v1_pods.route("/api/v1/namespaces/<namespace>/pods", methods=["POST"])
def post_pods(namespace):
    pod = json.loads(request.data)
    create_item(namespace, pod)
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
