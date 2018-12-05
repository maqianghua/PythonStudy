#coding=utf-8
# lyric = 'The night begin to shine, the night begin to shine'
# words=lyric.split()
#
# print words
import string
path='Walden.txt'
with open(path, 'r') as text:
    words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index=set(words)
    count_dict={index:words.count(index) for index in words_index}
for word in sorted(count_dict, key=lambda x: count_dict[x], reverse=True):
    print ('{} --{} times'.format(word, count_dict[word]))

# with open(path, 'r') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print ('{}-{} times'.format(word, words.count(word)))
