import psycopg2
def connect():
    return psycopg2.connect(host='db', user='app', password='S3cr3tP@ss!')  # SINK CWE-798
