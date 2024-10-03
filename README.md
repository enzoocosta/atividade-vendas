criar usuario 
curl -X POST http://localhost:5001/usuario -H "Content-Type: application/json" -d "{\"username\": \"Americanas\"}"

deletar usuario

curl -X DELETE http://127.0.0.1:5001/usuario/1

criar produto
curl -X POST http://127.0.0.1:5001/produto -H "Content-Type: application/json" -d "{\"name\": \"Produto A\", \"stock\": 10, \"price\": 19.99}"

comprar produto
curl -X POST http://127.0.0.1:5001/sale -H "Content-Type: application/json" -d "{\"user_id\": 1, \"product_id\": 1, \"quantity\": 2}"
