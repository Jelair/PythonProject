
import requests

# 通过GET访问一个页面
#r = requests.get('https://www.douban.com') # 豆瓣首页
#print(r.status_code)
#print(r.text)

# 对于带参数的URL，传入一个dict作为params参数
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print(r.content)

# 直接获取json
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
jsonStr = r.json()
print(jsonStr)

# 需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/',  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# 对于json数据，可以直接作为参数
# url = 'https://www.douban.com'
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# 上传文件需要更复杂的编码格式，但是requests把它简化为files参数：
# upload_files = {'file' : open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)
# 在读取文件时，
# 注意务必使用'rb'即二进制模式读取，
# 这样获取的bytes长度才是文件的长度

# 获取响应头
print(r.headers)
print(r.headers['Content-Type'])

# 获取指定的Cookie
cook = r.cookies['ts']

# 在请求中传入Cookie，只需准备一个dict传入cookies参数
# cs = {'token': '1234', 'status': 'working'}
# r = requests.get(url, cookies=cs)

# 指定超时
# r = requests.get(url, timeout=2.5) # 2.5秒后超时
