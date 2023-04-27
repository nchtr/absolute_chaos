#1 выводится конкретно все возможные комбинации
from itertools import product, chain
s = input()
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1

combinations = chain.from_iterable(product(char_count.keys(), repeat=i) for i in range(1, len(s) + 1))

words = set()
for combo in combinations:
    if all(combo.count(char) <= char_count[char] for char in combo):
        words.add(''.join(combo))

for word in sorted(words, key=len):
    print(word, end=' ')
print('\nКоличество слов:', len(words))
