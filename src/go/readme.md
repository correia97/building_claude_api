# Exemplos em golang utilizando a versão go1.26.1 windows/amd64

Para iniciar o projeto precisei realizar os comandos abaixo

Comando para iniciar os arquivos *go.mod* onde declara quais são as dependencias
```
go mod init
```

Comando para instalar o pacote da antropic e o que me permite utilizar o arquivo .env semelhante ao python
```
go get github.com/anthropics/anthropic-sdk-go@v1.26.0
go get github.com/joho/godotenv v1.5.1 
```
Comando para que ele preencha o arquivo *go.mod* com os pacotes que estão sendo utilizados semelhante ao *"pip freeze > requirements.txt"* do python
```
go mod tidy
```

Crie um arquivo *.env* e coloque uma variavel com a sua chave da api do Claude conforme o exemplo

```
ANTHROPIC_API_KEY="API-KEY-GERADA-NO-PAINEL-DO-CLAUDE"
```

Feita essas configurações pode ser executado cada arquivo chamando na linha de comando na raiz da pasta go
```
go run .\002_system_prompt.go
```