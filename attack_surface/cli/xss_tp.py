from flask import Flask, request
app = Flask(__name__)
def main():
    print("<p>" + (sys.argv[1] if len(sys.argv)>1 else "") + "</p>") # was return "<p>" + request.args.get("q", "") + "</p>"
