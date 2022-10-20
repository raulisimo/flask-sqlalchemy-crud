import os

from dotenv import load_dotenv

load_dotenv()

user = (os.environ.get('MYSQL_USER'))
pwd = (os.environ.get('MYSQL_PWD'))
host = (os.environ.get('MYSQL_HOST'))
db = (os.environ.get('MYSQL_DB'))
port = (os.environ.get('MYSQL_PORT'))

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}'
