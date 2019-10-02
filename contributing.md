# Como contribuir com esse projeto?

Primeiro, clone este repositório em sua máquina:

SSH
```bash
$ git clone git@github.com:thiagojoa/projetoacolher.git
```
HTTPS 
```bash
$ git clone https://github.com/thiagojoa/projetoacolher.git
```

## Criando virtualenv:


```bash
$ python3 -m venv venv
```
Ative seu virtualenv:

```bash
$ source venv/bin/activate
```


## Instalando dependências:


Instale os requirements.txt:

```bash
pip install -r requirements.txt
```

Criando o .env file

Para criar o arquivo de configurações do settings, basta executar o script create_eng.py

```bash
$ python contrib/create_env.py
```

## Migrações
Crie o banco de dados:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Finalmente, rode o projeto em seu ambiente local:

```bash
python manage.py runserver
```

## Licence

The source code is released under the MIT License.

