# 若出现
# The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
# 即端口号为5000的服务进程进行了多次
# 在终端中找出端口5000的进程，将进程杀死
# netstat -ano | findstr 5000
# taskkill /pid XXXXX /f                （XXXXX的地方用进程号替换）

from flask import Flask, request

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 文件上传到的目录
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
    # app.config中的config是字典的子类，可以用来设置自有的配置信息，也可以设置自己的配置信息
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 集合类型


# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
'''
     '.' in filename  
        # 判断是否有 .
     filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
        # 判断 . 后的文件格式是否在ALLOWED_EXTENSIONS中
'''


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
        # 客户端上传的图片必须以image标识(client中设置)。upload_file是上传文件对应的对象。
    if upload_file and allowed_file(upload_file.filename):
            # 判断upload_file是否非空并且是否合法
        filename = secure_filename(upload_file.filename)
        # 判断upload_file.filename是否是个安全名字 用werkzeug.utils的功能

        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            # app.root_path获取server.py所在目录在文件系统中的绝对路径
            # upload_file.save(path)用来将upload_file保存在服务器的文件系统中，参数最好是绝对路径，否则会报错
            # 函数os.path.join()用来将使用合适的路径分隔符将路径组合起来。
        return 'info is ' + request.form.get('info', '') + '. success'
    else:
        return 'failed'


if __name__ == '__main__':
    app.run(port=5000, debug=True)