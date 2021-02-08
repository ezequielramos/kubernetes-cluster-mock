FROM python:3.7.5-stretch 

COPY . /root/kubernetes-cluster-emulator

RUN apt update

WORKDIR /root/kubernetes-cluster-emulator

RUN pip install -r requirements.txt

CMD ["/usr/local/bin/python", "kubernetes-cluster-emulator.py"]