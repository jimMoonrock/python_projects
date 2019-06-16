list_words, dict_words, new_list = [], {}, []
for line in open('task1.txt','r'):
    #new_list.append(line.replace('\n',''))
    list_words.append(line.replace('\n','').lower().replace(',','').replace('.',' '))

# new_list = ' '.join(new_list).split('.')
new_list = ' '.join([file.replace('\n','') for file in open('task1.txt', 'r')]).split('.')

for word in new_list:
    if word == '':
        new_list.remove(word)
print(new_list)


list_words = ' '.join(list_words).split(' ')

for word in list_words:
    if word == '':
        list_words.remove(word)

new_spl = ''.join([x[1:] if x.startswith(' ') else x for x in ' '.join(list_words).split('.')]).split(' ')

count_words = len(new_spl) // len(new_list)

for word in list_words:
    dict_words.update({word: list_words.count(word)})


for words,count in dict_words.items():
    if  str(count) in ['2','3','4']:
        print(f'Слово - {words} повторяется {count}: разa')
    else:
        print(f'Слово - {words} повторяется {count}: раз')

if len(list_words) >= 1:
    print(f'Среднее количество слов в предложении: {count_words}')


