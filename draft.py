import re

url_patterns = [
    r'/api/maillists/(.+?)/(.+?)$',
    r'/api/groups/(.+?)/(.+?)/(.+?)$',
]

url = '/api/groups/jira/jira-software-users/member'

for ptn in url_patterns:
    if re.match(ptn, url):
        print('matched')
        break

ptn = '/(.*)/.+$'
s = '/api/groups/jira/jira-software-users/shit'

tmp = s.split('/')[:-1]
print(type(tmp))
tmp.append('member')
print('/'.join(tmp))




