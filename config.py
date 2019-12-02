import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.environ.get('7457465fhcdcbdfgcdfrtr')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'New Blog'
    SENDER_EMAIL = 'jumbamathews6@gmail.com'

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://cmsowuzzgjvjqm:c80ad4e60db4386975bd289b809ca05ddc753effc04059da0d8151f686e8c2be@ec2-184-73-209-230.compute-1.amazonaws.com:5432/d1gnev69cdiqu'

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://cmsowuzzgjvjqm:c80ad4e60db4386975bd289b809ca05ddc753effc04059da0d8151f686e8c2be@ec2-184-73-209-230.compute-1.amazonaws.com:5432/d1gnev69cdiqu'
    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,
'test': TestConfig
}
