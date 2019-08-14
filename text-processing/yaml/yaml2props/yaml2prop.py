import re


line = '      #shit abc'
line = '  port: 8080'
# line = 'server: '
ignore = re.search(r'^\s?[#-]', line)
print(ignore)

tabs = re.findall(r'(\s\s)', line.split(':')[0])
index = len(tabs) if tabs else 0
print(tabs)
print(index)

result_prop = re.search(r'.+(?=:\s)', line)
print(result_prop)

if ':' not in line:
    pass

