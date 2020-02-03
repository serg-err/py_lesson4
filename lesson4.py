'''
Напишите функцию (F):
на вход список имен и целое число N;
на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения:
количество имен 20, N = 100,
рекомендуется использовать функцию random);
'''
import random
list = ['Дима','Коля','Оля','Саша','Петя','Толя','Игорь','Люда','Владимир','Ярослав','Володя']
lengh = []
name = []
random_choice_name = []
def f(n):
    for i in range(1, n+1):
        random_choice_name.append(random.choice(list))
        lengh.append(len(random_choice_name[i-1]))
    print(random_choice_name)
    print(lengh)
f(100)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
dict = {}

def list_sorted():
    for word1 in random_choice_name:
        kolvo = 0
        for word2 in random_choice_name:
            if word1 == word2:
                kolvo = kolvo + 1
            else:
                continue
        dict[word1] = kolvo
    for k in sorted(dict, key=dict.get, reverse=True):
        print('Самое частое имя из списка - ', k)
        break


list_sorted()

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
dict2 = {}
letter = []
def seldom_letter():
    for i in random_choice_name:
        letter.append(i[0])
    for word1 in letter:
        kolvo = 0
        for word2 in letter:
            if word1 == word2:
                kolvo = kolvo + 1
            else:
                continue
        dict2[word1] = kolvo
    for k in sorted(dict2, key=dict2.get):
        print('Самая редкая буква из списка - ', k)
        break

seldom_letter()