# Shape data challenge
### Necesário para rodar
Para executar o projeto é necessário possuir o docker e docker-compose

Link para instalação:
* Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* Docker-compose: https://docs.docker.com/compose/install/

### Necesário para popular o DB
Para popular o DB é necessário o psycopg2 e o pandas
 * Comando para instalação: pip3 install pandas psycopg2
 
### Rodando o projeto
O docker monta o projeto e DB.

* Comando para rodar: docker-compose up

Assim que tudo for executado o projeto estará rodando e o banco criado

Depois disso na primeira vez é preciso popular o banco.
Na pasta scripts tem um script que popula o banco.
* Comando para rodar o script: python3 insert_data.py

### Executando o endpoint
Para executar os endpoints é possivel utilizar a documentação do swagger.
Para isso com o projeto rodando acesse: http://localhost:5000/apidocs/
