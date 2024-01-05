from lib.leitura_excel import Main_lib
from lib.interface import *
from lib.sistema import bot_mensagem_cobranca


df=Main_lib()
contatos_a_enviar=df[df['Mensagem_Necessária']]==True
numero_de_contatos = len(contatos_a_enviar)
cabecalho()
escolha()
x=inicio()
if x:
    execucao(numero_de_contatos)

    if numero_de_contatos > 0:
        bot_mensagem_cobranca()

    fim()
else:
    fim()