from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    if authorization_code:
        return 'Authorization Code Received: ' + authorization_code
    else:
        return 'No Authorization Code Found'

if __name__ == '__main__':
    app.run(port=8080)