from app.models import db, Sale, Product
from flask import jsonify

def list_sales():
    sales = Sale.query.all()
    return jsonify([{"id": s.id, "user_id": s.user_id, "product_id": s.product_id, "quantity": s.quantity, "price": str(s.price)} for s in sales])

def create_sale(data):
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Verificar se o produto existe
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produto não encontrado."}), 404

    # Verificar se há estoque suficiente
    if product.stock < quantity:
        return jsonify({"message": "Estoque insuficiente."}), 400

    # Calcular o preço total da venda
    sale_price = product.price * quantity
    sale = Sale(user_id=user_id, product_id=product_id, quantity=quantity, price=sale_price)
    db.session.add(sale)

    # Atualizar o estoque do produto
    product.stock -= quantity
    db.session.commit()

    return jsonify({"message": "Venda realizada com sucesso!", "sale_id": sale.id}), 201
