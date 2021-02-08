# kubernetes-cluster-mock

<img src="https://img.shields.io/badge/python-3.7.5-blue"> <img src="https://img.shields.io/github/license/digital-divas/PINP"> ![Python application](https://github.com/ezequielramos/azure-cosmos-emulator/workflows/Python%20application/badge.svg)

kubernetes-cluster-mock is a mock to a Kubernetes Cluster API using Flask. You can use it to test your application that integrates with Kubernetes API.

kubernetes-cluster-mock is available on dockerhub. To run it, just execute:

```bash
docker run -d -p 9988:9988 ezequielmr94/kubernetes-cluster-mock:latest
```

Inside the `assets` folder you can find a kube config file to access the kubernetes-cluster-mock service.

For now, you can:

- [x] Create a ingress
- [x] List ingresses
- [x] Delete a ingress
- [ ] Create a ingress using `kubectl create -f`
- [x] Create a pod
- [x] List pods
- [x] Delete a pod
- [ ] Create a pod using `kubectl create -f`
- [ ] Create a deploy
- [ ] List deploys
- [ ] Delete a deploy
- [ ] Create a deploy using `kubectl create -f`
