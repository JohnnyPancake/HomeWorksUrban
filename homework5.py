immutable_var = 3, 5, 7, 9, 'это кортеж', True
print(immutable_var)
# immutable_var [0] = 333
# Кортежи относятся к неизменяемым типам данных, поэтому вы не можете изменить кортеж после его создания.
mutable_list = [2, 4, 6, 8, 'это список', True]
mutable_list[3] = 999
mutable_list.append('его можно изменять')
print(mutable_list)
