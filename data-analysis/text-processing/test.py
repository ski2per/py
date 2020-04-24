
path = "houses[].houseOrgBorrowInfos.personName.abc[].efg"

import copy

l = path.split('.')
l.reverse()

tmp = None

def abc(item):
    global tmp
    if len(item) == 0:
        return 
    if isinstance(item, list):
        item.pop()
        return abc(item)
    else:
        if item.endswith('[]'):
            inner_object = {
                item[:-2] = [tmp]
            }
            # tmp = copy.deepcopy(inner_object)
            tmp = inner_object
        else:
            inner_object = {
                item: tmp
            }
            tmp = inner_object

        return tmp


# abc(path.split('.'))


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


print(factorial_recursive(3))
