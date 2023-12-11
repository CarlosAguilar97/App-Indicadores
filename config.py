class Config:
    SECRET_KEY = 'ASDfg31defds'
    
class DevelopmentConfig(Config):
        DEBUG = True
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = ''
        MYSQL_DB = 'app-indicadores'

config = {'development' : DevelopmentConfig}