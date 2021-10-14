####################################################################
# SUMMARY
####################################################################
# Это мой проект приложения курсовой работы (декабрь 2021 года).
# В планах создать программу, которая сможет по входному тексту
# определить его эмоциональную окраску, по шкале -2, -1, 0, 1, 2
# (отрицательная, негативная, нейтральная, положительная, доброжелательная).
# Предположительно буду пытаться реализовывать наивный байесовский
# классификатор самостоятельно, подготавливая исходный текст с
# помощью библиотеки NLTK.
####################################################################
import string

from nltk import sent_tokenize, word_tokenize, download
from nltk.corpus import stopwords

# ПРИМЕЧАНИЕ! При копировании текста из excel-файла LinisCrowd text rating final
# в txt файл читаются кракозябры. Из-за кодировки UTF-8. Необходимо либо вручную
# пересохранять txt с кодировкой ANSI, либо найти программное решение

# открытие файла с входным текстом для чтения
input_text_file = open('input_text.txt', 'r')

# чтение текста из файла (получаем строку)
input_text = input_text_file.read()

# закрытие файла
input_text_file.close()

#########
# Разбиение текста на предложения
#########
# sentence_tokenize_text = sent_tokenize(input_text)
#
# # ВНИМАНИЕ! здесь опять может быть проблема с кодировкой!!!
# # запись текста разбитого по предложениям в ткст файл.
# # одна строка одно предложение
# sent_tok_text_output_file = open('sentence_tokenize_text_output.txt', 'w')
# for i in sentence_tokenize_text:
#     sent_tok_text_output_file.write(i + '\n')
# sent_tok_text_output_file.close()

#########
# Разбиение входного текста на слова
#########
word_tokenize_text = word_tokenize(input_text)

# приведение к нижнему регистру всех слов
for i in range(0, len(word_tokenize_text)):
    word_tokenize_text[i] = word_tokenize_text[i].lower()

# Очистка от стоп-слов
stop_words = set(stopwords.words('russian'))
# ОБРАТИТЬ ВНИМАНИЕ НА ТО ЧТО СТОП-СЛОВА В НИЖНЕМ РЕГИСТРЕ!
word_tokenize_text_wout_stop_words = [word for word in word_tokenize_text if not word in stop_words]

# Очистка от знаков препинания
signs = '.,?!\"\';:[]{}\|/><-_–=+*&^%$`'
signs_set = set(signs)
# print(signs_set)
word_tok_text_wout_stop_words_punkt = [word for word in word_tokenize_text_wout_stop_words if not word in signs_set]


# Вывод без стоп слов и пунктуации
# ВНИМАНИЕ! здесь опять может быть проблема с кодировкой!!!
word_tok_text_wout_stop_words_punkt_output_file = open('word_tokenize_text_wout_stop_words_punkt_output.txt', 'w')
for i in word_tok_text_wout_stop_words_punkt:
    word_tok_text_wout_stop_words_punkt_output_file.write(i + '\n')
word_tok_text_wout_stop_words_punkt_output_file.close()


# # Вывод без стоп слов
# # ВНИМАНИЕ! здесь опять может быть проблема с кодировкой!!!
# word_tok_text_wout_stop_words_output_file = open('word_tokenize_text_wout_stop_words_output.txt', 'w')
# for i in word_tokenize_text_wout_stop_words:
#     word_tok_text_wout_stop_words_output_file.write(i + '\n')
# word_tok_text_wout_stop_words_output_file.close()


# # ВНИМАНИЕ! здесь опять может быть проблема с кодировкой!!!
# # Запись текста разбитого по словам в ткст файл.
# # Одна строка одно слово
# word_tok_text_output_file = open('word_tokenize_text_output.txt', 'w')
# for i in word_tokenize_text:
#     word_tok_text_output_file.write(i + '\n')
# word_tok_text_output_file.close()

# print(input_text)
# print('\n', type(input_text))
