import sys
import sqlite3
app = Flask(__name__)
def main():
    n = sys.argv[1] if len(sys.argv) > 1 else ""
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
