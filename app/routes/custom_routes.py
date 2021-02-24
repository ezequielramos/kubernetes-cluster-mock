import logging

from flask import Blueprint

from app.resources.pods import items

logger = logging.getLogger(__name__)
custom_routes = Blueprint("custom_routes", __name__)


@custom_routes.route(
    "/custom_routes/change_pod_phase/<namespace>/<pod_name>/<phase>", methods=["POST"]
)
def change_pod_phase(namespace, pod_name, phase):
    if namespace in items:
        for item in items[namespace]:
            if item["metadata"]["name"] == pod_name:
                item["status"]["phase"] = phase

    return ""
