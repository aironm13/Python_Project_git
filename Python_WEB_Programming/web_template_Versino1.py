import re
from io import StringIO, BytesIO

d = {'id':5, 'name':'tom', 'age':20}

class Template:
    _pattern = '{{([a-zA-Z0-9_])}}'
    regex = re.compile(_pattern)

    @classmethod
    def render(cls, template, data:dict):
        html = StringIO()

        with open(template, encoding='utf-8') as f:
            for line in f:
                start = 0
                newline = ''
                for matcher in cls.regex.finditer(line):
                    newline += line[start:matcher.start()]
                    print(matcher, matcher.group(1))
                    key = matcher.group(1)
                    tmp = data.get(key, '')
                    newline += str(tmp)
                    start = matcher.end()
                else:
                    newline += line[start:]
                html.write(newline)
            print(html.getvalue())
        html.close()

filename = 'index.html'
Template.render(filename, d)