import logging

from flask import Blueprint

from app.resources.pods import items as pods
from app.resources.nodes import items as nodes

logger = logging.getLogger(__name__)
custom_routes = Blueprint("custom_routes", __name__)


@custom_routes.route(
    "/custom_routes/change_pod_phase/<namespace>/<pod_name>/<phase>", methods=["POST"]
)
def change_pod_phase(namespace, pod_name, phase):
    if namespace in pods:
        for item in pods[namespace]:
            if item["metadata"]["name"] == pod_name:
                item["status"]["phase"] = phase

    return ""


@custom_routes.route("/custom_routes/change_cluster_size/<new_size>", methods=["POST"])
def change_cluster_size(new_size):
    new_size = int(new_size)
    if new_size > 0:
        while len(nodes) < new_size:
            nodes.append(nodes[0])
        while len(nodes) > new_size:
            nodes.pop()

    return ""
