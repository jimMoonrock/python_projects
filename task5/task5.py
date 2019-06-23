''''''
'''
написать функцию, которая принимает список и возвращает значение, которое встречается чаще всех в списке.

import collections
def count_value(l):
    d, max = {}, 0
    for num in l:
        d.update({num:l.count(num)})
        if d[num] > max:
            max = num
    return max
print(count_value([2, 3, 4, 3, 5, 3, 4, 4, 4, 4]))
'''
import collections
def count_num(l):
    return collections.Counter(l).most_common(1)[0][0]
print(count_num([2, 3, 4, 3, 5, 3, 4, 4, 4, 4]))
