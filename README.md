[![Build Status](https://gladsonbruno16.visualstudio.com/Portfolio_DevOps/_apis/build/status/Python-AzureDevOps-CI-Example?repoName=GladsonBruno%2FPython-AzureDevOps-CI-Example&branchName=master)](https://gladsonbruno16.visualstudio.com/Portfolio_DevOps/_build/latest?definitionId=9&repoName=GladsonBruno%2FPython-AzureDevOps-CI-Example&branchName=master)

# Visão Geral
Projeto de exemplo criado apenas para fins de exemplificação de automação DevOps com Azure DevOps.

Estará contemplado:

* Scan SonarCloud
* Teste unitário
* Code Coverage
* Build de container
* Teste de container
* Pipeline templatizada

# Executando a aplicação
## Configurando o VirtualEnv

Isso é importante para que as dependências sejam instaladas apenas localmente, não no seu sistema como um todo
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Para isso instale o virtualEnv com este comando:
```
python -m pip install --user virtualenv
```

em seguida crie o virtual env com o seguinte comando:
```
python -m venv env
```

Agora basta ativar o virtualEnv

Windows
```sh
.\env\Scripts\activate
```

Após instalar o virtualenv e ativar o environment, vamos instalar as dependências

--- 

## Instalando as dependências

```sh
pip install -r requirements.txt
```

## Executando a aplicação

Para executar a aplicação, basta executar o seguinte comando:

```sh
python -m app.app
```


## Geração de Cobertura de testes

Para executar os testes da applicação gerando arquivos de cobertura de testes tanto para o azure quanto para a pipeline execute o seguinte comando:

```sh
pytest --cov=app --cov-report=xml --cov-report=html --nunitxml=reports/nunit/test-output.xml --junitxml=reports/junit/test-output.xml
```

## Execução em produção

É necessário primeiro criar o virtual env, acessá-lo  e instalar as dependências previamente conforme o exemplo abaixo:

```sh
python -m pip install --user virtualenv
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

Após isso ara executar a aplicação em produção basta executar o seguinte comando:

```sh
waitress-serve --call "app:app.create_app"
```

https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/#run-with-a-production-server