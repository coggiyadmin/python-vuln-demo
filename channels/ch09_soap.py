"""CH-09 SOAP operation — arg -> SQL sink."""
import sqlite3
def get_user(soap_arg):
    uid = soap_arg  # SOURCE SOAP body arg
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE id='" + uid + "'")  # SINK CWE-89
