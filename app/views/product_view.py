from flask import Blueprint, request
from app.controllers.product_controller import list_products, create_product, delete_product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/produto', methods=['GET'])
def get_products():
    return list_products()

@product_bp.route('/produto', methods=['POST'])
def add_product():
    return create_product(request.json)

@product_bp.route('/produto/<int:id>', methods=['DELETE'])
def remove_product(id):
    return delete_product(id)
