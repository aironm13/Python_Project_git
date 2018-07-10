import jwt

# 给定一个key，也就是盐
key = 'secret'
# token由三部分组成，以点断开
token = jwt.encode({'payload':'abc123'}, key, 'HS256')
print(token)
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiYWJjMTIzIn0.lZc1PBGdbYDKq9k43tNTt1f0MHy4DjwT8NGTnHEIaVE'
print(jwt.decode(token, key, algorithms=['HS256']))
# {'payload': 'abc123'}

header, payload, signature = token.split(b'.')
print(header)
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
print(payload)
# b'eyJwYXlsb2FkIjoiYWJjMTIzIn0'
print(signature)
# b'lZc1PBGdbYDKq9k43tNTt1f0MHy4DjwT8NGTnHEIaVE'



import base64
def addeq(b:bytes):
    '''为base64编码补齐等号'''
    rem = len(b) % 4
    return b + b'=' * rem

print('header=', base64.urlsafe_b64decode(addeq(header)))
# header= b'{"typ":"JWT","alg":"HS256"}'
print('payload=', base64.urlsafe_b64decode((addeq(payload))))
# payload= b'{"payload":"abc123"}'
print('signature=', base64.urlsafe_b64decode(addeq(signature)))
# signature= b'\x95\x975<\x11\x9dm\x80\xca\xab\xd98\xde\xd3S\xb7W\xf40|\xb8\x0e<\x13\xf0\xd1\x93\x9cq\x08iQ'


# 根据jwt算法，重新生成签名
# 1，获取算法对象
from jwt import algorithms

alg = algorithms.get_default_algorithms()['HS256']
# key 为szecret： key = 'secret'
newkey = alg.prepare_key(key)

# 2，获取前两部分header payload
# 按照点分隔从右向左分隔三段
siginput, _, _ = token.rpartition(b'.')
print(siginput)
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiYWJjMTIzIn0'

# 3，使用key签名
signature = alg.sign(siginput, newkey)
print('=================')
print(signature)
# b'\x95\x975<\x11\x9dm\x80\xca\xab\xd98\xde\xd3S\xb7W\xf40|\xb8\x0e<\x13\xf0\xd1\x93\x9cq\x08iQ'
print(base64.urlsafe_b64encode(signature))
# b'lZc1PBGdbYDKq9k43tNTt1f0MHy4DjwT8NGTnHEIaVE='

import json
print(base64.urlsafe_b64encode(json.dumps({'payload':'abc123'}).encode()))
# b'eyJwYXlsb2FkIjogImFiYzEyMyJ9'