k = {}

def table(funk):
    def wrapper():
        funk()
        global k
        k = list(k)
        k.sort()
        print(" ", "_"*len(str(k[-1])), " ", "_"*7, "_"*8)
        for i in range(len(k)):
            print("|", str(k[i]).ljust(len((k[-1])), " "),"|", "кратное 3".ljust(11," ") if k[i] % 3== 0 else "не кратное 3".ljust(11, " "),
                  "|", "парное".ljust(8, " ") if k[i] % 2 == 0 else "не парное".ljust(8," "), "|")
            print("|", " " * len(str(k[-1])), "|", "_" * 8, "|")
    return wrapper

@table
def numbers():
    import random
    x = int(input("Введите число :"))
    n = set(random.randint(1, 1000) for i in range(x))
    global k
    k = n


# def my_shiny_new_decorator(function_to_decorate):
#      # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#      # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate() # Сама функция
#         print("А я - код, срабатывающий после")
#     # Вернём эту функцию
#     return the_wrapper_around_the_original_function
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
# stand_alone_function()
# #Я простая одинокая функция, ты ведь не посмеешь меня изменять?
# # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# # готовую к использованию функцию:
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()
# # Я - код, который отработает до вызова функции
# # Я простая одинокая функция, ты ведь не посмеешь меня изменять?
# # А я - код, срабатывающий после