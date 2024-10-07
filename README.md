deletar usuario
curl -X DELETE http://127.0.0.1:5001/usuario/1
----------------------------------------------
CRIAR PRODUTO: 
curl -X POST http://127.0.0.1:5001/produto -H "Content-Type: application/json" -d "{\"name\": \"controle\", \"stock\": 40, \"price\": 9.99}"
----------------------------------------------
COMPRAR PRODUTO: 
curl -X POST http://127.0.0.1:5001/sale -H "Content-Type: application/json" -d "{\"user_id\": 1, \"product_id\": 1, \"quantity\": 2}"
---------------------------------------------
CRIAR USUARIO:
curl -X POST http://localhost:5001/usuario -H "Content-Type: application/json" -d "{\"username\": \"PONTO FRIO\"}"

GRUPO:
ENZO LACERDA COSTA
RODRIGO COUTRUFO SILVA
RAUL GUILHERME SILVA RODRIGUES
