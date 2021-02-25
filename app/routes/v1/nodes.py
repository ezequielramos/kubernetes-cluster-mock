import logging
import json

from flask import Blueprint, request, Response

from app.resources.nodes import items

logger = logging.getLogger(__name__)
v1_nodes = Blueprint("v1_nodes", __name__)


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
