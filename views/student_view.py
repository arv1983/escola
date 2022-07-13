from flask import request, jsonify, Blueprint
from config.db import db
from services.mask import Masks
from services.validator import Validator
from models.student_model import StudentModel
from datetime import datetime

bp = Blueprint("student_route", __name__)

@bp.route("/", methods=["GET", "POST"])
def get_all_or_create():

    if request.method == "POST":
        data = request.get_json()
        
        validator_response = Validator.register_validator(data)
        
        if validator_response:
            return jsonify(validator_response)

        if not Validator.check_if_email_is_valid(str(data['email'])):
            return {'erro': 'Email inválido.'},409

        if not Validator.check_cpf_is_true(str(data['cpf'])):
            return {'erro': 'CPF inválido'},409
         
        if StudentModel.get_student_by_cpf(Masks.cpf_clean(data['cpf'])):
            return {'erro': 'Estudante já cadastrado'},401
        
        if not Validator.check_phone_11_digits(str(data['phone_number'])):
            return {'erro': 'Telefone de conter 11 dígitos'},409

        if not Validator.check_phone_only_numbers(str(data['phone_number'])):
            return {'erro': 'Telefone de conter somente números'},409


        data['cpf'] = str(Masks.cpf_clean(data['cpf']))

        data['created_at'] = datetime.now()

        data_serialized = StudentModel(**data)
        db.session.add(data_serialized)
        db.session.commit()

        return jsonify(StudentModel.serialized(data_serialized)),201

    if request.method == "GET":

        return jsonify(StudentModel.get_all_students()),200


@bp.route("/id/<int:id>", methods=["GET", "DELETE", "PATCH"])
def get_id(id):

    query = StudentModel.get_student_by_id(str(id))

    if not query:
        return '',404

    if request.method == "GET":
        
        return jsonify(StudentModel.serialized(query)),200

    if request.method == "PATCH":

        data = request.get_json()
        
        data['created_at'] = query.created_at
        data['cpf'] = query.cpf
        
        for key, value in data.items():
            setattr(query, key, value)
        
        db.session.add(query)
        db.session.commit()

        return jsonify(StudentModel.serialized(query)),200

    if request.method == "DELETE":

        db.session.delete(query)
        db.session.commit()

        return '',200

@bp.route("/student", methods=["GET"])
def search():

    data = request.get_json(silent=True) or {}
    
    validator_response = Validator.search_validator(data)
    
    if validator_response:
        return jsonify(validator_response)
                
    return jsonify(StudentModel.search_student_by_name(data['name'])),200