from flask import Flask, request, redirect
app = Flask(__name__)
ALLOW = ('https://app.example.com',)
@app.route('/go')
def go():
    nxt = request.args.get('next', '')
    if nxt.startswith(ALLOW):
        return redirect(nxt)  # SINK CWE-601
    return redirect('/home')
