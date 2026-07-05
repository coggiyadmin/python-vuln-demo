"""TN — SOAP arg parameterized."""
import sqlite3
def get_user(soap_arg):
    sqlite3.connect(':memory:').execute("SELECT * FROM u WHERE id=?", (soap_arg,))
