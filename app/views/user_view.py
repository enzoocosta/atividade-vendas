from flask import Blueprint, request
from app.controllers.user_controller import list_usuarios, create_usuario, delete_usuario

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    return list_usuarios()

@user_bp.route('/usuario', methods=['POST'])
def add_usuario():
    return create_usuario(request.json)

@user_bp.route('/usuario/<int:id>', methods=['DELETE'])
def remove_usuario(id):
    return delete_usuario(id)
