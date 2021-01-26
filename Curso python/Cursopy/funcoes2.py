# def func1():
#  var='Ola lucas'
#  return var
# def func2(va2):
#
#  va2= func1()
#  return va2
# va2 = func1()
# print(va2)

def func(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)
def fun1():
    nome = input("digite sseu nome")
    return  f'Oi{ nome }'
def fun2():
    sobrenome = input("digite sseu nome")
    return  f'Bom dia {fun1()} {sobrenome}'
exe = func(fun1)
exe2 = func(fun2)
print(exe)
print(exe2)