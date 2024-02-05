# librarias que eu usei neste projecto --------------------------------------------------------------------
from tkinter import Listbox, Scrollbar, messagebox
import customtkinter
import tkinter as tk
import threading
import _threading_local
#----------------------------------------------------------------------------------------------------------
# função para informar o Utilizador -----------------------------------------------------------------------
def info():
    messagebox.showinfo('Informacao',
                        'Este Programa Nascesu com vista' 
                         +'\n a Ajudar-te a defenir as cores para'
                         +' \n O teu projectos em Python'
                         +'\nAutor: Dev Joel Portugal 2024 ©'
                         +'\nTu que amas programar Python Como eu' 
                         +'\nEste programa Nasceu para Ti !...')
#----------------------------------------------------------------------------------------------------------
# função para sair do programa ----------------------------------------------------------------------------
def sair_programa():
    # Exibir caixa de diálogo de confirmação
    resposta = messagebox.askyesno("Sair", "Deseja realmente sair do programa?....")

    # Verificar a resposta
    if resposta:
        # Se a resposta for 'Sim', encerrar o programa
        Janela.destroy()
#----------------------------------------------------------------------------------------------------------
# função para Copiar as Cores de Lcores--------------------------------------------------------------------
def copiar_conteudo():
    # Obter todos os itens da Listbox
    itens_listbox = Lcores.get(0, tk.END)

    # Concatenar os itens em uma única string com quebras de linha
    conteudo = '\n'.join(itens_listbox)

    # Copiar o conteúdo para a área de transferência
    Janela.clipboard_clear()
    Janela.clipboard_append(conteudo)
    Janela.update()
    messagebox.showinfo('Codicos','Os seus codicos Foram Copiados Com sucesso!......')    
#---------------------------------------------------------------------------------------------------------

# função para Limpar campos --------------------------------------------------------------------------
def limpar_campos():
    # Limpar os campos Entry
    ENomeCor.delete(0, "end")
    Ehexa.delete(0, "end")
    ERGB.delete(0, "end")

    # Redefinir os valores dos sliders para zero
    Svermelho.set(0)
    Sverde.set(0)
    SAzul.set(0)

    # Atualizar os labels com os valores zerados
    Lvermelho.configure(text='Vermelho: 0')
    Lverde.configure(text='Verde: 0')
    LAzul.configure(text='Azul: 0')

    # Atualizar o Entry com a string "ERGB" e "Ehexa" para valores zerados
    ERGB.insert(0, 'Codico RGB: (0,0,0)')
    Ehexa.insert(0, 'Codico Hexdecimal: #000000')

    # Limpar a Listbox Lcores
    Lcores.delete(0, "end")

    # Atualizar a cor de fundo do CTkCanvas para preto
    PCor.config(bg='black')
    messagebox.showinfo('Limpeza','A sua Lista Foi limpa com sucesso!......')
#------------------------------------------------------------------------------------------------------

# Função para carregar a cor --------------------------------------------------------------------------
def carregar_cor():
    # Obter os valores dos Entry
    nome_cor = ENomeCor.get()
    cor_hexadecimal = Ehexa.get()
    cor_rgb = ERGB.get()

    # Verificar se os campos estão preenchidos
    if nome_cor and cor_hexadecimal and cor_rgb:
        # Adicionar a cor à Listbox
        cor_entry = f"{nome_cor}: {cor_hexadecimal} | {cor_rgb}"
        Lcores.insert("end", cor_entry)
    else:
        # Mostrar mensagem de erro se algum campo estiver vazio
        messagebox.showerror("Erro", "Preencha todos os campos!") 
#-----------------------------------------------------------------------------------------------------------

# função para Actualizar Cor -------------------------------------------------------------------------------
def atualizar_cor(event=None):
    # Obter os valores dos sliders
    valor_vermelho = int(Svermelho.get())
    valor_verde = int(Sverde.get())
    valor_azul = int(SAzul.get())

    # Atualizar os labels com os valores dos sliders
    Lvermelho.configure(text=f'Vermelho: {valor_vermelho}')
    Lverde.configure(text=f'Verde: {valor_verde}')
    LAzul.configure(text=f'Azul: {valor_azul}')

    # Criar a string "ERGB"
    cor_rgb = 'Codico RGB:'+ f'({valor_vermelho},{valor_verde},{valor_azul})'
    cor_hex = ("Codico Hexdecimal:"+"#{:02X}{:02X}{:02X}").format(valor_vermelho, valor_verde, valor_azul)

    # Atualizar o Entry com a string "ERGB"
    ERGB.delete(0, "end")
    ERGB.insert(0, cor_rgb)
    
    # Atualizar o Entry com a string "ERGB"
    Ehexa.delete(0, "end")
    Ehexa.insert(0, cor_hex)

    # Atualizar a cor de fundo do CTkCanvas
    cor_hex = f'#{valor_vermelho:02X}{valor_verde:02X}{valor_azul:02X}'
    PCor.config(bg=cor_hex)

