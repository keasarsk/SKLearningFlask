# Restful URL 可以看做对URL参数的替代
# 相当于在@app.route中就把URL的参数取出来赋予函数定义时的传参 （例如def user的username）
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'



@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username

@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username + '. There are your friends'


'''
由上面的示例可以看出，使用 Restful URL 得到的变量默认为str对象。
如果我们需要通过分页显示查询结果，那么需要在url中有数字来指定页数。
按照上面方法，可以在获取str类型页数变量后，将其转换为int类型。
不过，还有更方便的方法，就是用flask内置的转换机制，即在route中指定该如何转换。

官方资料中，说是有3个默认的转换器:
int         accepts integers
float       like int but for floating point values
path        like the default but also accepts slashes
'''
@app.route('/page/<int:num>')# 此处的 <int:num>
def page(num):
    print(num)
    print(type(num))
    return 'hello world'

'''
也可以这么写
此时可以访问http://127.0.0.1:5000/page/11-22
'''
@app.route('/page/<int:num1>-<int:num2>')
def page(num1, num2):
    print(num1)
    print(num2)
    return 'hello world'




'''
自己编写转换器
自定义的转换器是一个继承werkzeug.routing.BaseConverter的类，修改to_python和to_url方法即可。
to_python方法用于将url中的变量转换后供被`@app.route包装的函数使用，to_url方法用于flask.url_for`中的参数转换
'''
from flask import url_for
from werkzeug.routing import BaseConverter

class MyIntConverter(BaseConverter):

    def __init__(self, url_map):# 这句不用管
        super(MyIntConverter, self).__init__(url_map)

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value * 2

app = Flask(__name__)
app.url_map.converters['my_int'] = MyIntConverter# my_int就是自己编写的转换器类型 同官方的int float path

@app.route('/page/<my_int:num>')
def page(num):
    print(num)
    print(url_for('page', num=123))  # page 对应的是 page函数 ，num 对应对应`/page/<my_int:num>`中的num，必须是str
    return 'hello world'

'''
'''



if __name__ == '__main__':
    app.run(port=5000, debug=True)
