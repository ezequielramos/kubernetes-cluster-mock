const k8s = require('@kubernetes/client-node');

function getDeployBody(addIngress) {
    return {
        apiVersion: "extensions/v1beta1",
        kind: "Ingress",
        metadata: {
            name: "camerite-plataform-ingress-" + addIngress,
            namespace: "production",
            labels: {
                "certmanager-solver": "nginx-camerite-plataform-production"
            },
            annotations: {
                "kubernetes.io/ingress.class": "nginx-camerite-plataform-production",
                "kubernetes.io/tls-acme": "true",
                "meta.helm.sh/release-name": "camerite-plataform-ingress",
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
                host: addIngress,
                http: {
                    paths: [{
                        path: "/",
                        backend: {
                            serviceName: "camerite-plataform-app",
                            servicePort: 3000
                        }
                    }]
                }
            }],
            tls: [{
                hosts: [addIngress],
                secretName: addIngress + "-tls"
            }]
        }
    };
}


(async () => {
    const kc = new k8s.KubeConfig();
    kc.loadFromDefault();
    const k8sApi = kc.makeApiClient(k8s.Extensions_v1beta1Api);

    await k8sApi.listNamespacedIngress('production');
    await k8sApi.createNamespacedIngress("production", getDeployBody('hahuahua'));
})();
