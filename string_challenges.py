# Вывести последнюю букву в слове
word = 'Архангельск'
print("ЗАДАНИЕ 1: ",word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word=word.lower()
count=0
for letter in word:
    if letter == 'а':
        count+=1
print(f'ЗАДАНИЕ 2: Буква "a" в слове {word} встречается {count} раза')


# Вывести количество гласных букв в слове
word = 'Архангельск'
letter_vowel="А, Е, Ё, И, О, У, Ы, Э, Ю, Я"
count = 0
word=word.upper()
for letter in word:
    if letter in letter_vowel:
        count+=1
print("ЗАДАНИЕ 3: Гласных букв в слове ", count)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = len(sentence.split())
print("ЗАДАНИЕ 4: Кол-во слов в предложении: ", sentence)



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print('ЗАДАНИЕ 5:')
for letter in sentence:
    print(letter[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
count=0
for lenword in sentence:
    count+=len(lenword)
avrg= int(count/len(sentence))
print(f'ЗАДАНИЕ 6: Средняя длина слов - {avrg}')