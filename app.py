from flask import Flask,request
# 默认使用static存放静态资源 比如图片,js,css文件
# templartes存放模板文件

app = Flask(__name__)
# python内置变量__name__的值是字符串__main__ 。Flask类将这个参数作为程序名称。可以自定义的，比如app = Flask("my-app")
# 更多参数请参考__doc__：
#    print(Flask.__doc__)

@app.route('/')
def hello_world():  # put application's code here
    '''
    内容都在这里
    :return:
    '''

    # 浏览器传给我们的Flask服务的数据长什么样子呢？可以通过request.full_path和request.path来看一下
    print(request.path)
    print(request.full_path)

    # return 'Hello World!'
        # return 是返给client的东西
        # Hello World!只是HTTP响应报文的实体部分，状态码等信息既可以由Flask自动处理，也可以通过编程来制定。


    # return request.args.__str__()
    # # 列出所有url参数
    # # 访问http://127.0.0.1:5000/?user=Flask&time&p=7&p=8将显示所有参数:
    #     # ImmutableMultiDict([('user', 'Flask'), ('time', ''), ('p', '7'), ('p', '8')])

    # 要获取特定键对应的值:
        # request.args.get()
    return request.args.get('info')
    # request.args.get('info')返回Python内置的None，而Flask不允许返回None,
    # 所以用此return时访问http://127.0.0.1:5000/ 即不给info参数时会给flask返回none
    # 解决:
    # 方法一:
    # r = request.args.get('info')
    # if r==None:
    #     # do something
    #     return ''
    # return r
    # 方法二:
    # r = request.args.get('info', '若不给info时显示的默认值')
    #     return r
    # request.args.get的第二个参数用来设置默认值

    # 若要获取的特定键有多个时：
        # 使用request.args.getlist()


# # 获取POST方法传送的数据内容
# # 作为一种HTTP请求方法，POST用于向指定的资源提交要被处理的数据。我们在某网站注册用户、写文章等时候，
# # 需要将数据传递到网站服务器中。并不适合将数据放到URL参数中，密码放到URL参数中容易被看到，文章数据又太多，
# # 浏览器不一定支持太长长度的URL。这时，一般使用POST方法。
# # 本文使用python的requests库模拟浏览器
#
# # @app.route('/register',methods=['GET','POST'])
# # # 指url/register同时接受GET和POST
# # def register():
    # #     '''
    # #     这是'/'下的一个分支
    # #     :return:
    # #     '''
# #     print(request.headers)
    # #     '''
    # #     生成的HTTP请求头：
    # #     Host: 127.0.0.1:5000
    # #     User-Agent: python-requests/2.26.0
    # #     Accept-Encoding: gzip, deflate
    # #     Accept: */*
    # #     Connection: keep-alive
    # #     Content-Length: 24
    # #     '''
# #     print(request.stream.read())
    # #     '''
    # #     生成的 请求体 post的数据内容:
    # #     b'name=letian&password=123'
    # #     '''
# #     return 'welcome'
#
# # 若想获得name和password可以这么写:
# # Flask已经内置了解析器request.form
# @app.route('/register', methods=['POST'])
# def register():
#     print(request.headers)
#     # print(request.stream.read()) # 不要用，否则下面的form取不到数据
#     print(request.form)
#     print(request.form['name'])
#     print(request.form.get('name'))
#     print(request.form.getlist('name'))
#     print(request.form.get('nickname', default='default name'))
    #     '''
    #     request.form会自动解析数据
    #     request.form['name']和request.form.get('name')都会获得name的值
    #     request.form.get('name',default='default name') 当没有键那么时返回默认值default
    #     '''
    #     '''
    #     输出:
    #     ImmutableMultiDict([('name', 'sk'), ('password', '123')])
    #     sk
    #     sk
    #     ['sk']
    #     default name
    #     '''
#     # 如果name有多个值，可以使用request.form.getlist('name')，该方法将返回一个列表。
#     print(request.form.getlist('name'))
#
#
#     return 'welcome'


# 处理和响应JSON格式数据
'''
使用HTTP POST方法传到服务器的数据格式有很多种,比如上面中的通过&连接的键值对,还有很多比如JSON,XML
'''
# 如果是JSON格式数据,request.json会自动将其转化为python类型(字典或者列表)
@app.route('/add',methods = ['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']

    return str(result)
        # 此return响应回client的是str类型 若想响应回的时json类型可以:
    # 第一种:
    # return Response(json.dumps(result),  mimetype='application/json')
        # 其中mimetype='application/json'改变的是requset.headers中响应头的Content-Type
    # 第二种:使用jsonify工具函数
    # return jsonify(result)


if __name__ == '__main__':
    # app.run()

    app.run(port=5000,debug=True)
    # 此种运行方式 当服务器出错时会在客户端显示
    # 将debug设置为True的另一个好处是，程序启动后，会自动检测源码是否发生变化，若有变化则自动重启程序。这可以帮我们省下很多时间

    # 默认情况下，Flask绑定IP为127.0.0.1，端口为5000。我们也可以通过下面的方式自定义：
    # app.run(host='0.0.0.0', port=80, debug=True)
    # 0.0.0.0代表电脑所有的IP。80是HTTP网站服务的默认端口。

# URL参数是出现在url中的键值对，例如http://127.0.0.1:5000/?disp=3中的url参数是{'disp':3}。