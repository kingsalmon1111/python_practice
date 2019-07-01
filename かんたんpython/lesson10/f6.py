import random

data = ['one', 'two', 'three', 'four', 'five']

random.shuffle(data)
print(data)
item = random.choice(data)
print(item)
res = random.sample(data, 3)
print(res)
