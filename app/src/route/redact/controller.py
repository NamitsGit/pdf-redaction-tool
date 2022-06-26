import fitz
import re
import os
from flask_restplus import Namespace, Resource, fields
from flask import Flask, render_template, request, Response
from ...components.redactor.redact import Redactor
import time

directory = "output"
parent_dir = os.getcwd()
p = os.path.join(parent_dir, directory) 
try:
    os.makedirs(p, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)

api = Namespace('redact', description='description')
a_input = api.model('Inputs', {'filepath' : fields.String('/home/namit/Desktop/LargeApp/app/tests/1.pdf'),"datafields":fields.String('["acc_no","ifsc_code","email","card_no","pan_no","phone_no","acc_tag","acc_dash","city_tag","pin_tag","branch_tag"]'),"black_bar":fields.Boolean(True)}) #, 'id' : fields.Integer('ID')


@api.route('/')
class Ping(Resource):
    @api.doc(responses={200: 'OK'})
    @api.expect(a_input)
    def post(self):
        output = request.get_json()
        path=output["filepath"]
        data_list=output["datafields"]
        black_bar = output["black_bar"]
 #       data_list = json.dumps(output["datafields"])
        start_time = time.time()
        redactor = Redactor(path,data_list)
        redactor.redaction(data_list,black_bar)
        end_time = time.time()
        return {'result' : p,'time' : (end_time-start_time)}, 201 

