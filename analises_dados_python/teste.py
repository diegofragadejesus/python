from imap_tools import MailBox, AND

# Credenciais
usuario = 'diegofraga892@gmail.com'  # Corrigir o e-mail para gmail.com
senha = 'diego26032001'

# Corrigir o servidor IMAP para Gmail
meu_email = MailBox('imap.gmail.com').login(usuario, senha)

# Corrigir a query AND no fetch
lista_email = meu_email.fetch(AND(from_='diegofraga892@gmail.com'))

# Processar os e-mails
for msg in lista_email:
    print(f'Assunto: {msg.subject}')
    print(f'De: {msg.from_}')
    print(f'Data: {msg.date}')
    print(f'Conteúdo: {msg.text}')
