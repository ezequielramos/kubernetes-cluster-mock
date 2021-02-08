import logging
import json
import datetime

from flask import Blueprint, request, Response

logger = logging.getLogger(__name__)
api_networkingk8sio_v1beta1_info = Blueprint(
    "api_networkingk8sio_v1beta1_info", __name__
)


@api_networkingk8sio_v1beta1_info.route("/apis/networking.k8s.io/v1beta1")
def networking_v1beta1():
    return json.dumps(
        {
            "kind": "APIResourceList",
            "apiVersion": "v1",
            "groupVersion": "networking.k8s.io/v1beta1",
            "resources": [
                {
                    "name": "ingresses",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Ingress",
                    "verbs": [
                        "create",
                        "delete",
                        "deletecollection",
                        "get",
                        "list",
                        "patch",
                        "update",
                        "watch",
                    ],
                    "shortNames": ["ing"],
                },
                {
                    "name": "ingresses/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Ingress",
                    "verbs": ["get", "patch", "update"],
                },
            ],
        }
    )

