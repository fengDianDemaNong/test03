import tika
tika.initVM()
from tika import parser
FILE_PATH = 'test.pdf'
parsed = parser.from_file(FILE_PATH)
print(parsed["content"].strip())