import json

from flask import Flask
from flask import request, Response

from app.routes.basic_api_info_routes import basic_api_info_routes

# /apis/extensions/v1beta1
from app.routes.extensions.v1beta1.api_extensions_v1beta1_info import (
    api_extensions_v1beta1_info,
)
from app.routes.extensions.v1beta1.ingresses import v1beta1_ingresses

# /apis/networking.k8s.io/v1beta1
from app.routes.networkingk8sio.v1beta1.api_networkingk8sio_v1beta1_info import (
    api_networkingk8sio_v1beta1_info,
)

from app.routes.v1.pods import v1_pods

app = Flask(__name__)

app.register_blueprint(basic_api_info_routes)
app.register_blueprint(api_extensions_v1beta1_info)
app.register_blueprint(v1beta1_ingresses)
app.register_blueprint(api_networkingk8sio_v1beta1_info)
app.register_blueprint(v1_pods)


app.run(port=9988, debug=True)
