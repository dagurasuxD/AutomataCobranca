from time import sleep
def cabecalho():
    print('-'*50)
    print('BOT WHATSAPP'.center(50))
    print('-'*50)
    sleep(1.5)

def sobre():
    print('-'*50)
    print('CRIADO POR: DOUGLAS MENESES - Desenvolvedor de Softwares e Automações'.center(50))
    print('Versão Alpha 0.1b.'.center(50))
    print('-'*50)

def inicio(x=True):
    print('Antes de começar, é importante frisar que esse programa deve ser rodado sozinho na máquina. Não é permitido o uso da máquina enquanto o programa é executado, podendo ocasionar em erros.')
    print('É de suma importância que a máquina já esteja logada no WhatsApp Web. Se ainda não estiver, aguardamos você logar.')
    while True:
        try:
            resp=str(input('Estando ciente disso, podemos iniciar? [S/N] ').strip().upper()[0])
            while resp not in 'SsNn':
                resp=str(input('Oops. Você digitou algo que não é um "Sim" ou "Não". Tente novamente: ').upper().strip()[0])
            if resp in 'Nn':
                print('Certo. Execute novamente o programa após o término de suas atividades para iniciarmos o processo.')
                print('ENCERRANDO.',end='',flush=True)
                sleep(0.5)
                print('.',end='',flush=True)
                sleep(0.5)
                print('.')
                sleep(1)
                x=False
                break
            elif resp in 'Ss':
                print('Certo. Vamos começar!')
                break
        except (ValueError,TypeError):
            print('Oops. Você digitou algo que não é um "Sim" ou "Não". Tente novamente.')
        except (KeyboardInterrupt,IndexError):
            print('Oops. Você digitou algo que não é um "Sim" ou "Não". Tente novamente.')
    return x

def execucao(x):
    print('-'*50)
    print('INICIANDO...'.center(50))
    print('-'*50)
    while True:
        try:
            zapzap=str(input('Você já abriu o seu navegador? [S/N] ').upper().strip()[0])
            while zapzap in 'Nn':
                print('Certo, ficarei no aguardo...')
                sleep(10)
                zapzap=str(input('Você já abriu o seu navegador? [S/N] ').upper().strip()[0])
            if zapzap in 'Ss':
                print('Certo, vamos começar com os envios de mensagem. Por favor, não mexa na máquina enquanto o processo não for finalizado.')
                print('Verificando se há mensagens para serem enviadas.')
                sleep(5)
                if x > 0:
                    print(f'Número de contatos a enviar mensagem: {x}. Prazo de termino da execução é de aproximadamente {x*68} segundos.')
                    print('Abra a tela de seu navegador e não mexa na máquina...')
                    sleep(5)
                    break
                else:
                    print('Nenhum contato atende aos critérios para enviar a mensagem. Encerrando...')
                    sleep(2)
                    break
        except (ValueError,TypeError):
            print('Oops. Você digitou algo que não é um "Sim" ou "Não". Tente novamente.')
        except (KeyboardInterrupt,IndexError):
            print('O usuário não quis continuar com o processo. Encerrando...')
            break

def fim():
    print('-'*50)
    print('OBRIGADO. VOLTE SEMPRE!'.center(50))
    print('-'*50)
    sleep(3)

def escolha():
    print('Iniciar [1]\nSobre [2]')
    while True:
        try:
            esc=str(input('Escolha: ').strip()[0])
            while esc not in '12':
                esc=str(input('Oops. Parece que você não digitou uma escolha válida. Tente novamente.\nEscolha: '))
            if esc=='1':
                break
            elif esc=='2':
                sobre()
                sleep(5)
                break
        except (ValueError,TypeError):
            print('Oops. Você digitou algo que não é uma escolha válida. Tente novamente.')
        except (KeyboardInterrupt,IndexError):
            print('O usuário não quis continuar com o processo. Encerrando...')
            break