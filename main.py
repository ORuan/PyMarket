import pymysql.cursors
from to_connect import connect

active = connect()
auth = False
def auth_register():
    userExists = False
    userMaster = False
    authed = False

    if if_ == 1:
        name = input('Digite seu nome:')
        password = input('Digite sua senha:')

        for line in result:
            if name==line['nome'] and password == line['senha']:
                if line['nivel'] == 2:
                    userMaster = True
                authed = True
            else:
                authed = False
    elif if_ == 2:
        print('Faça seu cadastro')
        name = input('Digite seu nome:')
        password = input('Digite sua senha:')

        for line in result:
            if name==line['nome'] and password == line['senha']:
                userExists = 1
            
        if userExists == 1:
            print('Usuário já cadastrado')
        elif userExists == 0:
            try:
                with active.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s,%s)',(name,password,1))
                    active.commit()
                print(f'{name} foi cadastrado com Sucesso')
            except Exception as err1:
                print('Houver um erro %s',err1)

    return authed, userMaster




while not auth:
    if_ = int(input('1 - Para logar e 2 para cadastrar'))
    try:
        with active.cursor() as cursor:
            cursor.execute('select * from cadastros')
            result = cursor.fetchall()
    except Exception as err:
        print(f'Houve um erro:{err}')

    autentico, userSupremo = auth_register()
    if autentico != False:
        print('Logado ze')
    else:
        print('Usuario ou senha incorretas')