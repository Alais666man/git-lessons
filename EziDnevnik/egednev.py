def list_task():
    print('Вот твои задачи')
lt = list_task 
    
def add_task():
    print('Мало? Добавь ещё')
at = add_task 
    
def change_task():
    print('Подумай, а надо ли оно тебе?')
ct = change_task    

def end_task():
    print('Ну наконец-то')
et = end_task

def delete_task():
    print('Ну и правильно')
dt = delete_task   

def from_start_task():
    print('Что? Опять?!')
fst = from_start_task

def exit_task():
    print ('Свобода!')
ext = exit_task    

print("""
1. Список задач 
2. Добавить задачу 
3. Отредактировать задачу 
4. Завершить задачу 
5. Удалить задачу
6. Начать задачу с начала
7. Выход
""")
menu = True
while menu:
    menu = input('Выбирай мудро ')
    if menu == '1':
        lt()
    elif menu == '2':
        at()
    elif menu == '3':
        ct()
    elif menu == '4':
        et()
    elif menu == '5':
        dt()
    elif menu == '6':
        fst()    
    elif menu == '7':
        ext()
        break
    else:
        print('Неверная команда')
    
    
    
    
    
    
    
    
    
    
    
    
    


