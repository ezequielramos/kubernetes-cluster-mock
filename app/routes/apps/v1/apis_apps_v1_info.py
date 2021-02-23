import logging
import json
import datetime

from flask import Blueprint, request, Response

logger = logging.getLogger(__name__)
apis_apps_v1_info = Blueprint("apis_apps_v1_info", __name__)


@apis_apps_v1_info.route("/apis/apps/v1")
@apis_apps_v1_info.route("/apis/apps/v1beta2")
@apis_apps_v1_info.route("/apis/apps/v1beta1")
def apis_apps_v1_get_info():
    return json.dumps(
        {
            "kind": "APIResourceList",
            "apiVersion": "v1",
            "groupVersion": "apps/v1",
            "resources": [
                {
                    "name": "controllerrevisions",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ControllerRevision",
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
                },
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
                    "categories": ["all"],
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
                    "categories": ["all"],
                },
                {
                    "name": "deployments/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "autoscaling",
                    "version": "v1",
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
                    "categories": ["all"],
                },
                {
                    "name": "replicasets/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "autoscaling",
                    "version": "v1",
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
                    "name": "statefulsets",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "StatefulSet",
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
                    "shortNames": ["sts"],
                    "categories": ["all"],
                },
                {
                    "name": "statefulsets/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "autoscaling",
                    "version": "v1",
                    "kind": "Scale",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "statefulsets/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "StatefulSet",
                    "verbs": ["get", "patch", "update"],
                },
            ],
        }
    )
