import logging
import json
import datetime
import uuid

from flask import Blueprint, request, Response

logger = logging.getLogger(__name__)
v1beta1_ingresses = Blueprint("v1beta1_ingresses", __name__)

items = {}


@v1beta1_ingresses.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/ingresses", methods=["POST"]
)
def post_ingresses(namespace):
    new_ingress = json.loads(request.data)
    if namespace not in items:
        items[namespace] = []

    formated_new_ingress = {}

    if "metadata" in new_ingress:
        formated_new_ingress["metadata"] = new_ingress["metadata"]
        formated_new_ingress["metadata"][
            "selfLink"
        ] = f'/apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{new_ingress["metadata"]["name"]}'
        formated_new_ingress["metadata"]["uid"] = str(uuid.uuid4())
        formated_new_ingress["metadata"]["resourceVersion"] = "92452924"
        formated_new_ingress["metadata"]["generation"] = 3
        formated_new_ingress["metadata"][
            "creationTimestamp"
        ] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if "spec" in new_ingress:
        formated_new_ingress["spec"] = new_ingress["spec"]

    # if "status" in new_ingress:
    #     formated_new_ingress["status"] = new_ingress["status"]

    items[namespace].append(new_ingress)
    return ""


@v1beta1_ingresses.route("/apis/extensions/v1beta1/ingresses", methods=["GET"])
def get_all_namespaced_ingresses():
    ret_items = []
    for namespace in items:
        ret_items += items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "IngressList",
                "apiVersion": "extensions/v1beta1",
                "metadata": {
                    "selfLink": "/apis/extensions/v1beta1/namespaces/default/ingresses",
                    "resourceVersion": "102889374",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@v1beta1_ingresses.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/ingresses", methods=["GET"]
)
def get_ingresses(namespace):

    ret_items = []

    if namespace in items:
        ret_items = items[namespace]

    return Response(
        response=json.dumps(
            {
                "kind": "IngressList",
                "apiVersion": "extensions/v1beta1",
                "metadata": {
                    "selfLink": "/apis/extensions/v1beta1/namespaces/default/ingresses",
                    "resourceVersion": "102889374",
                },
                "items": ret_items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@v1beta1_ingresses.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/ingresses/<ingress_name>",
    methods=["DELETE"],
)
def delete_ingress(namespace, ingress_name):

    found = False

    if namespace in items:
        for item in items[namespace]:
            if item["metadata"]["name"] == ingress_name:
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
                "name": ingress_name,
                "group": "extensions",
                "kind": "ingresses",
                "uid": item["metadata"]["uid"],
            },
        }
    else:
        ret = {
            "kind": "Status",
            "apiVersion": "v1",
            "metadata": {},
            "status": "Failure",
            "message": f'ingresses.extensions "{ingress_name}" not found',
            "reason": "NotFound",
            "details": {
                "name": ingress_name,
                "group": "extensions",
                "kind": "ingresses",
            },
            "code": 404,
        }

    return Response(response=json.dumps(ret), status=200, mimetype="application/json")

