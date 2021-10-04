# redirect 函数用于重定向网址
# 实现机制为向客户端(浏览器)发送一个重定向的HTTP报文，使客户端去访问客户端中指定的URL
from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/test1')
def test1():
    print('this is test1')
    return redirect(url_for('test2'))
    # 访问http://127.0.0.1:5000/test1 这里直接就转到test2了


@app.route('/test2')
def test2():
    print('this is test2')
    return 'this is test2'


if __name__ == '__main__':
    app.run(debug=True)