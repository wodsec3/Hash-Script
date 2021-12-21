import hashlib as s

print('''
 _   _           _       ____            _       _
| | | | __ _ ___| |__   / ___|  ___ _ __(_)_ __ | |_
| |_| |/ _` / __| '_ \  \___ \ / __| '__| | '_ \| __|
|  _  | (_| \__ \ | | |  ___) | (__| |  | | |_) | |_
|_| |_|\__,_|___/_| |_| |____/ \___|_|  |_| .__/ \__|
                                          |_|
                                          ''')
#input from user and encode message . .
m=input('Give me message to Hash: ');m=m.encode()

#Set hash objects . .
s1=s.sha1(m)
s2=s.sha224(m)
s3=s.sha256(m)
s4=s.sha384(m)
s5=s.sha3_224(m)
s6=s.sha3_256(m)
s7=s.sha3_384(m)
s8=s.sha3_512(m)
s9=s.sha512(m)

#Print hash . .
print('SHA1:      %s'%(s1.hexdigest()))
print('SHA224:    %s'%(s2.hexdigest()))
print('SHA256:    %s'%(s3.hexdigest()))
print('SHA384:    %s'%(s4.hexdigest()))
print('SHA3_224:  %s'%(s5.hexdigest()))
print('SHA3_256:  %s'%(s6.hexdigest()))
print('SHA3_384:  %s'%(s7.hexdigest()))
print('SHA3_512:  %s'%(s8.hexdigest()))
print('SHA512:    %s'%(s9.hexdigest()))







