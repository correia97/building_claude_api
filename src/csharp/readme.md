# Exemplos em c# utilizando a versão .net 10
Para iniciar o projeto precisei realizar os comandos abaixo

Comando para criar um projeto console em c#
```
dotnet new console
```

Comando para instalar o pacote da antropic 
```
dotnet add package Anthropic --version 12.8.0
```
Comando no powershell para registrar a variavel da chave de API
```
$env:ANTHROPIC_API_KEY = "API-KEY-GERADA-NO-PAINEL-DO-CLAUDE"
```


Feita essas configurações pode ser executado 
*Obs.: No arquivo Program.cs eu informo qual o exercicios quero rodar e deixo os demais comentados*
```
dotnet run
```