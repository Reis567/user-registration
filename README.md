# User Registration Application

Portuguese version at the end

This is a simple user registration application developed in Python using the Tkinter library. It provides a graphical interface where users can enter their name, last name, email, and password to register in the system.

## Requirements

Make sure you have Python installed on your machine. Additionally, the code uses the Tkinter library, which is a standard Python library for creating graphical interfaces. Therefore, there is no need to install anything additional.

## Features

- The application displays a login window with fields for name, last name, email, and password.
- Fields marked with an asterisk (*) are mandatory.
- When clicking the "Create Account" button, the application performs several checks on the entered data:
  - It checks if the email is already registered in the database.
  - It checks if all mandatory fields have been filled.
  - It checks if the name and last name contain only letters.
  - It checks if the email is in a valid format.
  - It checks if the password and password confirmation are the same.
- If all checks are successful, the data is inserted into the database, and a success message is displayed. The login screen is reset to allow the registration of a new user.

## Database

The application uses an SQLite database to store user data. The database file is `cadastro_usuarios.db`. The `usuarios` table is created with columns for `Name`, `Last Name`, `Email`, and `Password`. In the provided code, the table creation is commented out. If it is the first execution of the application, uncomment that line and run the code once to create the table.


## Developed by Reis567


##

### Português

##

# Aplicativo de Cadastro de Usuários

Este é um aplicativo simples de cadastro de usuários desenvolvido em Python usando a biblioteca Tkinter. Ele fornece uma interface gráfica onde os usuários podem inserir seu nome, sobrenome, email e senha para se cadastrar no sistema.

## Requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, o código usa a biblioteca Tkinter, que é uma biblioteca padrão do Python para criar interfaces gráficas. Portanto, não há necessidade de instalar nada adicional.


## Funcionalidades

- O aplicativo exibe uma janela de login com campos para nome, sobrenome, email e senha.

- Os campos marcados com asterisco (*) são obrigatórios.

- Ao clicar no botão "Criar cadastro", o aplicativo realiza algumas verificações nos dados inseridos:
    - Verifica se o email já está cadastrado no banco de dados.
    - Verifica se todos os campos obrigatórios foram preenchidos.
    - Verifica se o nome e sobrenome contêm apenas letras.
    - Verifica se o email está em um formato válido.
    - Verifica se a senha e a confirmação de senha são iguais.

- Se todas as verificações forem bem-sucedidas, os dados são inseridos no banco de dados e uma mensagem de sucesso é exibida. A tela de login é redefinida para permitir o cadastro de um novo usuário.

## Banco de Dados

O aplicativo utiliza um banco de dados SQLite para armazenar os dados dos usuários. O arquivo do banco de dados é `cadastro_usuarios.db`. A tabela `usuarios` é criada com as colunas `Nome`, `Sobrenome`, `Email` e `Senha`. No código fornecido, a criação da tabela está comentada. Se for a primeira execução do aplicativo, descomente essa linha e execute o código uma vez para criar a tabela.

##  Desenvolvido por Reis567
