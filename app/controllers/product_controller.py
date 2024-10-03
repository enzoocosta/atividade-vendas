from app.models import db, Product
from flask import jsonify

def list_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "stock": p.stock, "price": str(p.price)} for p in products])

def create_product(data):
    name = data.get('name')
    stock = data.get('stock')
    price = data.get('price')

    if not name or stock is None or price is None:
        return jsonify({"message": "Nome, estoque e preço são obrigatórios."}), 400

    product = Product(name=name, stock=stock, price=price)
    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Produto criado com sucesso!", "product_id": product.id}), 201

def delete_product(id):
    product = Product.query.get(id)
    
    if not product:
        return jsonify({"message": "Produto não encontrado."}), 404
    
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Produto deletado com sucesso!"}), 200
