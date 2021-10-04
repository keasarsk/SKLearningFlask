# 自定义HTTP的404等错误 使用flask的abort函数

from flask import Flask, render_template_string, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user')
def user():
    abort(401)  # Unauthorized
# 当访问到/user分支时触发abort,401代表HTTP响应状态码

@app.errorhandler(401)
def page_unauthorized(error):
    return render_template_string('<h1> Unauthorized </h1><h2>{{ error_info }}</h2>', error_info=error), 401
# @app.errorhandler 中参数401是对网页URL的响应
# render_template_string是上节学的

if __name__ == '__main__':
    app.run(port=5000, debug=True)