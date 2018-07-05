from jinja2 import Environment, PackageLoader, FileSystemLoader

env = Environment(loader=FileSystemLoader('webarch/templates'))

def render(name, data:dict):

    template = env.get_template(name)
    return template.render(**data)

