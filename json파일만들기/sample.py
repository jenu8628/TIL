import requests
from kobis import URLMaker
import json

# open("community-new.json","wb").write(open("community.json").read().decode("unicode_escape").encode("utf8"))

file_data = open("community.json").read().encode("utf8")

with open('community-new.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


# with open('movies.json', 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent="\t")