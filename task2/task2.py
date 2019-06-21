''''''
''' Использую yield для того чтобы прибвать значения в бесконечном цикле'''
def random_step(n):
    score = 0
    while True:
        increment = yield score
        if increment is not None:
            score += increment
        else:
            score += n

r = random_step(5)
print(next(r))
# print(r.send(10))
print(next(r))
# print(r.send(15))
print(next(r))
print(next(r))
print(next(r))

