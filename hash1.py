import hashlib
a = hashlib.md5()
a.update(b'python')
print(a.digest())
print('=========================')
data =[b'paris', b'alii', b'hello']
for i in data:
    print(hashlib.sha256(i).hexdigest())#we could say like that ===> a = hashlib.sha256(d)  a.hexdigest()
