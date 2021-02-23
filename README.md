# kubernetes-cluster-mock

<img src="https://img.shields.io/badge/python-3.7.5-blue"> <img src="https://img.shields.io/github/license/digital-divas/PINP"> ![Python application](https://github.com/ezequielramos/azure-cosmos-emulator/workflows/Python%20application/badge.svg)

kubernetes-cluster-mock is a mock to a Kubernetes Cluster API using Flask. You can use it to test your application that integrates with Kubernetes API.

kubernetes-cluster-mock is available on dockerhub. To run it, just execute:

```bash
docker run -d -p 9988:9988 ezequielmr94/kubernetes-cluster-mock:latest
```

Inside the `assets` folder you can find a kube config file to access the kubernetes-cluster-mock service.

For now, you can:

- [x] List Nodes
- [x] Create a ingress
- [x] List ingresses
- [x] Delete a ingress
- [ ] Create a ingress using `kubectl create -f`
- [x] Create a pod
- [x] List pods
- [x] Delete a pod
- [ ] Create a pod using `kubectl create -f`
- [X] Create a deploy
- [X] List deploys
- [X] Delete a deploy
- [ ] Create a deploy using `kubectl create -f`

## How to build?
### Using pyenv with pyenv-virtualenv

You also should use virtualenv to build/develop the project and I recommend the use of [pyenv](https://github.com/pyenv/pyenv) with [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage multiple python environments.


```bash
pyenv install 3.7.5
pyenv virtualenv 3.7.5 kubernetes-cluster-emulator
```

### Installing dependencies (Python 3.7.5)

Open your bash and run the follow command to install all the project dependencies, you just need to run the command one time

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

#### Docker 🐋

Building the docker file:
```bash
docker build . -t ezequielmr94/kubernetes-cluster-mock:latest
```

Uploading the image to the repository:
```bash
docker push ezequielmr94/kubernetes-cluster-mock:latest
```

Pull the latest version of the image:
```bash
docker pull ezequielmr94/kubernetes-cluster-mock:latest
```
