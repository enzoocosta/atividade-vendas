from app.models import db, User
from flask import jsonify

def list_usuarios():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])

def create_usuario(data):
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user_id": user.id}), 201

def delete_usuario(id):
    user = User.query.get(id)
    
    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Usuário deletado com sucesso!"}), 200
