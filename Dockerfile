FROM python:3.7.5-stretch 

COPY . /root/kubernetes-cluster-mock

RUN apt update

WORKDIR /root/kubernetes-cluster-mock

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/usr/local/bin/python", "kubernetes-cluster-mock.py"]