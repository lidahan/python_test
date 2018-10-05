# -*- coding: utf-8 -*-

import hashlib,random

md5=hashlib.md5()
md5.update('how to use hashlib'.encode('utf-8'))
print(md5.hexdigest())


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
	if user in db:
		md5=hashlib.md5()
		md5.update(password.encode('utf-8'))
		print(md5.hexdigest())
		if db[user]==md5.hexdigest():
			return	True
		else:
			return False

if login('michael', '123456'):
	print('Pass')
else:
	print('Fail')

if login('bob', 'abc999'):
	print('Pass')
else:
	print('Fail')

if login('alice', 'alice2008'):
	print('Pass')
else:
	print('Fail')

if login('michael', '1234567'):
	print('Pass')
else:
	print('Fail')
if login('bob', '123456'):
	print('Pass')
else:
	print('Fail')
if login('alice', 'Alice2008'):
	print('Pass')
else:
	print('Fail')

def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
	def __init__(self,username,password):
		self.username=username
		self.salt=''.join([chr(random.randint(48,122)) for i in range(20)])
		self.password=get_md5(password+self.salt)

		