import os

class Config:
   '''
   General configuration parent class
   '''
   MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
   MOVIE_API_KEY = os.environ.get('ca01d53b89a120406e5cc40fb64905e3')
   SECRET_KEY = os.environ.get('sly14')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly14@localhost/watchlist'


   
class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   pass
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


