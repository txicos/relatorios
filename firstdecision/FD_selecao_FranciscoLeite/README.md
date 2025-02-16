# Instalação

OBS: Testado usando python3.11


 1. criar um ambiente virtual com: `python3 -m venv first-env`
 2. ativar o ambiente virtual: `source first-env/bin/activate`
 3. instalar os pacotes python: `pip install -r requirements.txt`
 4. instalar o [docker](https://docs.docker.com/desktop/) se não estiver disponível na máquina.

# Exercício 1:

Baixar arquivo com `wget https://raw.githubusercontent.com/datasets/finance-
vix/main/data/vix-daily.csv`

Executar `python3 -i finance.py` para iteragir com o script. As informações 
solicitadas (items de 1-9 do exercício) aparecerão na tela e os arquivos 
armazenados no diretório corrente.

# Exercício 2:

Baixar arquivo com `wget https://makeup-api.herokuapp.com/api/v1/products.json`

Executar `python3 -i product.py` para iteragir com o script. As informações 
solicitadas (items de 1-6 do exercício) aparecerão na tela e os arquivos 
armazenados no diretório corrente.


# Exercício 3:

Execute o comando `docker network create decision` e `docker compose build`
para criar o container da API e do banco.

Execute o comando `docker compose up` que disponibilizará um banco mongo para 
os outros itens deste exercício. Após subir o banco executar.

3.1 Executar `python3 -i storedb.py` para dar um carga no banco.

3.2 Executar `python3 -i readdb.py` para carregar o dataframe a partir do banco.

OBS: não foi colocado mecanismo para evitar dupla inserão. Assim, sugere-se
deletar a tabela tb_produto caso se execute 3.1 novamente.

# Exercício 4:

Ao Executar o comando `docker compose up` uma API também será disponibilizada.
Pode-se usar o comando curl -X 'GET'   'http://127.0.0.1:8080/prod'   -H 'accept: application/json'` para baixar os dados 


# Exercício 5:

Execute o comando `streamlit run gui.py` que disponbilizará uma interface web 
(http://localhost:8501) para ver o dataframe como tabela