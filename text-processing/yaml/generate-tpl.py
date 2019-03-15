import yaml
import jinja2

from jinja2 import Environment, FileSystemLoader

with open('crypto-config.yaml', 'r') as f:
    config = yaml.load(f, yaml.Loader)

env = Environment(loader=FileSystemLoader('./'), trim_blocks=True)
template = env.get_template('tpl.jinja')

print(template.render(config))

