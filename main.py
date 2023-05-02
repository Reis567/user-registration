from tkinter import *
from tkinter import Tk , ttk, messagebox
from variaveis import co0 , co1 , co2 , co3 , co4
import re
import sqlite3

db_cadastro = sqlite3.connect('cadastro_usuarios.db')
cursor = db_cadastro.cursor()
#cursor.execute("CREATE TABLE usuarios (Nome text, Sobrenome text, Email text , Senha text)")


#Janela criada
janela = Tk()

janela.title("Login")
janela.geometry('310x550')
janela.configure(background=co1)
janela.resizable(width=False, height=False)


#First frame
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0 , pady=1, padx=0, sticky=NSEW)

#Second frame
frame_baixo = Frame(janela, width=310, height=500, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0 , pady=1, padx=0, sticky=NSEW)


#Frames Configuration

##Cabeçalho
label_nome = Label(frame_cima, text='Cadastre - se', anchor=NE , font=('BEAR 25'), bg=co1, fg=co4)
label_nome.place(x=5, y=5)

label_linha = Label(frame_cima, text='',width=275, anchor=NW , font=('Ivy 1'), bg=co2, fg=co4)
label_linha.place(x=5, y=45)



##Corpo da tela
label_nome = Label(frame_baixo, text='Nome *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_nome.place(x=10, y=20)

entry_nome = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
entry_nome.place(x=14, y=50)

label_last_name = Label(frame_baixo, text='Sobrenome *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_last_name.place(x=10, y=100)

entry_last_name = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
entry_last_name.place(x=14, y=130)

label_email = Label(frame_baixo, text='Email *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_email.place(x=10, y=180)

entry_email = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
entry_email.place(x=14, y=210)

label_pass = Label(frame_baixo, text='Senha *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_pass.place(x=10, y=260)

entry_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('',15), highlightthickness=1, relief='solid')
entry_pass.place(x=14, y=290)

label_pass_confirm = Label(frame_baixo, text='Confirme sua Senha *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
label_pass_confirm.place(x=10, y=340)

entry_pass_confirm = Entry(frame_baixo, width=25, justify='left',show='*', font=('',15), highlightthickness=1, relief='solid')
entry_pass_confirm.place(x=14, y=370)

def verificar_email(email):
    cursor.execute("SELECT * FROM usuarios WHERE Email=?", (email,))
    resultado = cursor.fetchone()
    if resultado is not None:
        return True
    else:
        return False

def verificar_dados(dados_corretos):
    nome = entry_nome.get()
    sobrenome = entry_last_name.get()
    email = entry_email.get()
    senha = entry_pass.get()
    confirm_senha = entry_pass_confirm.get()

    dados_corretos=True

    ### Verificar se o email já está cadastrado
    if verificar_email(email):
        messagebox.showerror('Erro', 'Este email já está cadastrado')
        return dados_corretos==False
    
    ### Verificações de campo vazio
    if nome == "":
        messagebox.showerror('Erro', 'Preencha o seu nome')
        return dados_corretos==False
    

    if sobrenome == "":
        messagebox.showerror('Erro', 'Preencha o seu sobrenome')
        return dados_corretos==False
    

    if email == "":
        messagebox.showerror('Erro', 'Preencha o seu email')
        return dados_corretos==False



    if senha == "":
        messagebox.showerror('Erro', 'Preencha a sua senha')
        return dados_corretos==False
    

    if confirm_senha == "":
        messagebox.showerror('Erro', 'Preencha a sua confirmação de senha')
        return dados_corretos==False
    

    ### Retira espaços do sobrenome e nome
    nome_sem_espaço = sobrenome.replace(' ', '')
    sobrenome_sem_espaço = sobrenome.replace(' ', '')


    ###Verificações de "somente letras" em nome e sobrenome
    if nome_sem_espaço.isalpha():
        print('Verificação de nome concluida')
    else:
        messagebox.showerror('Erro', 'Preencha o seu nome apenas com letras')
        return dados_corretos==False
    

    if sobrenome_sem_espaço.isalpha():
        print('Verificação de sobrenome concluida')
    else:
        messagebox.showerror('Erro', 'Preencha o seu sobrenome apenas com letras')
        return dados_corretos==False
    
    

    ### verificações de padrao de email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Verifica se o email inserido corresponde ao padrão regex
    if re.match(email_pattern, email):
        # Se sim, continua o processo aqui
        print("Verificação de email concluida")
    else:
        # Se não, exibe uma mensagem de erro
        messagebox.showerror('Erro', 'Preencha o seu email corretamente')
        return dados_corretos==False
    

    if senha == confirm_senha:
        print('Senhas são idênticas')
    else:
        messagebox.showerror('Erro', 'As senhas não coincidem. Por favor, verifique e tente novamente.')
        return dados_corretos==False
    
    return dados_corretos

def tela_nova():
    label_nome = Label(frame_cima, text='Cadastre - se', anchor=NE , font=('BEAR 25'), bg=co1, fg=co4)
    label_nome.place(x=5, y=5)

    label_linha = Label(frame_cima, text='',width=275, anchor=NW , font=('Ivy 1'), bg=co2, fg=co4)
    label_linha.place(x=5, y=45)



    ##Corpo da tela
    label_nome = Label(frame_baixo, text='Nome *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
    label_nome.place(x=10, y=20)

    entry_nome = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
    entry_nome.place(x=14, y=50)

    label_last_name = Label(frame_baixo, text='Sobrenome *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
    label_last_name.place(x=10, y=100)

    entry_last_name = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
    entry_last_name.place(x=14, y=130)

    label_email = Label(frame_baixo, text='Email *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
    label_email.place(x=10, y=180)

    entry_email = Entry(frame_baixo, width=25, justify='left', font=('',15), highlightthickness=1, relief='solid')
    entry_email.place(x=14, y=210)

    label_pass = Label(frame_baixo, text='Senha *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
    label_pass.place(x=10, y=260)

    entry_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('',15), highlightthickness=1, relief='solid')
    entry_pass.place(x=14, y=290)

    label_pass_confirm = Label(frame_baixo, text='Confirme sua Senha *', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
    label_pass_confirm.place(x=10, y=340)

    entry_pass_confirm = Entry(frame_baixo, width=25, justify='left',show='*', font=('',15), highlightthickness=1, relief='solid')
    entry_pass_confirm.place(x=14, y=370)
    ###Botão
    button_confirm = Button(frame_baixo,command=botao_cadastrar,  text='Criar cadastro',width=34,height=2 , font=('Ivy 10'), bg=co2, fg=co1, relief=RAISED, overrelief= RIDGE )
    button_confirm.place(x=15, y=435) 



def cadastrar_dados():
    nome = entry_nome.get()
    sobrenome = entry_last_name.get()
    email = entry_email.get()
    senha = entry_pass.get()
    cursor.execute("INSERT INTO usuarios (Nome, Sobrenome, Email, Senha) VALUES (?, ?, ?, ?)", (nome, sobrenome, email, senha))
    db_cadastro.commit()
    messagebox.showinfo('Cadastrado', 'Usuario cadastrado com sucesso')


    tela_nova()



def botao_cadastrar():
    if verificar_dados(dados_corretos=True):
        cadastrar_dados()



###Botão
button_confirm = Button(frame_baixo,command=botao_cadastrar,  text='Criar cadastro',width=34,height=2 , font=('Ivy 10'), bg=co2, fg=co1, relief=RAISED, overrelief= RIDGE )
button_confirm.place(x=15, y=435) 



janela.mainloop()