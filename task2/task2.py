''''''
''' Использую yield для того чтобы прибвать значения в бесконечном цикле'''
def random_step(n):
    score = 0
    while True:
        increment = yield score
        if increment is not None:
            score = increment
        else:
            score += n

r = random_step(5)
print(next(r)) # 0
print(r.send(60)) # 60
print(next(r)) # None = 60 + 5 (score + n потому что это None)
print(r.send(123)) # 123
print(next(r)) # None = 123 + 5 (score + n потому что это None)
print(next(r)) # None = 128 + 5 (score + n потому что это None)
print(next(r)) # None = 133 + 5 (score + n потому что это None)
