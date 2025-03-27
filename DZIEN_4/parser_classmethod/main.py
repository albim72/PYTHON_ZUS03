
from parsers import Parser

json_text = '{"name":"Anna","age":30}'

parser = Parser.create_parser("json")
data = parser.parse(json_text)

print(data)
print(type(parser))
