# Exemplos em python utilizando a versão 3.12.10

Para executar o projeto primeiro recomendo que seja criado um ambiente virtual do python com o comando abaixo

```
python -m venv .venv
```

Após criar o ambiente ele geralmente é ativado automaticamente, mas caso de algum erro e para quando precisar sair e volvar pode ser utilizado o comando abaixo

```
.\venv\Scripts\activate
```

Agora precisa instalar os pacotes utilizados nos exemplos e descritos no arquivo *requirements.txt*

```
pip install
```
Crie um arquivo *.env* e coloque uma variavel com a sua chave da api do Claude conforme o exemplo

```
ANTHROPIC_API_KEY="API-KEY-GERADA-NO-PAINEL-DO-CLAUDE"
```

Feita essas configurações pode ser executado cada arquivo chamando na linha de comando 
```
python .\src\python\002_system_prompt.py
```

Para gerar ou atualizar o arquivo *requirements.txt*

```
pip freeze > requirements.txt
```