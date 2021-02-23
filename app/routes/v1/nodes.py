import logging
import json
import datetime
import uuid

from flask import Blueprint, request, Response

logger = logging.getLogger(__name__)
v1_nodes = Blueprint("v1_nodes", __name__)

items = [
    {
        "metadata": {
            "name": "aks-agentpool-26722002-vmss0000bb",
            "selfLink": "/api/v1/nodes/aks-agentpool-26722002-vmss0000bb",
            "uid": str(uuid.uuid4()),
            "resourceVersion": "108427685",
            "creationTimestamp": datetime.datetime.utcnow().strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "labels": {
                "agentpool": "agentpool",
                "beta.kubernetes.io/arch": "amd64",
                "beta.kubernetes.io/instance-type": "Standard_F2s_v2",
                "beta.kubernetes.io/os": "linux",
                "failure-domain.beta.kubernetes.io/region": "eastus2",
                "failure-domain.beta.kubernetes.io/zone": "eastus2-2",
                "kubernetes.azure.com/cluster": "MC_camerite-plataform-production_camerite-plataform-productionz",
                "kubernetes.azure.com/node-image-version": "AKSUbuntu-1604-2020.03.05",
                "kubernetes.azure.com/role": "agent",
                "kubernetes.io/arch": "amd64",
                "kubernetes.io/hostname": "aks-agentpool-26722002-vmss0000bb",
                "kubernetes.io/os": "linux",
                "kubernetes.io/role": "agent",
                "node-role.kubernetes.io/agent": "",
                "storageprofile": "managed",
                "storagetier": "Premium_LRS",
            },
            "annotations": {
                "node.alpha.kubernetes.io/ttl": "0",
                "volumes.kubernetes.io/controller-managed-attach-detach": "true",
            },
        },
        "spec": {
            "providerID": "azure:///subscriptions/3b5a688b-c118-4b17-a167-3e8d04449b8d/resourceGroups/mc_camerite-plataform-production_camerite-plataform-production_eastus2/providers/Microsoft.Compute/virtualMachineScaleSets/aks-agentpool-26722002-vmss/virtualMachines/407"
        },
        "status": {
            "capacity": {
                "attachable-volumes-azure-disk": "4",
                "cpu": "2",
                "ephemeral-storage": "50633320Ki",
                "hugepages-1Gi": "0",
                "hugepages-2Mi": "0",
                "memory": "4017252Ki",
                "pods": "100",
            },
            "allocatable": {
                "attachable-volumes-azure-disk": "4",
                "cpu": "1900m",
                "ephemeral-storage": "46663667635",
                "hugepages-1Gi": "0",
                "hugepages-2Mi": "0",
                "memory": "2200676Ki",
                "pods": "100",
            },
            "conditions": [
                {
                    "type": "MemoryPressure",
                    "status": "False",
                    "lastHeartbeatTime": "2021-02-23T20:38:26Z",
                    "lastTransitionTime": "2021-02-16T08:46:03Z",
                    "reason": "KubeletHasSufficientMemory",
                    "message": "kubelet has sufficient memory available",
                },
                {
                    "type": "DiskPressure",
                    "status": "False",
                    "lastHeartbeatTime": "2021-02-23T20:38:26Z",
                    "lastTransitionTime": "2021-02-16T08:46:03Z",
                    "reason": "KubeletHasNoDiskPressure",
                    "message": "kubelet has no disk pressure",
                },
                {
                    "type": "PIDPressure",
                    "status": "False",
                    "lastHeartbeatTime": "2021-02-23T20:38:26Z",
                    "lastTransitionTime": "2021-02-16T08:46:03Z",
                    "reason": "KubeletHasSufficientPID",
                    "message": "kubelet has sufficient PID available",
                },
                {
                    "type": "Ready",
                    "status": "True",
                    "lastHeartbeatTime": "2021-02-23T20:38:26Z",
                    "lastTransitionTime": "2021-02-16T08:46:03Z",
                    "reason": "KubeletReady",
                    "message": "kubelet is posting ready status. AppArmor enabled",
                },
            ],
            "addresses": [
                {"type": "Hostname", "address": "aks-agentpool-26722002-vmss0000bb"},
                {"type": "InternalIP", "address": "10.20.6.84"},
            ],
            "daemonEndpoints": {"kubeletEndpoint": {"Port": 10250}},
            "nodeInfo": {
                "machineID": "203108ea171f44bfbfe31830340427d6",
                "systemUUID": "01A28068-4EFD-244A-8624-3D148927BF5C",
                "bootID": "54981b9f-947e-4376-a225-0f9d61bfd50f",
                "kernelVersion": "4.15.0-1071-azure",
                "osImage": "Ubuntu 16.04.6 LTS",
                "containerRuntimeVersion": "docker://3.0.10+azure",
                "kubeletVersion": "v1.14.8",
                "kubeProxyVersion": "v1.14.8",
                "operatingSystem": "linux",
                "architecture": "amd64",
            },
            "images": [
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:08ce7ac99db7a4a400633f8a2c5706e6cea6bda7088fbe2a75f88ba6b27f0d9b",
                        "plataformproductionacr.azurecr.io/app:4732",
                    ],
                    "sizeBytes": 783182988,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:4dc1e3a6878889175b75946375e78778d6c44aabe846960384d301b01b504a8d",
                        "plataformproductionacr.azurecr.io/app:4255",
                    ],
                    "sizeBytes": 780426232,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:6eb8ee75e9d2494db3e2d4fc7f5c9549c5f16b92c4d856fee7fc816ff84d5b34",
                        "plataformproductionacr.azurecr.io/app:4254",
                    ],
                    "sizeBytes": 780391921,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:1f9cb573d8871917cd7ba993d3d9ffd8cb40a0f201c3e9eac02604da026d31b5",
                        "plataformproductionacr.azurecr.io/app:4253",
                    ],
                    "sizeBytes": 780384044,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:3d2dd62947ab569bb9f7e346a0d542b194866754c5e5e108a258b80583bb0605",
                        "plataformproductionacr.azurecr.io/app:4247",
                    ],
                    "sizeBytes": 780339878,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:c7f1f943caf2c18a18626d769da26a557b876990ebc27e56301635be0680bd19",
                        "plataformproductionacr.azurecr.io/app:4235",
                    ],
                    "sizeBytes": 780103011,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:0228710d12b74195fdbfdc3b7ab9fb46519dba62c9d1278734c4c6242d0877db",
                        "plataformproductionacr.azurecr.io/app:4191",
                    ],
                    "sizeBytes": 780041086,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:a5a4da11de4698fe1233b5fd31c463b7688c73e8c0e950ee38070db255a2ea3f",
                        "plataformproductionacr.azurecr.io/app:4185",
                    ],
                    "sizeBytes": 779843261,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:4867b6fb77eb85bb1b27ddc04b60e5578c1ec41cf8fb575cb65732011aa3b817",
                        "plataformproductionacr.azurecr.io/app:4164",
                    ],
                    "sizeBytes": 779833042,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:f1844b3b998bbb7cd61a5ffae76ba55be6d73b3d5f2034fa8776ba3ed4c98a1a",
                        "plataformproductionacr.azurecr.io/app:4140",
                    ],
                    "sizeBytes": 779787604,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:d265acfc1874783897a1db9129eedab86aecea83ccb3e73f2d9f647895e1a014",
                        "plataformproductionacr.azurecr.io/app:4934",
                    ],
                    "sizeBytes": 773667094,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:aa698babb58bb9f7c93bd6e5b9c665758ab6398b3f51ade06d376c0b2796e2e1",
                        "plataformproductionacr.azurecr.io/app:4915",
                    ],
                    "sizeBytes": 773644432,
                },
                {
                    "names": [
                        "plataformproductionacr.azurecr.io/app@sha256:97dbf1d8bd0a8493aefb295a3301ac76710061a58fb33a668a0d7c2d31f6dcf6",
                        "plataformproductionacr.azurecr.io/app:4907",
                    ],
                    "sizeBytes": 773625633,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/hyperkube@sha256:27355a15ddc5834100c225979b92b6b6e30c1691a1433d2636911df9326e9f83",
                        "mcr.microsoft.com/oss/kubernetes/hyperkube:v1.14.8-hotfix.20200529.1",
                    ],
                    "sizeBytes": 770490271,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:a01860de0830e460c7b1f80c75a204390a1c837bdaccdc9dc298d166529f1ce6",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod01112021",
                    ],
                    "sizeBytes": 554653119,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:92023bbf142c777915fbef5feeac9bb23a692c7d802090bb081666f77edb5c38",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod11092020",
                    ],
                    "sizeBytes": 544233220,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:526f024b02d88809bc3bdc998943e1f2cc25bb9dbbf82eb159a346b7f4138506",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod10272020",
                    ],
                    "sizeBytes": 540739090,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:532c608ad5e68f78ec73ca95ea5d985edd80aada10a8fcd9afd04caee10218de",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod10052020",
                    ],
                    "sizeBytes": 540403962,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:780131d482cbbf9c2b221c307f699fbbe2ced9ffad74083ea6565cdabd5c91f4",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod08072020",
                    ],
                    "sizeBytes": 536621814,
                },
                {
                    "names": [
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod@sha256:e5a5787184e6405980bf9c38a6f05137996547d9f02ee3a5af047929b32a940c",
                        "mcr.microsoft.com/azuremonitor/containerinsights/ciprod:ciprod07152020",
                    ],
                    "sizeBytes": 429070490,
                },
                {
                    "names": [
                        "us.gcr.io/k8s-artifacts-prod/ingress-nginx/controller@sha256:0e072dddd1f7f8fc8909a2ca6f65e76c5f0d2fcfb8be47935ae3457e8bbceb20",
                        "us.gcr.io/k8s-artifacts-prod/ingress-nginx/controller:v0.34.1",
                    ],
                    "sizeBytes": 328878603,
                },
                {
                    "names": [
                        "quay.io/kubernetes-ingress-controller/nginx-ingress-controller@sha256:b312c91d0de688a21075078982b5e3a48b13b46eda4df743317d3059fc3ca0d9",
                        "quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.30.0",
                    ],
                    "sizeBytes": 322915865,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/azure-npm@sha256:2a72c55556655834dadbe856cdf3a325325c893dc67ca5b9e7a1e198662a55fe",
                        "mcr.microsoft.com/containernetworking/azure-npm:v1.1.8",
                    ],
                    "sizeBytes": 179364698,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/azure-npm@sha256:3652926fdb4afba317377076726100b4c5670ee2ed297d3fd676e08a2cf32325",
                        "mcr.microsoft.com/containernetworking/azure-npm:v1.1.7",
                    ],
                    "sizeBytes": 152192978,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/azure-npm@sha256:0f2443de9f11d3e0d16bdc836d152cbbf3a4ba3309ca30f6d5ca65f8051b8095",
                        "mcr.microsoft.com/containernetworking/azure-npm:v1.1.5",
                    ],
                    "sizeBytes": 151205567,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/azure-npm@sha256:d1ef2bebbb62bf9f97c7d51d6d799c673d638b78ac4eae51c71268b1bbab9209",
                        "mcr.microsoft.com/containernetworking/azure-npm:v1.1.4",
                    ],
                    "sizeBytes": 132464587,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/networkmonitor@sha256:0cfe44a07bf7405ff5e9573ef1aabf3c7df034ffa6d626a9bd470da98eb8559a",
                        "mcr.microsoft.com/containernetworking/networkmonitor:v1.1.8",
                    ],
                    "sizeBytes": 124708650,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/kubernetes-dashboard@sha256:dca7e06333b41acd5ba4c6554d93d7b57cf74a1f2c90a72dbbe39cbb40f86979",
                        "mcr.microsoft.com/oss/kubernetes/kubernetes-dashboard:v1.10.1",
                    ],
                    "sizeBytes": 121711221,
                },
                {
                    "names": [
                        "mcr.microsoft.com/containernetworking/networkmonitor@sha256:1ab5ce423894918c4fd7ec5533837e943dc0fb4c762c3f751486359348d4f8c9",
                        "mcr.microsoft.com/containernetworking/networkmonitor:v0.0.7",
                    ],
                    "sizeBytes": 104673601,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/ip-masq-agent@sha256:c25e53d5a32b1ae09750774307d2b5790893ccea5480d990cb57aa6ac35c5f9a",
                        "mcr.microsoft.com/oss/kubernetes/ip-masq-agent:v2.5.0.2",
                    ],
                    "sizeBytes": 59464125,
                },
                {
                    "names": [
                        "quay.io/jetstack/cert-manager-controller@sha256:7928d472d4abc001d289e438170a61fc5cf004f736d874ce9cb68e3e4a6c9e48",
                        "quay.io/jetstack/cert-manager-controller:v0.9.1",
                    ],
                    "sizeBytes": 51771795,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/ip-masq-agent@sha256:bddf19be25644c7176e8c501465dbad07d032288334f135877b984660b0d3ee6",
                        "mcr.microsoft.com/oss/kubernetes/ip-masq-agent:v2.5.0",
                    ],
                    "sizeBytes": 50148508,
                },
                {
                    "names": [
                        "quay.io/jetstack/cert-manager-cainjector@sha256:3123cd2427ea1988fb1f6b8d7c7c9dc2ba1d423e2f9e7e66a495b921ea5b509c",
                        "quay.io/jetstack/cert-manager-cainjector:v0.8.0",
                    ],
                    "sizeBytes": 44756002,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/coredns@sha256:fe1a122eeca3beaf643c19aeba64b9e1834235da76e1f5be604ad25b57e95398",
                        "mcr.microsoft.com/oss/kubernetes/coredns:1.6.6",
                    ],
                    "sizeBytes": 40853219,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/autoscaler/cluster-proportional-autoscaler@sha256:1be911b269aba912facbbdcdd33ffeb091bd4b4b326c979f24ab21d9b85dc395",
                        "mcr.microsoft.com/oss/kubernetes/autoscaler/cluster-proportional-autoscaler:1.7.1-hotfix.20200403",
                    ],
                    "sizeBytes": 40682655,
                },
                {
                    "names": [
                        "mcr.microsoft.com/oss/kubernetes/metrics-server@sha256:47042a74b6968faeb1ea3fcabddf5319d003586c6019fe981675ea151e629484",
                        "mcr.microsoft.com/oss/kubernetes/metrics-server:v0.3.6",
                    ],
                    "sizeBytes": 39944451,
                },
                {
                    "names": [
                        "quay.io/jetstack/cert-manager-acmesolver@sha256:46a3fd5d52723054031de11b7093a3cd092d1df7d92b58d53e27cee799546ef4",
                        "quay.io/jetstack/cert-manager-acmesolver:v0.8.0",
                    ],
                    "sizeBytes": 32788026,
                },
                {
                    "names": [
                        "quay.io/jetstack/cert-manager-acmesolver@sha256:3d9b9ea7e6514468354e79c7f8885247729ebf997a2ad07fb03b9ee15369a38d",
                        "quay.io/jetstack/cert-manager-acmesolver:v0.9.1",
                    ],
                    "sizeBytes": 30089727,
                },
                {
                    "names": [
                        "mcr.microsoft.com/k8s/core/pause@sha256:6666771bdc36e6c335f8bfcc1976fc0624c1dd9bc9fa9793ea27ccd6de5e4289",
                        "mcr.microsoft.com/k8s/core/pause:1.2.0",
                    ],
                    "sizeBytes": 738384,
                },
            ],
            "config": {},
        },
    }
]


@v1_nodes.route("/api/v1/nodes", methods=["GET"])
def get_all_nodes():

    return Response(
        response=json.dumps(
            {
                "kind": "NodeList",
                "apiVersion": "v1",
                "metadata": {
                    "selfLink": "/api/v1/nodes",
                    "resourceVersion": "108427802",
                },
                "items": items,
            }
        ),
        status=200,
        mimetype="application/json",
    )
