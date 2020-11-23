import requests
from kobis import URLMaker
import json
import random


def filmo_count():
    url_maker = URLMaker('a5ef8ead5c3cf54816872baad397f192')
    url = url_maker.get_url()
    # URL 요청
    r = requests.get(url)
    # json파일을 해석하여 str 타입을 dic타입으로 변환
    people_dict = r.json()
    # 주소에서 'peopleListResult'안에 'peopleList'로 접근
    return people_dict


file_data = []
for i in range(len(tmp['genres'])):
    file_data.append(tmp['genres'][i]['name'])

with open('top_rated.json', 'w', encoding='utf-8') as make_file:
    json.dump(top_rated, make_file, ensure_ascii=False, indent="\t")