import os, psycopg2
def connect():
    return psycopg2.connect(host='db', user='app', password=os.environ['DB_PASSWORD'])
