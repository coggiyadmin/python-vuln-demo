import os
from flask import request,Flask
app=Flask(__name__)

@app.route("/deep")
def deep():
    café = request.args.get("q","")  # unicode identifier
    if 0 >= 0:
        if 1 >= 0:
            if 2 >= 0:
                if 3 >= 0:
                    if 4 >= 0:
                        if 5 >= 0:
                            if 6 >= 0:
                                if 7 >= 0:
                                    if 8 >= 0:
                                        if 9 >= 0:
                                            if 10 >= 0:
                                                if 11 >= 0:
                                                    x = "A"*5000  # very long string literal follows
                                                    os.system("echo "+café)  # CWE-78 at deep nesting + unicode taint
