from mysql.connector import Error
from sqlalchemy import create_engine
import mysql
import json

def setInfosConect() -> dict[str]:
    """
    => Função utilizada para obter as informações necessárias para conectar
    no Banco de Dados
    :return: Retorna user,database,password e host utilizados para conectar no BD
    """

    with open("/home/bug/Documents/resolucaocases/app/configs/conexao.json") as f:
        conexao = json.load(f)
    return conexao

def conectaBD() -> mysql.connector.connect:
    """ 
    => Função utilizada para criar a conexão no banco de dados MySQL
    :return: Retorna a variável de conexão com o banco
    
    """

    #Obtendo as informações para a para conexão
    conexao = setInfosConect()

    # Passando as informações necessárias para criar a conexão com o MySQL
    conn = mysql.connector.connect(user= conexao["user"], 
                                   database= conexao["database"],
                                   password= conexao["password"],
                                   host= conexao["host"])
    return conn


def criaEngine() -> create_engine:
    """
    => Função que cria a engine para realizar a conexão ao banco de dados
    :return: Returna a engine que será utilizada para as cargas de dados
    
    """

    #Obtendo as informações para a para conexão
    conexao = setInfosConect()

    # Informações conectar ao Banco de Dados
    user=conexao["user"]
    database= conexao["database"]
    password= conexao["password"]
    host= conexao["host"]

    # Criando a engine que será utilizada para conectar ao Banco de Dados
    return create_engine('mysql+mysqlconnector://'+user+':'+password+'@'+host+':3306/'+database+'', echo = False)