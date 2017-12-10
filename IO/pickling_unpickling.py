import pickle
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
d = dict(name='Bob', age=20, score=88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object
import json
j = json.dumps(d)
#j2 = json.dump(d, f)
print(j)
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
k = json.loads(j)
print(k)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))