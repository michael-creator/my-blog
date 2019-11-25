import os
class Config:
    SECRET_KEY="a9f5c99073afb2"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options ={
    'production' : ProdConfig,
    'development': DevConfig
}