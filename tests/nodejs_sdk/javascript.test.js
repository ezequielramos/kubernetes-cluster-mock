const k8s = require('@kubernetes/client-node');

function getDeployBody(ingressName) {
    return {
        apiVersion: "extensions/v1beta1",
        kind: "Ingress",
        metadata: {
            name: "platform-ingress-" + ingressName,
            namespace: "production",
            labels: {
                "certmanager-solver": "nginx-platform-production"
            },
            annotations: {
                "kubernetes.io/ingress.class": "nginx-platform-production",
                "kubernetes.io/tls-acme": "true",
                "meta.helm.sh/release-name": "platform-ingress",
                "meta.helm.sh/release-namespace": "production",
                "certmanager.k8s.io/cluster-issuer": "letsencrypt-prod",
                "nginx.ingress.kubernetes.io/ssl-redirect": "true",
                "nginx.ingress.kubernetes.io/proxy-body-size": "0",
                "nginx.ingress.kubernetes.io/server-snippet": "location = /check-dns {\n  return 200;\n}",
                "nginx.ingress.kubernetes.io/configuration-snippet": 'proxy_set_header Host $host;\nproxy_set_header whitelabel "$host";'
            }
        },
        spec: {
            rules: [{
                host: ingressName,
                http: {
                    paths: [{
                        path: "/",
                        backend: {
                            serviceName: "platform-app",
                            servicePort: 3000
                        }
                    }]
                }
            }],
            tls: [{
                hosts: [ingressName],
                secretName: ingressName + "-tls"
            }]
        }
    };
}

async function ingressTest() {
    const kc = new k8s.KubeConfig();
    kc.loadFromDefault();
    const k8sApi = kc.makeApiClient(k8s.Extensions_v1beta1Api);
    const deploy_name = 'test_ingress';

    await k8sApi.listNamespacedIngress('production');
    await k8sApi.createNamespacedIngress("production", getDeployBody(deploy_name));
    await k8sApi.deleteNamespacedIngress("platform-ingress-" + deploy_name, "production");
}

async function podTest() {
    const kc = new k8s.KubeConfig();
    kc.loadFromDefault();
    const k8sApi = kc.makeApiClient(k8s.Core_v1Api);

    const pod = {
        "metadata": {
            "name": "platform-app-958795556-2nqgj",
            "generateName": "platform-app-958795556-",
            "namespace": "production",
            "labels": {
                "app": "platform",
                "chart": "platform",
                "component": "app",
                "heritage": "Helm",
                "pod-template-hash": "958795556",
                "release": "platform-production",
                "version": "1.0.3"
            },
            "ownerReferences": [
                {
                    "apiVersion": "apps/v1",
                    "kind": "ReplicaSet",
                    "name": "platform-app-958795556",
                    "uid": "35ba938b-681d-11eb-a74a-16e1a04d726b",
                    "controller": true,
                    "blockOwnerDeletion": true
                }
            ]
        },
        "spec": {
            "volumes": [
                {
                    "name": "default-token-2cg25",
                    "secret": {
                        "secretName": "default-token-2cg25",
                        "defaultMode": 420
                    }
                }
            ],
            "containers": [
                {
                    "name": "app",
                    "image": "platform.azurecr.io/app:master",
                    "ports": [
                        {
                            "containerPort": 3000,
                            "protocol": "TCP"
                        }
                    ],
                    "env": [],
                    "resources": {
                        "limits": {
                            "cpu": "1200m",
                            "memory": "1Gi"
                        },
                        "requests": {
                            "cpu": "1",
                            "memory": "768Mi"
                        }
                    },
                    "volumeMounts": [
                        {
                            "name": "default-token-2cg25",
                            "readOnly": true,
                            "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
                        }
                    ],
                    "livenessProbe": {
                        "httpGet": {
                            "path": "/health/liveness",
                            "port": 3000,
                            "scheme": "HTTP"
                        },
                        "initialDelaySeconds": 10,
                        "timeoutSeconds": 5,
                        "periodSeconds": 10,
                        "successThreshold": 1,
                        "failureThreshold": 6
                    },
                    "readinessProbe": {
                        "httpGet": {
                            "path": "/health/readness",
                            "port": 3000,
                            "scheme": "HTTP"
                        },
                        "initialDelaySeconds": 10,
                        "timeoutSeconds": 5,
                        "periodSeconds": 10,
                        "successThreshold": 2,
                        "failureThreshold": 6
                    },
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File",
                    "imagePullPolicy": "Always"
                }
            ],
            "restartPolicy": "Always",
            "terminationGracePeriodSeconds": 30,
            "dnsPolicy": "ClusterFirst",
            "serviceAccountName": "default",
            "serviceAccount": "default",
            "nodeName": "aks-agentpool-26722002-vmss00039t",
            "securityContext": {
                "runAsUser": 1000,
                "fsGroup": 1000
            },
            "schedulerName": "default-scheduler",
            "tolerations": [
                {
                    "key": "node.kubernetes.io/not-ready",
                    "operator": "Exists",
                    "effect": "NoExecute",
                    "tolerationSeconds": 300
                },
                {
                    "key": "node.kubernetes.io/unreachable",
                    "operator": "Exists",
                    "effect": "NoExecute",
                    "tolerationSeconds": 300
                }
            ],
            "priority": 0,
            "enableServiceLinks": true
        }
    };

    await k8sApi.listNamespacedPod('production');
    await k8sApi.createNamespacedPod("production", pod);
    await k8sApi.deleteNamespacedPod(pod.metadata.name, 'production');
}


async function nodeTest() {
    const kc = new k8s.KubeConfig();
    kc.loadFromDefault();
    const k8sApi = kc.makeApiClient(k8s.Core_v1Api);
    await k8sApi.listNode();
}

async function deployTest() {
    const kc = new k8s.KubeConfig();
    kc.loadFromDefault();
    const k8sApi = kc.makeApiClient(k8s.Apps_v1Api);
    await k8sApi.listNamespacedDeployment("production");
}

(async () => {
    try {
        await ingressTest();
        await podTest();
        await nodeTest();
        await deployTest();
    } catch (err) {
        console.error(err);
    }
})();
