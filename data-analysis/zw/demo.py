
old = {'buy': {'test': 'case'}}
new = {'buy': {'test1': 'case1'}}

for k, v in new.items():
    if k in old:
        old[k].update(v)

print(old)

