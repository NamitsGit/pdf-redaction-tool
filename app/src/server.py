import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
# Import flask and template operators
from flask import Flask, render_template, request, Response
from flask_restplus import Api

# from .route.ping.controller import api



# Define the WSGI application object
app = Flask(import_name="ExtractData",
            template_folder='src/templates',
            static_folder='src/static')

api = Api(app,
        version='1.0',
        title='PDF Redactor',
        description='',
        license='Perfios',
        prefix='/pdfredactor')

from .route.redact.controller import api as redact
api.add_namespace(redact)