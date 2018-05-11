API FEIRASP TESTE

1. Configurar banco de dados em apiFeira/apiFeira/setting.py

2. Instalar tabela no banco.
$ python manage.py migrate

3.Inserir registro do documento feira.csv no banco.
Executar python insert.py

4.Instalar django
pip install django

5.Instalar djangorestframework
pip install djangorestframework

6.Para rodar o projeto.
python manage.py runserver
Copiar o endereço do terminal http://127.0.0.1:8000/

7.No navegador inserir endereço seguido da rota api/feira

8.Para buscar todos os registros da tabela basta vide 7

9.Para buscar um registro a mesma rota do passo 8 seguido do parametro
exemplos 
http://127.0.0.1:8000/api/feira/AMERICANOPOLIS
http://127.0.0.1:8000/api/feira/LAJEADO


