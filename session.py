from flask import Flask, render_template_string, \
    session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'
    # app.secret_key用于给session加密。

@app.route('/')
def hello_world():
    return 'hello world'

'''
在/login中将向用户展示一个表单，要求输入一个名字，submit后将数据以post的方式传递给/do_login，
/do_login将名字存放在session中
'''
@app.route('/login')
def login():
    page = '''
    <form action="{{ url_for('do_login') }}" method="post">
        <p>name: <input type="text" name="user_name" /></p>
        <input type="submit" value="Submit" />
    </form>
    '''
    return render_template_string(page)

@app.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    session['user_name'] = name
    return 'success'


@app.route('/show')
def show():
    return session['user_name']

'''
/logout用于登出，通过将session中的user_name字段pop即可。
Flask中的session基于字典类型实现，调用pop方法时会返回pop第一个参数的键对应的值；
如果要pop的键并不存在，那么返回值是pop()的第二个参数

使用redirect()重定向时，一定要在前面加上return
'''
@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))

# shezhisession的有效时间
from datetime import timedelta
from flask import session, app

session.permanent = True
app.permanent_session_lifetime = timedelta(minutes=5)

if __name__ == '__main__':
    app.run(port=5000, debug=True)