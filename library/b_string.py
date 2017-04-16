# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

"""
Created on 15.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

# ==============================================================================
# СТРОКИ
# ==============================================================================

a = "couldn\"t"  # экранирование символов
print(a)
# couldn"t

b = """multi line
very long
string constant"""
print(b)
# multi line
# very long
# string constant

c = 'multi line\nvery long\nstring constant'
print(c)
# multi line
# very long
# string constant

d = 'this takes \
two lines'
print(d)  # this takes two lines

# форматирование с помощью символа %
print('%(language)s has %(number)03d quote types.' %
      {"language": "Python", "number": 2})  # Python has 002 quote types.


# Строки можно склеивать оператором + и «размножать» оператором *
# ---------------------------------------------------------------

e = "Hello " + "word"
print(e)  # Hello word

f = "Hello " * 3
print(f)  # Hello Hello Hello


# x = "Hello " / 2
# print(x)
# error - деление строк запрещено !

# ==============================================================================
# ОПЕРАТОР СРЕЗА и ИЗЬЯТИЕ СИМВОЛА ПО ИНДЕКСУ
# ==============================================================================

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


# Cтрока - это последовательность символов с произвольным доступом
# ----------------------------------------------------------------

str = "Hello, cruel world!"
print(len(str))  # 19

str[0]  # H
str[1]  # e

# только первый символ
print(str[:1], str[0])  # H H

# только 4 символ строки
print(str[3])  # l

# все кроме первого
print(str[1:])  # ello, cruel world!

# все кроме последнего
print(str[:-1])  # Hello, cruel world

# все кроме первого и последнего
print(str[1:-1])  # ello, cruel world

# все символы с 8 по 14 но не включая 14
print(str[7:14])  # cruel w

# каждый второй символ со 2 по 13
print(str[1:12:2])  # 'el,cul'

# каждый второй символ строки, обратите внимание, что первый символ
# в этом случае выведется тоже т.к. он считается равным нулю
print(str[::2])  # 'Hlo re ol!'


# Note! частный случай, вернёт реверсивную последовательность,
# также как и метод reverse()
print(str[::-1])  # !dlrow leurc ,olleH

# каждый второй символ, исключая первый
print(str[1::2])  # 'el,culwrd'

# первый и каждый четвёртый до конца строки
print(str[::4], str[0::4])  # Hor l Hor l

# только последний и предпоследний
print(str[-1], str[-2])  # ! d

# все кроме последних двух
print(str[:-2])  # Hello, cruel worl

# последние два
print(str[-2:])  # d!


# Примеры из Станфордского университета
# -------------------------------------

s = 'Hello'
print(len(s))  # 5

# Буквы и символны начинаються с нуля (0)

s[0]  # 'H'
s[1]  # 'e'
s[4]  # 'o'  -- последний элемент это length - 1 или len(s) - 1
# s[5]  # ERROR, index out of bounds
  

s = 'Hello'
t = 'Hello' + ' hi!'  # t is 'Hello hi!'

# String Slices - позитивный срез по индексу
# ------------------------------------------

s = 'Hello'

# 01234 # Демонстрация индексов в 'Hello'

s[1:4]  # 'ell' - starting at 1, up to but not including 4
s[0:2]  # 'He'
s[:2]  # 'He', omit first number uses start of string
s[2:]  # 'llo', omit second number uses end of string


# Компановка новой строки из переменных
# -------------------------------------

a = 'Hi!'
b = 'Hello'

# Новая строка 'c' содержит первые 2 символа из 'a' и последние 2 символа из 'c'
c = a[:2] + b[len(b) - 2:]
print(c)  # Hilo


# Negative Index - отрицательные индексы
# --------------------------------------

s = 'Hello'
# -54321  # negative index numbers

s[-2:]  # 'lo', срез первых 2-х символов с конца
s[:-3]  # 'He', срез 3-символов с начала строки

# Python String Loops - Петли (Цикл) по строкам
# ---------------------------------------------

# Один из способов перебрать строку - использовать функцию xrange(x),
# которая задает число, например. 5, возвращает последовательность
# 0, 1, 2, 3 ... n-1. Эти значения отлично работают для индексации строк,
# поэтому цикл для i в диапазоне (len (s)): будет циклически перебрасывать
# переменную i через значения индекса 0, 1, 2, ... len (s) -1,
# по существу Глядя на каждый символ один раз.

s = 'Hello'
result = ''
result2 = ''
for i in range(len(s)):
    # Работеам s[i], в примере добавляем каждое значение в переменную result
    result += s[i]
    print(result)

    # 1  H
    # 2  He
    # 3  Hel
    # 4  Hell
    # 5  Hello

    # Поскольку у нас есть номер индекса, i, каждый раз по циклу, легко написать
    # логику, которая вставляет символы рядом с i, например. Символ слева в i-1.

    result2 += s[i - 1]
    print(result2)

    # 1  o
    # 2  oH
    # 3  oHe
    # 4  oHel
    # 5  oHell

# Другой способ это ссылаться на каждый символ в строке в цикле for:

s = 'Hello'
result = ''

for x in s:  # x будет последовательно вывовдить 'H', затем 'e', ​​... и т.д.
    result += x

    # 0  H
    # 1  He
    # 2  Hel
    # 3  Hell
    # 4  Hello

# Эта форма представляет собой простой способ обработать каждый символ в
# строке, хотя в нем отсутствует некоторая гибкость формы i / range () выше.

# Python Strings Code Example - Пример работы со строками в Python
# ----------------------------------------------------------------

# Функция with_no () принимает строку и возвращает новую
# Строка с надписью «No:» спереди.


def with_no(s):
    return "No: " + s

print(with_no('Some string'))  # No: Some string

# Функция two_e() возвращает True если строка содержит два символа 'e'.
# Цикл для каждого for x in str: является стандартным, в нём каждый символ
# строки проходит свою итерацию


def two_e(s):
    count = 0
    for x in s:  # последовательный обход по каждому символу в строке
        if x == 'e':  # если символ равен 'e'
            count += 1  # присваеваем счётчику еденицу

    # это условие if/else может быть записано, как
    # "return (count == 3)"
    if count == 3:
        return True
    else:
        return False

print(two_e('Some Awesome'))  # True

# ==============================================================================
# UNICODE
# ==============================================================================

uni = "Тест"
print(uni)
# '\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'

uni1 = u"Тест"  # или uni1 = unicode("Тест", "UTF-8")
print(uni1)
# u'\u0422\u0435\u0441\u0442'


# добавим оператор 'r'
uni3 = ur'Hello\u0020World !'  # u'Hello World !'
print(uni3)

uni4 = ur'Hello\\u0020World !'  # u'Hello\\u0020World !'
print(uni4)


# Преобразуем строку в unicode методом decode
# -------------------------------------------

# uni2 = uni.decode("utf8")
# print(uni2)
# u'\u0422\u0435\u0441\u0442'

# Для обратного преобразования служит метод encode
# ------------------------------------------------

# uni3 = uni2.encode("utf8")
# print(uni3)
# '\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'

# ==============================================================================
# СТРОКОВЫЕ МЕТОДЫ
# https://docs.python.org/2.7/library/stdtypes.html#string-methods
# ==============================================================================

s = 'String'
ls = 'Very long string'

print(ls.count('n'))  # 3

f = "The sum of 1 + 2 is {0} {1}".format(1+2, ls)
print(f)  # The sum of 1 + 2 is 3 Very long string
# https://docs.python.org/2.7/library/string.html#formatstrings

print(s.index('g'))  # 5 - вернёт номер индекса

# s = "-";
# seq = ("a", "b", "c"); # This is sequence of strings.
# print s.join( seq )

ls = 'Very long string'
print(' '.join(ls))  # V e r y   l o n g   s t r i n g

sl = ['Very long string', 'Very long string', 'Very long string']
result = ' '.join(sl)
print(result)  # Very long string Very long string Very long string


# strip, lstrip, rstrip
# ---------------------

# удаляет пробелы или символы
ls = '     STRIP     '
lsp = ls.strip()  # STRIP
print('www.example.com'.strip('cmowz.'))  # example

# удаляет символы слева, если пусто, то убирает пустые пробелы
ls = '     Very long string     '
lsp = ls.lstrip()
print(lsp)  # Very long string.....

# ls.rstrip() - удаляет справа

ls = '!!!     Very long string     !!!'
lsp = ls.lstrip('!')
print(lsp)  # .    Very long string     !!!

print(ls.partition('lo'))
# (u'!!!     Very ', u'lo', u'ng string     !!!')

ls = '     Very long string     !!!'
lsp = ls.replace('     ', '...')
print(lsp)  # ...Very long string...!!!


# split - возвращает список с разбиением строк на элементы
# -----

ls = '     Very long string     !!!'
lsp = ls.split()
print(lsp)  # [u'Very', u'long', u'string', u'!!!']

ls = 'Very,,, long, string!!!'
lsp = ls.split(',')  # включая символ ','
print(lsp)  # [u'Very', u'', u'', u' long', u' string!!!']

print('1<>2<>3'.split('<>'))  # [u'1', u'2', u'3']

print('Two lines\n'.split('\n'))  # [u'Two lines', u''] - частный случай

# splitlines - удаляет спецсимволы "\r", "\n", and "\r\n"
# ----------

ls = 'abc \n\n de fg \r kl \r\n'
lsp = ls.splitlines()
print(lsp)  # [u'abc ', u'', u' de fg ', u' kl ']

print("One \n line".splitlines())  # [u'One ', u' line']
print("One line\n".splitlines())  # [u'One line'] - частный случий

# strip + split
# -------------

ls = 'Z  ,   Very long string     !!!'
lsp = (ls.strip()).split()  # Удалим пробелы и вернём список
print(lsp)  # [u'Z', u',', u'Very', u'long', u'string', u'!!!']
