import re
def main():
    list_words, dict_words, new_list = [], {}, []

    for line in open('task1.txt'):
        list_words.append(line.replace('\n','').lower().replace(',','').replace('.',' '))

    new_list = re.split(r'[.?!]', ' '.join([file.replace('\n','') for file in open('task1.txt')]))

    for word in new_list:
        if word == '':
            new_list.remove(word)

    list_words = ' '.join(list_words).split(' ')

    for word in list_words:
        if word == '':
            list_words.remove(word)

    new_spl = ''.join([x[1:] if x.startswith(' ') else x for x in ' '.join(list_words).split('.')]).split(' ')

    count_words = float("{:0.2f}".format(len(new_spl) / len(new_list)))

    for word in list_words:
        dict_words.update({word: list_words.count(word)})

    for words,count in dict_words.items():
        if  str(count) in ['2','3','4']:
            print(f'Слово - {words} повторяется: {count} разa')
        else:
            print(f'Слово - {words} повторяется: {count} раз')

    if list_words:
        print(f'Среднее количество слов в предложении: {count_words}')


if __name__ == '__main__':
    main()
