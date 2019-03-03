from fnv import *
data = 'my big fat data'
data = data.encode('utf-8')
hashcode1 = hash(data, algorithm=fnv_1a, bits=64) # uses fnv.fnv_1a algorithm
hashcode2 = hash(data, bits=64) # fnv.fnv_1a is a default algorithm
hashcode3 = hash(data, algorithm=fnv, bits=64)
print(hashcode1)
print(hashcode2)
print(hashcode3)

data = '.?'
data = data.encode('utf-8')
hashcode1 = hash(data, algorithm=fnv_1a, bits=64) # uses fnv.fnv_1a algorithm
hashcode2 = hash(data, bits=64) # fnv.fnv_1a is a default algorithm
hashcode3 = hash(data, algorithm=fnv, bits=64)
print(hashcode1)
print(hashcode2)
print(hashcode3)
