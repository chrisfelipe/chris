import mysql.connector
#procedimento padrao
print('cadastro de usuarios ')
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='final'
)
cursor = banco.cursor()
while True:
        nome = str(input('Nome: '))

        idade = int(input('Idade: '))

        email = str(input('E-mail: '))

        ddd= int(input('qual o ddd ?'))

        telefone= int(input('qual o numero de celular ? '))


        dados = f'"{nome}", "{idade}", "{email}", "{ddd}", "{telefone}"'

        comando_SQL = f'insert into pessoas (nome,idade,email,ddd,telefone) values ({dados})'

        cursor.execute(comando_SQL)

        resp =str(input('continuar [s/n] ? ')).upper()
        if resp in "Nn":
            break


banco.commit()