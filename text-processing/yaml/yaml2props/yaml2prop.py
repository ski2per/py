import re
import os.path


def yaml2prop(filename, space_num=2):
    props = []
    print(os.path.basename(filename))
    with open(filename) as f:
        for line in f:

            # Ignore comments and blank line
            ignore = re.search(r'^\s?[#]', line)
            if ignore or not line.strip() or ':' not in line:
                continue

            ptn = re.compile(r'(\s{' + str(space_num) + r'})')
            indents = ptn.findall(line.split(':')[0])

            level = len(indents) if indents else 0

            result_prop = re.search(r'.+(?=:\s)', line)

            # Property without indent
            if level is 0:
                props = [result_prop.group().strip()]
            # Property with indent
            else:
                prop_name = result_prop.group().strip()
                while props and level < len(props):
                    props.pop()
                props.append(prop_name)

            value = re.search(r'(?<=:).+', line)
            # need to process if value is a list

            # Format value
            if value and value.group().strip():
                new_line = '{} = {}'.format('.'.join(props), value.group().strip())
                print(new_line)


if __name__ == '__main__':
    filename = 'demo.yml'
    yaml2prop(filename)
