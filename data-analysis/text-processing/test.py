path = "houses[].houseOrgBorrowInfos.personName.abc[].efg"

import copy

l = path.split('.')
l.reverse()

tmp = None

i = 0
for item in l:
    if item.endswith('[]'):

        inner_object = {
            item[:-2]: [tmp]
        }
        # tmp = copy.deepcopy(inner_object)
        tmp = inner_object
    else:
        if i == 0:
            inner_object = {
                item: "hehe"
            }
        else:
            inner_object = {
                item: tmp
            }

        # tmp = copy.deepcopy(inner_object)
        tmp = inner_object
    i += 1

print(tmp)

