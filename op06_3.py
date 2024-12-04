import random

# Список имён
name_list = ["Авдей","Адам","Адриан","Аким","Александр","Алексей","Анатолий","Андрей","Анисим","Агата","Агафья","Аглая","Агнесса","Агния","Агриппина","Ада","Аделаида","Адиля"]

# которые будут отвечать на уроке
name_set = set()

# Обработка
while not len(name_set) == 5:
    elem = random.choice(name_list)
    name_set.add(elem)
    continue

print("5 уникальных имён, которые будут отвечать на уроке:")
print(name_set)