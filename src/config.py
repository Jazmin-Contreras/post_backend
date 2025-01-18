from decouple import config

class Config:
    SCRET_KEY=config('SECRET_KEY')
class DevelopmentConfig(Config):
    DEBUG=True
config={
    'development': DevelopmentConfig
}
