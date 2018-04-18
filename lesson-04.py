"""
Урок №2. Функции, область видимости и время жизни переменной
1. Пользовательские функции
"""
#Функция - это блок кода, который можно вызывать многократно

def hello ():
    print('Hello!')     # Объявление функции
    
print(type(hello))
hello()  # Вызов функции

say_hello = hello # Присвоить ссылку на функцию
say_hello()


# Передча значений аргументов по ссылке
def parse(src, output):
    src = src.strip('.')
    
    for i in src.split():   # split - разделение строки 
        output.append(i)

src = 'Python is programming language.'
output = []

print(src, output)
parse(src, output)
print(src, output)


# Аргументы функции
def hello_username(name):  # name -аргумент.Понятное имя, демонстрирующее его функцию (внутри функции становится переменной)
    print('Hello,', name)


hello_username('Python')
hello_username('JavaScript')
hello_username('Вася')
    
def summa(a, b):   #Аргументов должно быть минимум. Обязательные аргументы. Максимум 4.
    print(a + b) # Аргумент по-умолчанию - аргумент с уже заданным значением
summa(1, 3)    

def poww(x, p=2):   # p=2 не обязательный аргумент со значением по умолчанию (Всегда идут последними)
    print(x ** p)   # Значения по умолчанию всегда неизменяемого типа
poww(5)    
poww(2, 3)



def f(i, l=None):
    #l = l if i is not None else []
    l = l or [] # Переданный элемент приводится к True (Только для аргументов изменяемого типа)


# Как вернуть значение из функции?

def minus(a, b):
    return a - b    # Возвращает результат
    a = a * b # Не выполняется после return
    
r = minus(1,2)
print(r)



#if connect ():
    #if select.bd():
        #if quevy()
        #'or'
        #else:
            #'error'
    #else:
        #'error'
#else:
    #'error'
    



#if not connetc():
    #'error' // return
#if not select.bd():
    #'error'// return
#if not quevy():
    #'error' // return

#'ok'


#Лучше всё всегда проверять на False!!!!


#Функция, котороя ничего не возвращает является процедурой


def f2():
    return 1, 2, 3   # Такая функция возвращает кортеж 
a, b, c = f2()   # Распаковать кортеж


# Переменное количество аргументов в функции

def demo_func(i, *args, **kwargs):
    """
    args - кортеж (распологается в конце)
    j - именованный аргумент
    kwargs - словарь
    i - аргумент с позицией
    """
    print(i, args, type(args))
    print(kwargs, type(kwargs))

demo_func(1, 2, 3 , j=4)
demo_func('10', '20', k=True, e=456)

def f3(i, *args, j=1, **kwargs):
    print(i, j, args)
f3(2, 5, 5, j=2)


# Переменное количество аргументов при вызове функции

def f4(i,j,k, a=None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a': 10,
    'b': 20,
    'c': 30,
    }
f4(*args, **kwargs)



# Анонианя функция - функция, у которой нет имени (lambda - функция). Работает быстрее def. Всегда возвращает результат


sqrt = lambda x: x ** 0.5
# lambda: pass
#lambda x, y: pass
print(sqrt(9))


# Замыкания (когда внутри функции описывается другая функция)

def trim(chars=None):
    # Локальная область видимости функции trim
    # Замкнутая область
    def f(s):
        # Локальная область видимости функции f
        return s.strip(chars)
    return f

spaces_trim = trim() #Вызов функции trim, создание лок. области trim
slashes_trim = trim('/\\')
print(spaces_trim('     Hello      '))
print(slashes_trim('//////url\\\\\\\\\\\////'))




#глобальная область видимости - все переменные вне функции
#локальная область видимости - область функции. Обращение только внутри функции



# Рекурсивная функция - когда в одной функции вызывается та же функция
# 5! = 1 *2 * 3 * 4 * 5
def factorial(x):
    # Прямая рекурсия
    return 1 if x == 0 else x * factorial (x -1)
print(factorial(5))


# Косвенная рекурсия
#def a():
    #b()
        
#def b():
    #a()
#print(a())   




#g = 666
#def wrapper():
    #external = 777
    
    #def func():
        #global g
        #nonlocal external
        
        #g += 1
        #external += 1
        
     #func()
     
     #print(g, external)
     
#wrapper()











