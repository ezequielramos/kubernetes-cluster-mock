import logging
import json
import datetime

from flask import Blueprint, request, Response

logger = logging.getLogger(__name__)
api_extensions_v1beta1_info = Blueprint("api_extensions_v1beta1_info", __name__)


@api_extensions_v1beta1_info.route("/apis/extensions/v1beta1")
def extensions_v1beta1():
    return json.dumps(
        {
            "kind": "APIResourceList",
            "groupVersion": "extensions/v1beta1",
            "resources": [
                {
                    "name": "daemonsets",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "DaemonSet",
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
                    "shortNames": ["ds"],
                },
                {
                    "name": "daemonsets/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "DaemonSet",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "deployments",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Deployment",
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
                    "shortNames": ["deploy"],
                },
                {
                    "name": "deployments/rollback",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "DeploymentRollback",
                    "verbs": ["create"],
                },
                {
                    "name": "deployments/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "extensions",
                    "version": "v1beta1",
                    "kind": "Scale",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "deployments/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Deployment",
                    "verbs": ["get", "patch", "update"],
                },
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
                {
                    "name": "networkpolicies",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "NetworkPolicy",
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
                    "shortNames": ["netpol"],
                },
                {
                    "name": "podsecuritypolicies",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodSecurityPolicy",
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
                    "shortNames": ["psp"],
                },
                {
                    "name": "replicasets",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ReplicaSet",
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
                    "shortNames": ["rs"],
                },
                {
                    "name": "replicasets/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "extensions",
                    "version": "v1beta1",
                    "kind": "Scale",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "replicasets/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ReplicaSet",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "replicationcontrollers",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ReplicationControllerDummy",
                    "verbs": [],
                },
                {
                    "name": "replicationcontrollers/scale",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Scale",
                    "verbs": ["get", "patch", "update"],
                },
            ],
        }
    )
