# API_Django Rest framework
API básica para firmar conhecimentos em django restframework
Relização de um CRUD para pedidos de oração. Utilizei @api_view para as criações de endpoints.

Aqui está o README melhorado com mais clareza, organização e algumas explicações adicionais:  

---

# 🚀 Iniciando com Django  

Este guia fornece um passo a passo para iniciar um projeto CRUD utilizando **Django**, um dos frameworks mais populares para desenvolvimento web com Python.  

## 📌 Pré-requisitos  
- **Python** instalado (versão 3.8 ou superior recomendada)  
- **Pip** (gerenciador de pacotes do Python) atualizado  
- **Virtual Environment** para isolar o projeto  

---

## 🔹 1. Criar e ativar um ambiente virtual  

Criar o ambiente virtual:  
```bash
python -m venv env
```  

Ativar o ambiente virtual:  
- **Windows:**  
  ```bash
  .\env\Scripts\activate
  ```  
- **Linux/macOS:**  
  ```bash
  source env/bin/activate
  ```  

---

## 🔹 2. Instalar o Django  

Instale a versão mais recente do Django com:  
```bash
pip install django
```  

Verifique se a instalação foi bem-sucedida:  
```bash
django-admin --version
```  

---

## 🔹 3. Criar um novo projeto Django  

Crie o projeto principal chamado `project`:  
```bash
django-admin startproject project
```  

Entre no diretório do projeto:  
```bash
cd project
```  

---

## 🔹 4. Rodar o servidor Django  

Para verificar se o Django está funcionando corretamente, execute:  
```bash
python manage.py runserver
```  
Acesse no navegador: **http://127.0.0.1:8000/**  

> ⚠️ Para interromper o servidor, pressione `CTRL + C`.  

---

## 🔹 5. Criar um aplicativo dentro do projeto  

Django organiza funcionalidades em **apps**. Vamos criar um app chamado `app`:  
```bash
python manage.py startapp app
```  

> 📌 Substitua `app` pelo nome do seu app, caso deseje um diferente.  

Agora, adicione o app ao projeto:  
1. Abra o arquivo `settings.py` dentro da pasta `project`.  
2. No bloco `INSTALLED_APPS`, adicione a nova aplicação:  

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Nome do seu app
]
```

---

## 🔹 6. Aplicar as migrações do banco de dados  

Django usa um ORM para gerenciar o banco de dados. Para criar as tabelas iniciais, execute:  
```bash
python manage.py migrate
```  

---

## 🔹 7. Criar um superusuário para acessar o Django Admin  

Para acessar o painel de administração do Django, crie um superusuário:  
```bash
python manage.py createsuperuser
```  
Preencha os dados solicitados (nome, e-mail, senha) e pronto!  

Agora, rode novamente o servidor e acesse **http://127.0.0.1:8000/admin/** para fazer login no painel administrativo.  

---




## 🔹 8. Instalando o django rest framework  

Para acessar o painel de administração do Django, crie um superusuário:  
```bash
pip install djangorestframework
```  

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Nome do seu app
    'rest_framework',
]
```


---


### Caso der erro de execução de scripts foi desabilitada no sistema

Você pode controlar estas permissões usando o cmdlet Set-ExecutionPolicy. E pode conferir qual a política de execução atual usando o cmdlet Get-ExecutionPolicy.
