from collections import Counter

myList = [1, 1, 3, 2, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

print(Counter(myList))
# Counter({3: 4, 2: 4, 1: 3, 4: 2, 5: 1})
# type = Counter[int]
print(Counter(myList).items())
# dict_items([(1, 3), (3, 4), (2, 4), (4, 2), (5, 1)])
# type = dict_items[Tuple[int, int]]
print(Counter(myList).keys())
# dict_keys([1, 3, 2, 4, 5])
# type = KeysView[int]
print(Counter(myList).values())
# dict_values([3, 4, 4, 2, 1])
# type = ValuesView[int]
