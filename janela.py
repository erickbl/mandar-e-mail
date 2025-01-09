import pyautogui as pa
import customtkinter as ctk

# Função que envia o e-mail
def mail():
    # Define um intervalo de pausa entre os comandos para evitar erros
    pa.PAUSE = 2  
    
    # Captura os valores inseridos nos campos
    email = emaill.get()
    assunto_texto = assunto.get()  # Renomeado para evitar conflito de nome com a função
    text = texto.get()
    
    # Abrir o navegador
    pa.press('win')  # Pressiona a tecla Windows
    pa.write('chrome')  # Digita "chrome" para abrir o navegador
    pa.press('ENTER')  # Confirma
    pa.write('gmail.com')  # Digita o endereço do Gmail
    pa.press('ENTER')  # Acessa o site

    # Aguarda a página carregar (tempo extra pode ser ajustado conforme necessário)
    pa.sleep(10)

    # Clica para iniciar um novo e-mail (a coordenada deve ser ajustada conforme a resolução)
    pa.click(x=65, y=184)  

    # Escreve o e-mail
    pa.write(email)  # Digita o e-mail do destinatário
    pa.press('tab')  # Avança para o campo "Assunto"
    pa.press('tab')  

    # Escreve o assunto
    pa.write(assunto_texto)  
    
    pa.press('tab')  # Avança para o corpo do e-mail
    
    # Escreve o corpo do e-mail
    pa.write(text)

    # Aqui você pode adicionar comandos para enviar o e-mail, como clicar no botão "Enviar".

# Configura a aparência do CustomTkinter
ctk.set_appearance_mode('dark')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Mensagens')  # Título da janela
app.geometry('500x400')  # Tamanho da janela

# Campo para e-mail
campo_emai = ctk.CTkLabel(app, text='E-mail')  # Label para o campo de e-mail
campo_emai.pack(pady=10)  # Espaçamento

emaill = ctk.CTkEntry(app, placeholder_text='Digite o e-mail')  # Campo para inserir o e-mail
emaill.pack(pady=10)

# Campo para assunto
campo_assuto = ctk.CTkLabel(app, text='Assunto')  # Label para o campo de assunto
campo_assuto.pack(pady=10)

assunto = ctk.CTkEntry(app, placeholder_text='Digite o Assunto')  # Campo para inserir o assunto
assunto.pack(pady=10)

# Campo para o texto
campo_txto = ctk.CTkLabel(app, text='Texto')  # Label para o texto
campo_txto.pack(pady=10)

texto = ctk.CTkEntry(app, placeholder_text='Digite o texto',width=200,height=50)  # Campo para inserir o texto
texto.pack(pady=10)

# Botão para iniciar o processopip install pyinstaller

iniciar_button = ctk.CTkButton(app, text='INICIAR', command=mail)  # O comando "mail" é passado sem parênteses
iniciar_button.pack(pady=20)

# Loop principal do CustomTkinter
app.mainloop()
