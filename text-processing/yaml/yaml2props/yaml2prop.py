import re 
import os.path
import argparse


def yaml2prop(filename, space_num=2):
    properties_file = '{}.properties'.format(filename)
    props = []
    with open(filename, 'r') as f,\
        open(properties_file, 'w') as p:
        for line in f:
            # Ignore comments and blank line
            ignore = re.search(r'^\s?[#]', line)
            if ignore or not line.strip() or ':' not in line:
                continue

            # Get indent level
            ptn = re.compile(r'(\s{' + str(space_num) + r'})')
            indents = ptn.findall(line.split(':')[0])
            level = len(indents) if indents else 0

            result_prop = re.search(r'.+(?=:\s?)', line)

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
                print(new_line, file=p)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("yaml", help='Specify a YAML to convert')
    args = parser.parse_args()

    if not os.path.exists(args.yaml):
        print("{} not exists".format(args.yaml))
        exit(-1)

    yaml2prop(args.yaml)
