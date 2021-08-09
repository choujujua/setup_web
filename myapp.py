from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!11'

if __name__ == '__main__':
    app.run(host='169.254.98.1', debug=True, port=80)  # 127.0.0.1 回路 自己返回自己