import json
from collections import OrderedDict

file_data = OrderedDict()
for 
file_data["name"] = "first"
file_data["age"] = 23
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

# with open('boxoffice.json', 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file)