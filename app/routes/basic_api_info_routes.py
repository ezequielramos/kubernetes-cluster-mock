import logging
import json
import gzip

from flask import Blueprint, request, Response, make_response

logger = logging.getLogger(__name__)
basic_api_info_routes = Blueprint("basic_api_info_routes", __name__)


@basic_api_info_routes.route("/api")
def api():
    return Response(
        response=json.dumps(
            {
                "kind": "APIVersions",
                "versions": ["v1"],
                "serverAddressByClientCIDRs": [
                    {"clientCIDR": "0.0.0.0/0", "serverAddress": '"localhost":9988'}
                ],
            }
        ),
        status=200,
        mimetype="application/json",
    )


@basic_api_info_routes.route("/apis")
def apis():
    return json.dumps(
        {
            "kind": "APIGroupList",
            "apiVersion": "v1",
            "groups": [
                {
                    "name": "extensions",
                    "versions": [
                        {"groupVersion": "extensions/v1beta1", "version": "v1beta1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "extensions/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "apps",
                    "versions": [
                        {"groupVersion": "apps/v1", "version": "v1"},
                        {"groupVersion": "apps/v1beta2", "version": "v1beta2"},
                        {"groupVersion": "apps/v1beta1", "version": "v1beta1"},
                    ],
                    "preferredVersion": {"groupVersion": "apps/v1", "version": "v1"},
                },
                {
                    "name": "events.k8s.io",
                    "versions": [
                        {"groupVersion": "events.k8s.io/v1beta1", "version": "v1beta1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "events.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "authentication.k8s.io",
                    "versions": [
                        {"groupVersion": "authentication.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "authentication.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "authentication.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "authorization.k8s.io",
                    "versions": [
                        {"groupVersion": "authorization.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "authorization.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "authorization.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "autoscaling",
                    "versions": [
                        {"groupVersion": "autoscaling/v1", "version": "v1"},
                        {"groupVersion": "autoscaling/v2beta1", "version": "v2beta1"},
                        {"groupVersion": "autoscaling/v2beta2", "version": "v2beta2"},
                    ],
                    "preferredVersion": {
                        "groupVersion": "autoscaling/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "batch",
                    "versions": [
                        {"groupVersion": "batch/v1", "version": "v1"},
                        {"groupVersion": "batch/v1beta1", "version": "v1beta1"},
                    ],
                    "preferredVersion": {"groupVersion": "batch/v1", "version": "v1"},
                },
                {
                    "name": "certificates.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "certificates.k8s.io/v1beta1",
                            "version": "v1beta1",
                        }
                    ],
                    "preferredVersion": {
                        "groupVersion": "certificates.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "networking.k8s.io",
                    "versions": [
                        {"groupVersion": "networking.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "networking.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "networking.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "policy",
                    "versions": [
                        {"groupVersion": "policy/v1beta1", "version": "v1beta1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "policy/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "rbac.authorization.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "rbac.authorization.k8s.io/v1",
                            "version": "v1",
                        },
                        {
                            "groupVersion": "rbac.authorization.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "rbac.authorization.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "storage.k8s.io",
                    "versions": [
                        {"groupVersion": "storage.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "storage.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "storage.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "admissionregistration.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "admissionregistration.k8s.io/v1beta1",
                            "version": "v1beta1",
                        }
                    ],
                    "preferredVersion": {
                        "groupVersion": "admissionregistration.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "apiextensions.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "apiextensions.k8s.io/v1beta1",
                            "version": "v1beta1",
                        }
                    ],
                    "preferredVersion": {
                        "groupVersion": "apiextensions.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "scheduling.k8s.io",
                    "versions": [
                        {"groupVersion": "scheduling.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "scheduling.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "scheduling.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "coordination.k8s.io",
                    "versions": [
                        {"groupVersion": "coordination.k8s.io/v1", "version": "v1"},
                        {
                            "groupVersion": "coordination.k8s.io/v1beta1",
                            "version": "v1beta1",
                        },
                    ],
                    "preferredVersion": {
                        "groupVersion": "coordination.k8s.io/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "node.k8s.io",
                    "versions": [
                        {"groupVersion": "node.k8s.io/v1beta1", "version": "v1beta1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "node.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "azmon.container.insights",
                    "versions": [
                        {"groupVersion": "azmon.container.insights/v1", "version": "v1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "azmon.container.insights/v1",
                        "version": "v1",
                    },
                },
                {
                    "name": "certmanager.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "certmanager.k8s.io/v1alpha1",
                            "version": "v1alpha1",
                        }
                    ],
                    "preferredVersion": {
                        "groupVersion": "certmanager.k8s.io/v1alpha1",
                        "version": "v1alpha1",
                    },
                },
                {
                    "name": "admission.certmanager.k8s.io",
                    "versions": [
                        {
                            "groupVersion": "admission.certmanager.k8s.io/v1beta1",
                            "version": "v1beta1",
                        }
                    ],
                    "preferredVersion": {
                        "groupVersion": "admission.certmanager.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
                {
                    "name": "metrics.k8s.io",
                    "versions": [
                        {"groupVersion": "metrics.k8s.io/v1beta1", "version": "v1beta1"}
                    ],
                    "preferredVersion": {
                        "groupVersion": "metrics.k8s.io/v1beta1",
                        "version": "v1beta1",
                    },
                },
            ],
        }
    )


@basic_api_info_routes.route("/api/v1")
def api_v1():
    return json.dumps(
        {
            "kind": "APIResourceList",
            "groupVersion": "v1",
            "resources": [
                {
                    "name": "bindings",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Binding",
                    "verbs": ["create"],
                },
                {
                    "name": "componentstatuses",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "ComponentStatus",
                    "verbs": ["get", "list"],
                    "shortNames": ["cs"],
                },
                {
                    "name": "configmaps",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ConfigMap",
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
                    "shortNames": ["cm"],
                },
                {
                    "name": "endpoints",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Endpoints",
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
                    "shortNames": ["ep"],
                },
                {
                    "name": "events",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Event",
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
                    "shortNames": ["ev"],
                },
                {
                    "name": "limitranges",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "LimitRange",
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
                    "shortNames": ["limits"],
                },
                {
                    "name": "namespaces",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "Namespace",
                    "verbs": [
                        "create",
                        "delete",
                        "get",
                        "list",
                        "patch",
                        "update",
                        "watch",
                    ],
                    "shortNames": ["ns"],
                },
                {
                    "name": "namespaces/finalize",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "Namespace",
                    "verbs": ["update"],
                },
                {
                    "name": "namespaces/status",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "Namespace",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "nodes",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "Node",
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
                    "shortNames": ["no"],
                },
                {
                    "name": "nodes/proxy",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "NodeProxyOptions",
                    "verbs": ["create", "delete", "get", "patch", "update"],
                },
                {
                    "name": "nodes/status",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "Node",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "persistentvolumeclaims",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PersistentVolumeClaim",
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
                    "shortNames": ["pvc"],
                },
                {
                    "name": "persistentvolumeclaims/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PersistentVolumeClaim",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "persistentvolumes",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "PersistentVolume",
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
                    "shortNames": ["pv"],
                },
                {
                    "name": "persistentvolumes/status",
                    "singularName": "",
                    "namespaced": False,
                    "kind": "PersistentVolume",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "pods",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Pod",
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
                    "shortNames": ["po"],
                    "categories": ["all"],
                },
                {
                    "name": "pods/attach",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodAttachOptions",
                    "verbs": ["create", "get"],
                },
                {
                    "name": "pods/binding",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Binding",
                    "verbs": ["create"],
                },
                {
                    "name": "pods/eviction",
                    "singularName": "",
                    "namespaced": True,
                    "group": "policy",
                    "version": "v1beta1",
                    "kind": "Eviction",
                    "verbs": ["create"],
                },
                {
                    "name": "pods/exec",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodExecOptions",
                    "verbs": ["create", "get"],
                },
                {
                    "name": "pods/log",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Pod",
                    "verbs": ["get"],
                },
                {
                    "name": "pods/portforward",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodPortForwardOptions",
                    "verbs": ["create", "get"],
                },
                {
                    "name": "pods/proxy",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodProxyOptions",
                    "verbs": ["create", "delete", "get", "patch", "update"],
                },
                {
                    "name": "pods/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Pod",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "podtemplates",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "PodTemplate",
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
                    "name": "replicationcontrollers",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ReplicationController",
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
                    "shortNames": ["rc"],
                    "categories": ["all"],
                },
                {
                    "name": "replicationcontrollers/scale",
                    "singularName": "",
                    "namespaced": True,
                    "group": "autoscaling",
                    "version": "v1",
                    "kind": "Scale",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "replicationcontrollers/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ReplicationController",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "resourcequotas",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ResourceQuota",
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
                    "shortNames": ["quota"],
                },
                {
                    "name": "resourcequotas/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ResourceQuota",
                    "verbs": ["get", "patch", "update"],
                },
                {
                    "name": "secrets",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Secret",
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
                    "name": "serviceaccounts",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ServiceAccount",
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
                    "shortNames": ["sa"],
                },
                {
                    "name": "serviceaccounts/token",
                    "singularName": "",
                    "namespaced": True,
                    "group": "authentication.k8s.io",
                    "version": "v1",
                    "kind": "TokenRequest",
                    "verbs": ["create"],
                },
                {
                    "name": "services",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Service",
                    "verbs": [
                        "create",
                        "delete",
                        "get",
                        "list",
                        "patch",
                        "update",
                        "watch",
                    ],
                    "shortNames": ["svc"],
                    "categories": ["all"],
                },
                {
                    "name": "services/proxy",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "ServiceProxyOptions",
                    "verbs": ["create", "delete", "get", "patch", "update"],
                },
                {
                    "name": "services/status",
                    "singularName": "",
                    "namespaced": True,
                    "kind": "Service",
                    "verbs": ["get", "patch", "update"],
                },
            ],
        }
    )


@basic_api_info_routes.route("/swagger-2.0.0.pb-v1", methods=["GET"])
def swagger_info():
    return json.dumps(
        {
            "paths": [
                "/apis",
                "/apis/",
                "/apis/apiextensions.k8s.io",
                "/apis/apiextensions.k8s.io/v1beta1",
                "/healthz",
                "/healthz/etcd",
                "/healthz/log",
                "/healthz/ping",
                "/healthz/poststarthook/crd-informer-synced",
                "/healthz/poststarthook/generic-apiserver-start-informers",
                "/healthz/poststarthook/start-apiextensions-controllers",
                "/healthz/poststarthook/start-apiextensions-informers",
                "/metrics",
                "/openapi/v2",
                "/version",
            ]
        }
    )


@basic_api_info_routes.route("/openapi/v2", methods=["GET"])
def openapiv2():
    file = open("app/routes/wtf.json", "rb")

    content = gzip.compress(json.dumps(json.loads(file.read())).encode("utf8"), 5)

    # response = make_response(content)
    # response.headers["Content-length"] = len(content)
    # response.headers["Content-Encoding"] = "gzip"
    # response.headers["Accept-Ranges"] = "bytes"
    # response.headers["Audit-Id"]: "cdcd1bdb-6641-44ee-9d6e-37c1fb7bb446"
    # response.headers[
    #     "Etag"
    # ] = '"C2298C195737DD3BBAEF8546CC568D7A4CC0EE374EFA46410BC12B6CEA0CF7F50F05379EAE84A7F27C178BDB194516ED8D79FE05A395371D8E0CA652E2AF5E1F"'
    # response.headers["Last-Modified"] = "Sat, 06 Feb 2021 16:54:47 GMT"
    # response.headers["Vary"] = "Accept-Encoding"
    # response.headers["Date"] = "Mon, 08 Feb 2021 00:42:12 GMT"
    # response.headers["Transfer-Encoding"] = "chunked"

    def generate():

        i = 0
        chunk_size = 100
        chunks = []

        while i < len(content):
            if i + chunk_size > len(content):
                chunks.append(content[i:])
            else:
                chunks.append(content[i:chunk_size])
            i += 100

        for i, row in enumerate(chunks):
            if len(chunks) - 1 == i:
                yield gzip.compress(row + b"\n")
            else:
                yield gzip.compress(row + b",\n")

    return Response(
        generate(),
        mimetype="text/plain; charset=utf-8",
        headers={
            "Content-Encoding": "gzip",
            "Accept-Ranges": "bytes",
            "Transfer-Encoding": "chunked",
        },
    )

    # return response
