import re
from statistics import median

def main():
    dict_words, text = {}, ''

    with open('task1.txt') as file:
        text += file.read()

    # Medians
    list_with_text = re.split(r'[.?!]',text.replace('\n',''))
    for word in list_with_text:
        if word == '':
            list_with_text.remove(word)

    median_words = median([len(word.split()) for word in list_with_text])

    list_words = ' '.join(list_with_text).split(' ')
    for word in list_words:
        if word == '':
            list_words.remove(word)

    new_spl = ''.join([x[1:] if x.startswith(' ') else x for x in ' '.join(list_words).split('.')]).split(' ')

    count_words = float("{:0.2f}".format(len(new_spl) / len(list_with_text)))

    for word in list_words:
        dict_words.update({word: list_words.count(word)})

    for words,count in dict_words.items():
        if  str(count)[-1] in ['2','3','4']:
            print(f'Слово - {words} повторяется: {count} разa')
        else:
            print(f'Слово - {words} повторяется: {count} раз')

    if list_words:
        print(f'Среднее количество слов в предложении: {count_words}')

    print(f"Медианное количество слов в предложение: {median_words}")


if __name__ == '__main__':
    main()

