# cookie 是储存在客户端的记录访问者状态的数据,常用的记录用户登陆状态的session一般基于cookie实现
# cookie可以借助flask.Response实现

from flask import Flask, request, Response, make_response
import time
# from pip._internal.utils import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/add')
def login():
    res = Response('add cookies')
        # 创建一个Response对象 括号里是在客户端显示的内容 不是传的参数
    res.set_cookie(key='name', value='sk')
    #, expires=time.localtime() + 6 * 60)
        # 使用Response.set_cookie添加和删除cookie
        # expires参数用来设置cookie有效时间

    return res


@app.route('/show')
def show():
    return request.cookies.__str__()


@app.route('/del')
def del_cookie():
    res = Response('delete cookies')
    res.set_cookie('name', '', expires=0)
    return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)