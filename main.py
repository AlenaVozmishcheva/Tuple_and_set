"""Создайте любым способом кортеж из следующих жанров
литературы:
Роман, Новелла, Фэнтези, Научная Фантастика.
И второй кортеж из чисел в следующем порядке:
3, 7, 9, 1, 6, 8, 2, 5, 4.
При помощи методов работы с кортежами проведите следующие
операции:
узнайте длину обоих кортежей (это количество элементов в них);
найдите максимальный и минимальный элемент;
просуммируйте элементы если это возможно;
отсортируйте элементы по возрастанию и убыванию в
результате сортировки и последующих операций необходимо
получить кортеж.
Помните что кортеж это неизменяемый тип данных, поэтому для
некоторых операций нужно создавать новый кортеж."""
from os import remove

genres_books = ('Роман', 'Новелла', 'Фэнтези', 'Научная Фантастика')
num_tuple = (3, 7, 9, 1, 6, 8, 2, 5, 4)

len_tuples_genres_book = len(genres_books)
print(f"Количество элементов в кортеже из жанров литературы: {len_tuples_genres_book}")

len_num_tuple = len(num_tuple)
print(f"Количество элементов в кортеже, состоящем из чисел: {len_num_tuple}")

max_element_genres_books = max(genres_books)
min_element_genres_books = min(genres_books)
print(f"Максимальный элемент кортежа : {max_element_genres_books}\nМинимальный элемент кортежа: {min_element_genres_books}")

max_element_num_tuple = max(num_tuple)
min_element_num_tuple = min(num_tuple)
print(f"Максимальный элемент кортежа : {max_element_num_tuple}\nМинимальный элемент кортежа: {min_element_num_tuple}")

import math
res = math.fsum(num_tuple)
print(f"Сумма всех элементов кортежа равна: {res}")

sort_down_genres_books = sorted(genres_books, reverse=True)
sort_down_genres_books_1 = tuple(sort_down_genres_books)
print(f"Кортеж в порядке убывания: {sort_down_genres_books_1}")

sort_up_genres_books = sorted(genres_books)
sort_up_genres_books_1 = tuple(sort_up_genres_books)
print(f"Кортеж в порядке возрастания: {sort_up_genres_books_1}")


sort_down_num_tuple = sorted(num_tuple, reverse=True)
sort_down_num_tuple_1 = tuple(sort_down_num_tuple)
print(f"Кортеж в порядке убывания: {sort_down_num_tuple_1}")

sort_up_num_tuple = sorted(num_tuple)
sort_up_num_tuple_1 = tuple(sort_up_num_tuple)
print(f"Кортеж в порядке возрастания: {sort_up_num_tuple_1}")


"""У вас есть кортеж из следующих жанров кино:
cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
Вам необходимо:
заменить жанр Экшн на Боевик
добавить жанр по вашему выбору между жанрами боевик, и
пеплум (я выбрал Фэнтези) вы можете выбрать что хотите.
Результат вывести в консоль
преобразовать полученный кортеж в строку. Результат вывести в
консоль"""

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

new_cinema_genres = list(cinema_genres)
new_cinema_genres[1] = "Боевик"
new_cinema_genres.insert(2,"Фэнтези")
new_cinema_genres = tuple(new_cinema_genres)
print(new_cinema_genres)

new_cinema_genres = ", ".join(new_cinema_genres)
print(new_cinema_genres)


"""Создайте любым способом множество из десяти вещей, которые вы
бы взяли на необитаемый остров. Спросите у кого-то из ваших
близких, какие вещи они взяли бы туда. Выведите на экран
множество вещей:
которые бы взяли вы двое;
которое взяли только вы;
которое возьмет ваш близкий человек;
вещи которые есть и у вас и у вашего близкого человека."""

my_things = {'вода', 'зажигалка', 'нож', 'палатка', 'фонарик', 'компас', 'спальный мешок', 'очки', 'книга', 'медикаменты'}
print(f"На необитаемый остров я бы взяла: {my_things}")

friend_things = {'нож', 'веревка', 'сигнальная ракета', 'аптечка', 'вода', 'спички', 'еда', 'палатка', 'сменная одежда', 'фонарик'}
print(f"Мой друг взял бы на необитаемый остров следующие вещи: {friend_things}")

our_things = my_things|friend_things
print(f"Вещи, которые мы возьмем вместе: {our_things}")

general_things = my_things.intersection(friend_things)
print(f"Вещи, которые есть и у меня, и у друга: {general_things}")

my_exclusive_things = my_things.difference(friend_things)
print(f"Вещи, которые будут только у меня: {my_exclusive_things}")

friend_exclusive_things = friend_things.difference(my_things)
print(f"Вещи, которые будут только у друга: {friend_exclusive_things}")



"""У вас есть список:
cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия",
"пеплум"]
Вам необходимо:
преобразовать данный список в множество;
добавить 2 жанра на ваш выбор (то что вы захотите);
удалить какой-то из жанров по вашему выбору;
удалить некий случайный жанр;
преобразовать множество обратно в список."""

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]
cinema_genres_set = set(cinema_genres)
print(cinema_genres_set)

cinema_genres_set.update(["боевик", "мелодрама"])
print(cinema_genres_set)

cinema_genres_set.remove("пеплум")
print(cinema_genres_set)

cinema_genres_set.pop()
print(cinema_genres_set)

cinema_genres_list = list(cinema_genres_set)
print(cinema_genres_list)

