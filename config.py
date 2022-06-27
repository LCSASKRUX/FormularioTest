#CONFIGURACION DE VARIABLES DE CONEXION A LA BASE DE DATOS Y FLASK


class DevelopmentConfig():
    DEBUG = True
    DB_HOST = "kesavan.db.elephantsql.com"
    DB_NAME = "jvifvcvs"
    DB_USER = "jvifvcvs"
    DB_PASSWORD = "GdeM1cVS7J8cDom_l0PqebBnQMVh1aD3"

config = {
    'development': DevelopmentConfig
}

import datetime

