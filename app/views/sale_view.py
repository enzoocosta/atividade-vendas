from flask import Blueprint, request
from app.controllers.sale_controller import list_sales, create_sale

# Definindo o Blueprint para as rotas de vendas
sale_bp = Blueprint('sale_bp', __name__)

# Rota para listar todas as vendas
@sale_bp.route('/sales', methods=['GET'])
def get_sales():
    return list_sales()

# Rota para criar uma nova venda
@sale_bp.route('/sale', methods=['POST'])
def add_sale():
    return create_sale(request.json)
