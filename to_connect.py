import pymysql.cursors

def connect():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='makertplace',
        charset='utf8mb4',
        cursorclass =pymysql.cursors.DictCursor
    )
    return conexao

    