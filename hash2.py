import hashlib as f
import time as t
print('''
1-md5
2-sha1
3-sha224
4-sha256
5-sha384
6-sha512
'''
)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('please choose one of this option')
ch = int(input('chosse option only with number ===>> '))
t.sleep(2)
x = input(' now please enter your data for hashing===>>')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
''''
here we produce 
hash code for data
'''
if ch == 1:
    a = f.md5()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-md5 : {Ha}')
elif ch == 2:
    a = f.sha1()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-sha1 : {Ha}')
elif ch == 3:
    a = f.sha224()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-sha224 : {Ha}')
elif ch == 4:
    a = f.sha256()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-sha256 : {Ha}')
elif ch == 5:
    a = f.sha384()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-sha384 : {Ha}')
elif ch == 6:
    a = f.sha512()
    a.update(x.encode())
    Ha = a.hexdigest()
    print(f'hash-sha512 : {Ha}')
else:
    print('you did\'nt select any option or data please try again')


