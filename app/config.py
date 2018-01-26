class Config:
    '''
    general configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    production configuration child class
    args:
        config:the parent configuration class with 
        general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    args:
        config:the parent configuration class with
        general configuration settings
    '''
    DEBUG = True
