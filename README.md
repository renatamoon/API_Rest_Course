# API_Rest_Course

<i>CURSO DE API REST Framework - DJANGO</i><br>

<hr>
<p align="center">
  <a href="#curso">Sobre o curso</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  
  <a href="#imagens">Algumas Imagens</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#links_apps">Links Úteis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>
<hr>

## <a id="curso"> 💻 SOBRE O CURSO </a><br>

Aprendi sobre:

-Funcionamento e implementação de uma API REST utilizando o Django e o Django REST Framework.<br>
-Funciomaneot dos serializers, paginação e autenticação no Django REST Framework. <br>
-Construção de uma API com relacionamento NN entre as entidades Tecnologia e Vagas, para que vagas de emprego fossem cadastradas utilizando o serviço da API.<br>

> 🟩 Status do curso: FINALIZADO EM 30/11/2021<br>
<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS UTILIZADAS </a>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Django-Rest](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![POSTMAN](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)

-Desenvolvimento em:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows:

<b>-Clone o repositório com o camando:</b> `https://github.com/renatamoon/API_Rest_Course.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'desafio_2',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```

-Migre o banco de dados com: `python manage.py migrate` <br>
-Execute o servidor: `python manage.py runserver` <br>
  
<hr>

## <a id="imagens"> 🔴 IMAGENS: </a> 

Dados da API REST:<br>
<i>Usando o POSTMAN para requisição de dados da API em formato JSON.</i>
<br>
<br>
-Cadastrando vaga na API via POSTMAN:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/144066036-5ad99035-4d63-4840-8ab0-e3ccd582e7f4.png)
<br>
<br>
-Cadastrando uma tecnologia:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/144066413-c4e89c9b-5413-47bb-8558-b6ff1cd71e4a.png)
<br>
<br>
-Cadastro de usuário da API, já retorna o Password como código tolken para acesso da API:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/144066523-8cae94b9-e548-4194-bf29-b53c35d7e49c.png)
<br>
<br>
-Temos que criar um super usuario atraves do comando ```python manage.py createsuperuser```, entrar na área de Admin do Django, criar uma aplicação onde será gerado
  um ```clientid``` e ```clientsecret```:
<br>
<br>   
![image](https://user-images.githubusercontent.com/87100340/144073646-177457c9-5fcd-46ee-86ac-a0d1b12ad9e5.png) 
<br>
<br> 
-Com isso, passaremos as informações dentro do POSTMAN para acesso da API.
 <br>
<br>
![image](https://user-images.githubusercontent.com/87100340/144066767-17d64c37-6964-47ae-8f60-3a0223978383.png)
<br>
<br>
-Faz o input do Authorization e Content Type, teremos acesso aos dados publicos da API:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/144066915-4663c5d7-9de6-4162-aa6b-269f49a2925c.png)
<br>

<hr>
  
## <a id="links_apps"> 🔴 LINKS ÚTEIS </a> 

*USANDO MYSQL WORKBENCH PARA EXPORTAÇÃO DOS DADOS EM XML:
<br>
<br>
-Documentação da API Rest: https://www.django-rest-framework.org/ - documentação completa do Django API Rest Framework<br>
-Paginação do REST Framework: https://www.django-rest-framework.org/api-guide/pagination/<br>
-POSTMAN – para teste de API – ferramenta que permite fazer requisições para a API que criamos e retorna as respostas.<br>
