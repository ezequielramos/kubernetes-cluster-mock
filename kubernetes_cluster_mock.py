import json
import logging
import os

from flask import Flask
from flask import request, Response

from app.routes.basic_api_info_routes import basic_api_info_routes

# /apis/extensions/v1beta1
from app.routes.extensions.v1beta1.api_extensions_v1beta1_info import (
    api_extensions_v1beta1_info,
)
from app.routes.extensions.v1beta1.ingresses import v1beta1_ingresses
from app.routes.extensions.v1beta1.deployments import extensions_v1beta1_deployments

# /apis/networking.k8s.io/v1beta1
from app.routes.networkingk8sio.v1beta1.api_networkingk8sio_v1beta1_info import (
    api_networkingk8sio_v1beta1_info,
)

from app.routes.v1.pods import v1_pods
from app.routes.v1.nodes import v1_nodes
from app.routes.apps.v1.deployments import apps_v1_deploy
from app.routes.apps.v1.apis_apps_v1_info import apis_apps_v1_info
from app.routes.custom_routes import custom_routes

DEBUG = os.getenv("DEBUG", None)
log_level = logging.INFO if DEBUG is None else logging.DEBUG

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=log_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

app.register_blueprint(basic_api_info_routes)
app.register_blueprint(api_extensions_v1beta1_info)
app.register_blueprint(v1beta1_ingresses)
app.register_blueprint(api_networkingk8sio_v1beta1_info)
app.register_blueprint(v1_pods)
app.register_blueprint(v1_nodes)
app.register_blueprint(apps_v1_deploy)
app.register_blueprint(apis_apps_v1_info)
app.register_blueprint(extensions_v1beta1_deployments)
app.register_blueprint(custom_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9988, debug=True)
