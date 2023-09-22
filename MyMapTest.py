from TreeMap import *
from HashMap import *


def test(my_map):
    print(f'Is it empty?: {my_map.is_empty()}')
    my_map.put("key5", 5)
    my_map.put("key2", 2)
    my_map.put("key3", 3)
    my_map.put("key1", 1)
    my_map.put("key7", 7)
    my_map.put("key10", 10)
    print(f'get("key5") Value of: {my_map.get("key5")}')
    print(my_map.__str__())
    print(f'Should say True: {my_map.contains_key("key5")}')
    print(f'Size: {my_map.size()}')
    my_map.remove("key5")
    my_map.remove("key5")
    print(f'Should say False: {my_map.contains_key("key5")}')
    print(f'Size: {my_map.size()}')
    print(my_map.__str__())
    print(f'Is it empty?: {my_map.is_empty()}')


test(TreeMap())
test(HashMap())
