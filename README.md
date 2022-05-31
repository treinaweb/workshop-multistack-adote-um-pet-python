## Projeto API Adote um Pet

Desenvolvido no curso multi-stack da treinaweb

### Instalando o projeto

#### Clonar o repositório

```
git clone https://github.com/treinaweb/workshop-multistack-adote-um-pet-php.git
```

#### Criar e ativar ambiente virtual

```
python3 -m venv .venv
source .venv/bin/activate
```

#### Instalar as depencências

```
pip install -r requirements.txt
```

#### Criar a estrutura no banco de dados

```
python manage.py migrate
```

#### Iniciar o servidor de desenvolvimento

```
python manage.py runserver
```
