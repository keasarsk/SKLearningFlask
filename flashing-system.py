# 闪存系统是flask框架用于向客户端反馈信息,这些反馈信息一般是对客户端上一步操作的反馈
# 反馈信息存储在服务器端,当服务器向客户端返回反馈信息之后就会被服务器端删除.

# 也就是暂时存放一些信息,一般用来存放客户端的上一步操作信息
# 想要下一次访问时让让上一次的flash存的内容展示 需要使用get_flashed_messages().__str或者其他类型__()方法
# 只要使用了get_flashed_messages()方法 flash内容就会被删除 无论输出了flash的多少内容,
#   比如先/show1 会输出flash的show1分类内容 但再次/show2 也不会输出flash的show2内容
from flask import Flask, flash, get_flashed_messages
import time

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return 'hi'


@app.route('/gen')
def gen():
    info = 'access at ' + time.time().__str__()
    flash('show1 ' + info, category='show1')
    flash('show2 ' + info, category='show2')
        # 此时生成了两个flash信息
    return info


@app.route('/show1')
def show1():
    return get_flashed_messages(category_filter='show1').__str__()


@app.route('/show2')
def show2():
    return get_flashed_messages(category_filter='show2').__str__()


if __name__ == "__main__":
    app.run(port=5000, debug=True)