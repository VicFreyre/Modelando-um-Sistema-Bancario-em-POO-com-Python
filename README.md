# Modelando-um-Sistema-Bancario-em-POO-com-Python
Desafio de Código DIO - Suzano Python Bootcamp.

Este projeto é um sistema bancário simples, implementado em Python, utilizando Programação Orientada a Objetos (POO). O sistema permite a criação de clientes, contas bancárias, depósitos, saques e visualização de extratos.

## Funcionalidades

- **Criação de clientes**: Permite cadastrar um cliente com nome, data de nascimento, CPF e endereço.
- **Criação de contas bancárias**: Para cada cliente, uma conta bancária pode ser criada.
- **Depósitos**: É possível depositar valores nas contas.
- **Saques**: Os clientes podem sacar valores, respeitando um limite diário de saques.
- **Extrato**: O sistema mantém um extrato das movimentações realizadas em cada conta.
- **Listagem de contas**: Exibe uma lista com as contas criadas no sistema.

## Estrutura do Projeto

O projeto é modularizado em três partes principais, cada uma responsável por um aspecto do sistema:

1. **cliente.py**: Define a classe `Cliente`, que armazena informações dos clientes.
2. **conta_bancaria.py**: Define a classe `ContaBancaria`, que lida com operações de depósito, saque e extrato.
3. **banco.py**: Define a classe `Banco`, que gerencia os clientes e suas contas.



