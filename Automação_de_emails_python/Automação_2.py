import yagmail
from time import sleep

cont = 0
emails = ["empresa1@gmail.com", "empresa2@gmail.com", "empresa3@gmail.com"]

while cont < len(emails):

    receiver = emails[cont]

    message = ('''
Bom dia,

Segue em anexo meu curriculo

Atenciosamente,

Eu
''', "Meu_curriculo.doc")

    sender = yagmail.SMTP("meu_email@gmail.com", "minha_senha_super_secreta")

    sender.send(to=receiver, subject="Meu curriculo - tecnologia da informação", contents=message)

    cont += 1
    sleep(30)



