# Jinja2模板引擎 负责MVC中的V view
'''
Flask与模板相关的函数有：

    flask.render_template(template_name_or_list, **context)
    Renders a template from the template folder with the given context.
    flask.render_template_string(source, **context)
    Renders a template from the given template source string with the given context.
    flask.get_template_attribute(template_name, attribute)
    Loads a macro (or variable) a template exports. This can be used to invoke a macro from within Python code.
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user')
def user():
    user_info = {
        'name': 'sk',
        'email': '123@aa.com',
        'age': 0,
        'github': 'https://github.com/letiantian'
    }
    return render_template('user_info.html', page_title='sk\'s info', user_info=user_info)
        # render_template()函数的第一个参数指定模板文件，后面的参数是要传递的数据。

if __name__ == '__main__':
    app.run(port=5000, debug=True)