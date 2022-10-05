## Django:
- framework web fullstack que permite a criação de websites usando somente python e um pouco de html

#

## Parte 1: Instalação e Navegação
```shell
$ pip install django
$ cd (diretorio que quer instalar as dependências do django) 
$ django-admin startproject (nome do projeto)
$ cd (diretorio onde está o arquivo manage.py)
$ python manage.py runserver (porta que quer rodar o servidor  - não obrigatório)
$ python manage.py startapp (nome do aplicativo que quer criar)
```

- manage.py: responsável por criar aplicações, rodar servidores etc.
- /main: aplicação que será vinculada com o projeto
- main/views.py :como se um website, é onde se escreve os códigos que farão as requisições http que mostrarão coisas na nossa página
- main/urls.py: representa as URLs que vão para as diferentes views criadas no arquivo views.py

### Resumo:
- criação de uma view (resposta http que será exibida no website)
- especificar no arquivo main/urls.py qual caminho será o responsável por mostrar determinada view
- especificar no arquivo urls.py o url pattern de determinado nome, que mostrará a view

#

## Parte 2: Ligação com banco de dados SQLite3
- especificar no arquivo settings.py a aplicação que estamos trabalhando
```shell
$ python manage.py migrate
$ python manage.py makemigrations (nome da aplicação) | coloca os arquivos que foram modificados na "staging area"
$ python manage.py migrate
$ python manage.py shell | abre o shell para adicionar algumas coisas ao banco de dados
```

- migrations: maneira de aplicar as mudanças realizadas no arquivo "models.py" ao banco de dados
#
```shell

>> from main.models import Item, ToDoList (item(ns) que quer importar do arquivo main/models)
>> t = ToDoList(name="nome que quer colocar no objeto que será adicionado ao banco de dados")
>> t.save() | salva o objeto no banco de dados
>> ToDoList.objects.all() | mostra os objetos que estão cadastrados no banco de dados
>> ToDoList.objects.get(atributo que quer acessar=valor que quer acessar)
```

#

## Parte 3: Admin Dashboard
```shell
$ python manage.py shell
$ from main.models import ToDoList, Item
$ t = ToDoList.objects
$ t.filter(name__startswith='substring') | filtra um objeto que começa com uma determinada substring
$ t.filter(name__endswith='substring') | filtra um objeto que termina com uma determinada substring
$ delete_object = t.get(name='string') | pega o objeto que será deletado
$ delete_object.delete()
```

- filter X get: caso não haja nenhum resultado em uma query utilizando o método get, será retornado um erro. No filter, será retornado um QuerySet vazio.


```shell
$ python manage.py createsuperuser | cria uma conta de admin na página de dashboard do django
```

- necessário cadastrar o banco de dados no arquivo main/admin.py para ele ser mostrado no dashboard

#

## Parte 4: Templates & Custom HTML
- deixa o html bonito e mostra-o no website
- criar templates/main/ dentro da pasta da aplicação
- herança de templates: permite a construção de um template "básico", que possui elementos comuns que serão exibidos em toda página
- bloco: permite a substituição de partes específicas de um template

#

## Parte 5: Formulários Simples
- criar objeto form em templates/main/, que gerará o html automaticamente na página de acordo com os atributos da classe
- layouts padrões para forms (.as_table, .as_div, .as_ul, .as_p)
- necessário criar um {% csrf_token %} para cada formulário
- tratar as requisições get e posts nas views por meio do parâmetro response
- render(request object, template, dictionary) → HttpResponse
- .is_valid → checa automaticamente se os inputs definidos têm informações válidas
- .cleaned_data → possibilita acessar os atributos a partir da descriptografia dos dados da requisição post
- HttpResponseRedirect → redireciona o usuário para outra página 

#

## Parte 9: User Registration & Sign Up Page
- criar nova aplicação no projeto que será responsável pelas páginas de usuário
- importante: não se esquecer de adicionar a nova aplicação no arquivo settings.py
```python
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# formulário de criação de usuário já prontos
```

- para adicionar outros inputs no formulário já pronto, cria-se uma classe que herda de UserCreationForm
- classe Meta: permite a modificação de alguns atributos da classe mãe
```python
model = User
fields = ["username", "email", "password1", "password2"] # especifica a ordem dos inputs na página
```

- crispy forms: aplicação que ajuda a manipular os formulários django

#

## Parte 10: Login, logout e autenticação de usuário 

- 'django.contrib.auth': aplicação que consegue autenticar usuários
- definir LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL para a página que desejar

#

## Parte 11: Páginas específicas de usuário

- em caso de problemas com as migrations, excluir todos os arquivos das pastas migrations exceto o "init.py"