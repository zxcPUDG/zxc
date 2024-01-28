# Hello=2
# world=3
# print(Hello,world,'Hello world')
# str()   #'qefqefqfqfqfq'
# int()   #2 4 6
# float() #2.3
# list() #['21','25','15']

# list=['44','21','62']
# list[0]=int(list[0])
# list[2]=int(list[2])
# print(list[0]+list[2], '+')
# print(list[0]-list[2], '-')
# print(list[0]*list[2], '*')
# print(list[0]/list[2], '/') 

# if 15>=20:
# 	print('true')
# else:
# 	print('false')
# print('do you like play on pudge???')
# cart=[]
# eggs=True
# sweet=False
# bread=True
# if bread==True:
# 	cart.append('bread')
# #print(cart)
# if eggs==True:
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
#     cart.append('eggs')
# if sweet==True:
# 	cart.append('sweet')
# 	cart.append('sweet')
# 	cart.append('sweet')
# 	cart.append('sweet')
# 	cart.append('sweet')
# print(cart)	

# login=['shadow fiend' ,'pudge' ,'zxc']
# password=['ezmid','my dick is big','igra proebana opyat(']
# your_login=input('login:')
# if your_login==login[0]:
# 	your_password=input('password:')
# 	if your_password==password[0]:
# 		print('success')
# 	else:
# 		print('password incorrect')
# else:
# 	print('login incorrect')

# if your_login==login[1]:
# 	your_password=input('password:')
# 	if your_password==password[1]:
# 		print('success')
# 	else:
# 		print('password incorrect')
# else:
# 	print('login incorrect')

# if your_login==login[2]:
# 	your_password=input('password:')
# 	if your_password==password[2]:
# 		print('success')
# 	else:
# 		print('password incorrect')
# else:
# 	print('login incorrect')
# 	#123adel
# 2.1 практикум
# week=['saturday','sanday']
# week1=['monday','tuesday','wendsay','friday']
# today=input('what day of the week is today?')
# if today==week1[0]:
# 	print('study study study')
# elif today==week1[1]:
# 	print('study study study')
# elif today==week1[2]:
# 	print('study study study')
# elif today==week1[3]:
# 	print('study study study')
# elif today==week[0]:
# 	print('party')
# else:
# 	print('have a rest')
#qwe
# x=int(input('какая температура ?'))
# if x < 10 :
# 	print('ПРОХЛАДНО')
# elif x < 30:
# 	print('ТЕПЛО')
# elif x >= 30:
# 	print('ЖАРКО')
# login=['shadow fiend' ,'pudge' ,'zxc']
# password=['ezmid','123zxc','qwe']
# your_login=input('login:')
# your_password=input('password:')
# i=2
# while i>=0:
#     if your_login==login[i]:
#         if your_password==password[i]:
#             print('success')
#     i=i-1


# login=['shadow fiend' ,'pudge' ,'zxc']
# password=['ezmid','123zxc','qwe']
# your_login=input('login:')
# your_password=input('password:')
# for i in range(3):
#     if your_login==login[i]:
#         if your_password==password[i]:
#             print('success')

# login=['shadow fiend' ,'pudge' ,'zxc']
# password=['ezmid','123zxc','qwe']
# your_login=input('login:')
# your_password=input('password:')
# i=2
# while i>=0:
#     if your_login==login[i]:
#         if your_password==password[i]:
#             print('success')
#     i=i-1
#     if i<0:
#         break
#     print(i)
# else:
#     print('ghost hz')


# login=['shadow fiend' ,'pudge' ,'zxc']
# password=['ezmid','123zxc','qwe']
# your_login=input('login:')
# your_password=input('password:')
# i=2
# while i>=0:
#     if your_login==login[i]:
#         if your_password==password[i]:
#             print('success')
#     i=i-1
#     print(i)
# else:
#     print('ghost of kiev is kall ')

# def login_c():
#     n_login=input('new login: ')
#     login[i]=n_login
#     print(login, i)
#     print('login has been changed')
#     file=open(name+'.txt','w')
#     for i in login:
#         file.write(i+'\n')

# file=open('text.txt','w')
# file.write('zxc\n')
# file.write('qwe\n')
# file.write('mid\n')
# file.write('ezgg\n')
# file.write('ggwp\n')
# file.write('pudge\n')
# file.close()
# file=open('text.txt','r')
# data=file.read().split('\n')
# for i in range(len(data)):
#     if data[i] == '':
#         del(data[i])
# print(data)
# file=open('login.txt','w')
# file.write('zxc\n')
# file.write('qwe\n')
# file.write('mid\n')
# file.write('ezgg\n')
# file.write('ggwp\n')
# file.write('pudge\n')
# file.close()
# file=open('password.txt','w')
# file.write('zxc\n')
# file.write('qwe\n')
# file.write('mid\n')
# file.write('ezgg\n')
# file.write('ggwp\n')
# file.write('pudge\n')
# file.close()
def signup():
    login_temp=input('reg your login: ')
    password_temp=input('reg your password: ')
    login.append(login_temp)
    password.append(password_temp)
    write('login',login)
    write('password',password)
    print('success')
def password_changer():
    new_password=input('new password: ')
    password[i]=new_password
    print('password has been changed')
    return password
def write(name, lists):
    file=open(name+'.txt', 'w')
    for k in lists:
        file.write(k+'\n')
def read(name):
    file=open(name+'.txt', 'r')
    data=file.read().split('\n')
    for i in range(len(data)):
        if data[i]=='':
            del(data[i])
    return data
login=read('login')
password=read('password')
while True:
    cmd=input('signup to reg new account  or signin to signin your account: ')
    if cmd=='signin':
        your_login=input('input login: ')
        your_password=input('input password: ')
        for i in range(len(login)):
            if your_login==login[i]:
                if your_password==password[i]:
                    exit=False
                    while exit==False:
                        cmd=input('logout to logout or change password to change password: ')
                        if cmd=='change password':
                            password=password_changer()
                        elif cmd=='logout':
                            exit=True
                        else:
                            print('invalid command')
                    else:
                        break
    elif cmd=='signup':
        signup()