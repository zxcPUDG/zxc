# for x in range(10):
#     print('You are welcome!')
# i=int(input('введите число повторений: '))
# for z in range(i):
#     print('Silence is golden')
# sr=int(input('сколько строк?: '))
# for f in range(sr):
#     print('00000')
# i=-1
# p=0
# for l in range(0,13):
#     i=i+2
#     p=p+2
#     print(i,'первый')
#     print(p, 'второй')
# print(p , 'расчет окончен')
# from random import choice
# ans = ['может быть да','категорически нет','да','возможно нет','вроде верно']
# while True :
#     que=input('задайте вопрос магическому шару: ')
#     choice(ans)
#     print(choice(ans))
#     with open('magic_ball.txt','a')as file:
#         file.write(que+':'+choice(ans)+'\n')   
def plus(a,b):
    c=a+b
    print('результат суммирования: ', c)
def minus(a,b):
    c=a-b
    print('результат вычетания: ', c)
def multiply(a,b):
    c=a*b
    print('результат умножения: ', c)
def divide(a,b):
    c=a/b
    print('результат деления: ', c)

while True:
    a=int(input('введите первое число: '))   
    w=input('какое действие?( +,-,*,/ ): ')
    b=int(input('введите второе число: ')) 
    if w=='+':
        plus(a,b)
    elif w=='-':
        minus(a,b)
    elif w=='*':
        multiply(a,b)
    elif w=='/':
        divide(a,b)