class Config:
    SECRET_KEY = "sua_chave_secreta"
    DEBUG = True  

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/bd_bankcap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