#-----------------------------------------------------------------------------------------------------------
# Criar a janela--------------------------------------------------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('600x465+100+100')
Janela.title('Cores De Portugal dev Joel 2024 ©')
Janela.resizable(False, False)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\projectos\\programas\\selector de cores\\icon.ico')
#----------------------------------------------------------------------------------------------------------
# criar o frontend ----------------------------------------------------------------------------------------
# criar o painel canvas Cor -------------------------------------------------------------------------------
PCor = customtkinter.CTkCanvas(Janela)
PCor.place(x=10, y=10)
PCor.config(bg='white', width=200, height=170)
#----------------------------------------------------------------------------------------------------------
# criar o label de Controle -------------------------------------------------------------------------------
Lvermelho = customtkinter.CTkLabel(Janela, text='Vermelho:0')
Lvermelho.place(x=180, y=10)
Lverde = customtkinter.CTkLabel(Janela, text='Verde:0')
Lverde.place(x=180, y=55)
LAzul = customtkinter.CTkLabel(Janela, text='Azul:0')
LAzul.place(x=180, y=95)
#----------------------------------------------------------------------------------------------------------
# criar o slider ------------------------------------------------------------------------------------------
Svermelho = customtkinter.CTkSlider(Janela, from_=0, to=255, width=399, command=atualizar_cor)
Svermelho.place(x=180, y=39)
Sverde = customtkinter.CTkSlider(Janela, from_=0, to=255, width=399, command=atualizar_cor)
Sverde.place(x=180, y=80)
SAzul = customtkinter.CTkSlider(Janela, from_=0, to=255, width=399, command=atualizar_cor)
SAzul.place(x=180, y=120)
#----------------------------------------------------------------------------------------------------------
# criar a entry -------------------------------------------------------------------------------------------
ENomeCor = customtkinter.CTkEntry(Janela, placeholder_text='Isira o nome da cor')
ENomeCor.place(x=10, y=155)
Ehexa = customtkinter.CTkEntry(Janela, placeholder_text='Cor hexadecimal', width=190)
Ehexa.place(x=155, y=155)
ERGB = customtkinter.CTkEntry(Janela, placeholder_text='Cor RGB', width=190)
ERGB.place(x=350, y=155)
#----------------------------------------------------------------------------------------------------------
# criar Botões --------------------------------------------------------------------------------------------
Bcarregar = customtkinter.CTkButton(Janela,text='Carregar', command=carregar_cor,)
Bcarregar.place(x=10, y=195)
BLimpar = customtkinter.CTkButton(Janela,text='Limpar', command=limpar_campos)
BLimpar.place(x=160, y=195)
BCopiar = customtkinter.CTkButton(Janela,text='Copiar', command=copiar_conteudo)
BCopiar.place(x=310, y=195)
BSair = customtkinter.CTkButton(Janela,text='Sair', width=140, command=sair_programa)
BSair.place(x=455, y=195)
Binfo = customtkinter.CTkButton(Janela,text='info', width=140, command=info)
Binfo.place(x=10, y=420)
#----------------------------------------------------------------------------------------------------------
# criar uma Listbox para armazenar os codicos das Cores ---------------------------------------------------
Lcores = Listbox(Janela, width=65, font=('arial', 14))
Lcores.place(x=10, y=285)
#----------------------------------------------------------------------------------------------------------
# criar um scrollbar --------------------------------------------------------------------------------------
# criar um scrollbar
scrollbar = Scrollbar(Janela, command=Lcores.yview)
scrollbar.place(x=710, y=286, height=233)
# vincular o scrollbar à Listbox
Lcores.config(yscrollcommand=scrollbar.set)
#-----------------------------------------------------------------------------------------------------------
# Vincular a função de atualização à mudança nos sliders ---------------------------------------------------
Svermelho.bind("<ButtonRelease-1>", atualizar_cor)
Sverde.bind("<ButtonRelease-1>", atualizar_cor)
SAzul.bind("<ButtonRelease-1>", atualizar_cor)
#-----------------------------------------------------------------------------------------------------------
# Executar o loop principal da janela ----------------------------------------------------------------------
Janela.mainloop()
#-----------------------------------------------------------------------------------------------------------