import requests

# # 简单的向服务器发送POST
# user_info = {'name': 'sk', 'password': '123'}
# r = requests.post("http://127.0.0.1:5000/register", data=user_info)

# # 向服务器发送json格式数据
# json_data = {'a': 1,'b': 2}
# r = requests.post("http://127.0.0.1:5000/add",json = json_data)


# uploadFile
file_data = {'image': open('sk.jpg', 'rb')}

user_info = {'info': 'sk'}

r = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)



print(r.text)