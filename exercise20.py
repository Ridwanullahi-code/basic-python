import collections

name1 = "Ross"
name2 = "Racheal"
bond = "bonds"
join = list(name1 + bond + name2)
print(join)
count = collections.Counter(join)
print(count)
empty_list = []
empty_list.extend(join)
print(empty_list)