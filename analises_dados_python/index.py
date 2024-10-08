from imap_tools import MailBox ,AND
 
usuario = 'diegofraga892@gmail.com'
senha = 'diego26032001'

meu_email = MailBox('imap.gmail.com').login(usuario,senha)
lista_email = meu_email.fetch(AND(from_='info@campaigns-br.betano.com'))
print(len(list(lista_email)))