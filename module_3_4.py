def single_root_words(root_word, *other_words):
  """
  Функция находит слова, однокоренные с заданным словом.

  Args:
    root_word: Корневое слово.
    *other_words: Произвольное количество слов для сравнения.

  Returns:
    Список однокоренных слов.
  """

  same_words = []
  root_word = root_word.lower()  # Приводим корневое слово к нижнему регистру

  for word in other_words:
    word = word.lower()  # Приводим сравниваемое слово к нижнему регистру
    if root_word in word or word in root_word:
      same_words.append(word)

  return same_words

# Примеры использования
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Вывод: ['Able', 'Disable']