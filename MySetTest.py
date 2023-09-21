from HashSet import *


def test_set(my_set):
    my_set.add(5)
    my_set.add(6)
    my_set.add(7)
    print(my_set.contains(7))
    my_set.add(8)
    my_set.add(9)
    my_set.remove(7)
    my_set.remove(7)
    print(my_set.contains(7))
    print(my_set.is_empty())
    print(my_set.size())


test_set(TreeSet())
test_set(HashSet())
