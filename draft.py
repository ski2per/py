import re


ptn = '/api/groups/.+?'
# ptn = '/api/groups/'

url = '/api/groups/'
# url = '/api/groups/jira'
# url = '/api/groups/jira/jira-software-users'
# url = '/api/groups/jira/jira-software-users/member'

# print(re.match(ptn, url))


print(re.fullmatch(ptn, url))
