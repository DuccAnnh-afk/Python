_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new = list(dict.fromkeys(_list))

print(_new)