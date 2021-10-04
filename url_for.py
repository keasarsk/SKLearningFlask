# 使用工具函数url_for生成链接 提高开发效率
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    pass


@app.route('/user/<name>')
def user(name):
    pass


@app.route('/page/<int:num>')
def page(num):
    pass


@app.route('/test')
def test():
    print(url_for('hello_world'))
    '''
        这个'hello_world'是分支名(函数名)
        生成到这个分支的 后续 链接即 /
    '''
    print(url_for('user', name='sk'))
    '''
        生成到分支user,参数name取'sk'的 后续链接 即 /user/sk
    '''
    print(url_for('page', num=1, q='hadoop mapreduce 10%3'))
    print(url_for('static', filename='uploads/01.jpg'))

    return 'Hello'
    # return的东西显示在浏览器中 上面的print等输出内容显示在.py运行台


if __name__ == '__main__':
    app.run(debug=True)