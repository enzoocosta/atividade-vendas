from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos para usuários, produtos e vendas
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

# Rotas para usuários
@app.route('/usuarios', methods=['GET'])
def list_usuarios():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

@app.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user_id": user.id}), 201

# Rota para deletar usuários
@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    user = User.query.get(id)
    
    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Usuário deletado com sucesso!"}), 200

# Rotas para produtos
@app.route('/produto', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        stock = data.get('stock')
        price = data.get('price')

        if not name or stock is None or price is None:
            return jsonify({"message": "Nome, estoque e preço são obrigatórios."}), 400

        product = Product(name=name, stock=stock, price=price)
        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Produto criado com sucesso!", "product_id": product.id}), 201
    else:
        products = Product.query.all()
        return jsonify([{"id": p.id, "name": p.name, "stock": p.stock, "price": str(p.price)} for p in products]), 200

# Rotas para vendas
@app.route('/sale', methods=['GET', 'POST'])
def sale():
    if request.method == 'POST':
        data = request.json
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
    else:
        sales = Sale.query.all()
        return jsonify([{"id": s.id, "user_id": s.user_id, "product_id": s.product_id, "quantity": s.quantity, "price": str(s.price)} for s in sales]), 200

# Rota para deletar produtos
@app.route('/produto/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    
    if not product:
        return jsonify({"message": "Produto não encontrado."}), 404
    
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Produto deletado com sucesso!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True, port=5001)
