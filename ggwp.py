def cipher(str,key):
    encrypt_str=''
    for letter in str:
        encrypt_str += chr(ord(letter)^key)
    return encrypt_str
def read(name):
    file=open(name+'.txt', 'r')
    data_e=file.read().split('\n')
    data=cipher(data_e, key)
    for i in range(len(data)):
        if data[i]=='':
            del(data[i])
    return data
login=read('login')
login_enc=(cipher(login, 2))

