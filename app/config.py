class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything/{}?apiKey={}'
    

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
