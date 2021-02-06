from flask import Flask
from flask import request, Response
import json

app = Flask(__name__)


@app.route("/api")
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


@app.route("/apis")
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


@app.route(
    "/apis/extensions/v1beta1/namespaces/<namespace>/ingresses", methods=["POST"]
)
def post_ingresses(namespace):
    return ""


@app.route("/apis/extensions/v1beta1/namespaces/<namespace>/ingresses", methods=["GET"])
def get_ingresses(namespace):

    items = [
        {
            "metadata": {
                "name": "camerite-plataform-http",
                "namespace": "production",
                "selfLink": "/apis/extensions/v1beta1/namespaces/production/ingresses/camerite-plataform-http",
                "uid": "62749880-88cd-11ea-ab84-a6dd52d5633a",
                "resourceVersion": "92452924",
                "generation": 3,
                "creationTimestamp": "2020-04-27T21:23:48Z",
                "labels": {
                    "certmanager-solver": "nginx-camerite-plataform-wildcard-production"
                },
                "annotations": {
                    "certmanager.k8s.io/cluster-issuer": "letsencrypt-prod",
                    "kubernetes.io/ingress.class": "nginx-camerite-plataform-production",
                    "kubernetes.io/tls-acme": "true",
                    "nginx.ingress.kubernetes.io/configuration-snippet": 'proxy_set_header whitelabel "$host";\n',
                    "nginx.ingress.kubernetes.io/proxy-body-size": "0",
                    "nginx.ingress.kubernetes.io/ssl-redirect": "false",
                },
            },
            "spec": {
                "tls": [
                    {
                        "hosts": ["*.camerite.com"],
                        "secretName": "camerite-plataform-tls",
                    }
                ],
                "rules": [
                    {
                        "host": "*.camerite.com",
                        "http": {
                            "paths": [
                                {
                                    "path": "/api/mobile/sendpush/zowee",
                                    "backend": {
                                        "serviceName": "camerite-plataform-app",
                                        "servicePort": 3000,
                                    },
                                },
                                {
                                    "path": "/api/rtmp-auth",
                                    "backend": {
                                        "serviceName": "camerite-plataform-app",
                                        "servicePort": 3000,
                                    },
                                },
                                {
                                    "path": "/healthz",
                                    "backend": {
                                        "serviceName": "camerite-plataform-app",
                                        "servicePort": 3000,
                                    },
                                },
                            ]
                        },
                    }
                ],
            },
            "status": {
                "loadBalancer": {
                    "ingress": [
                        {"ip": "10.20.0.4"},
                        {"ip": "10.20.1.152"},
                        {"ip": "10.20.1.253"},
                        {"ip": "10.20.1.51"},
                        {"ip": "10.20.2.199"},
                        {"ip": "10.20.2.98"},
                        {"ip": "10.20.3.145"},
                        {"ip": "10.20.3.44"},
                        {"ip": "10.20.4.91"},
                        {"ip": "10.20.6.84"},
                    ]
                }
            },
        }
    ]

    return Response(
        response=json.dumps(
            {
                "kind": "IngressList",
                "apiVersion": "extensions/v1beta1",
                "metadata": {
                    "selfLink": "/apis/extensions/v1beta1/namespaces/default/ingresses",
                    "resourceVersion": "102889374",
                },
                "items": items,
            }
        ),
        status=200,
        mimetype="application/json",
    )


@app.route("/api/v1")
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


@app.route("/apis/networking.k8s.io/v1beta1")
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


@app.route("/apis/extensions/v1beta1")
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


app.run(port=9988, debug=True)
