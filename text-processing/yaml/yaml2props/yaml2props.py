import re

with open("application-dkxl.yml") as f:
    lines = f.readlines()

prop = []

output = ''

for line in lines:
    print(output)
    ignore = re.search(r'^\s?[#-]', line)

    if ignore or not line.strip() or not ':' in line:
        output += '\n'
        continue
    tabs = re.findall(r'(\s\s)', line.split(':')[0])

    index = len(tabs) if tabs else 0

    result_prop = re.search(r'.+(?=:\s)', line)
    
    if index is 0:
        prop = []
        prop.append(result_prop.group().strip())
    else:
        prop_name = result_prop.group(0).strip()

        while prop and index < len(prop):
            prop.pop()

        prop.append(prop_name)

    value = re.search(r'(?<=:).+', line)

    if value and value.group().strip():
        p = '.'.join(prop) + ' = ' + value.group().strip() + '\n'
        output += p

# Prepare write file
file_path =  'done.properties'

# For debug output
print(output) 

print('\nSave to file : ' + file_path)
 
 # Write file
file_props = open(file_path,'w+')
file_props.write(output)
file_props.close()

print('Done!')
