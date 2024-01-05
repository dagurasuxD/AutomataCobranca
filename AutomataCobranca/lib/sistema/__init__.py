import pyautogui
from time import sleep
from lib.leitura_excel import Main_lib
from lib.interface import *
import sys
import keyboard


df=Main_lib()
def bot_mensagem_cobranca():
    sys.stdout.reconfigure(encoding='utf-8')
    # index é a linha e row é a célula;
    for index,row in df.iterrows():
        # Se a linha da coluna 'Mensagem_Necessária' for True, ele fará o processo, senão ele pula para próxima linha da mesma coluna até o fim da planilha.
        if row['Mensagem_Necessária']:
            pyautogui.hotkey('ctrl','t')
            pyautogui.click(411,48)
            whatsapp_number = ''.join(filter(str.isdigit, str(row['WHATSAPP']))) 
            keyboard.write(f'wa.me/{whatsapp_number}')
            pyautogui.press('enter')
            sleep(8)
            pyautogui.click(640,348)
            sleep(5)
            pyautogui.click(597,427)
            sleep(30)
            pyautogui.click(707,720)
            nome_da_pessoa = row['NOME']
            valor_da_divida = row['VALOR DÍVIDA']
            data_de_vencimento = row['DATA DE VENCIMENTO']
            mensagem_personalizada = f'Oi, {nome_da_pessoa}. Estamos entrando em contato para informar sobre a sua dívida em aberto conosco no valor de R${valor_da_divida}. A data de vencimento é de {data_de_vencimento} e ainda não reconhecemos o pagamento.'
            keyboard.write(mensagem_personalizada)
            sleep(2)
            pyautogui.press('enter')
            sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            sleep(2)