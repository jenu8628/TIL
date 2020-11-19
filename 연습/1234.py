import requests
from kobis import URLMaker
import json
import time

date_time = int(time.strftime('%Y%m%d', time.localtime(time.time()))) - 1

def filmo_count(page):
    url_maker = URLMaker('a5ef8ead5c3cf54816872baad397f192')
    url = url_maker.get_url()
    payload = f'page={page}'
    # URL 요청
    r = requests.get(url,params = payload)
    # json파일을 해석하여 str 타입을 dic타입으로 변환
    people_dict = r.json()
    # 주소에서 'peopleListResult'안에 'peopleList'로 접근
    return people_dict
# file_data = filmo_count(1)
file_data = []
for i in range(1, 2):
    for j in range(len(filmo_count(i)['results'])):
        filmo_count(i)['results'][j]['poster_path'] = 'https://image.tmdb.org/t/p/w500'+ filmo_count(i)['results'][j]['poster_path']
        print(filmo_count(i)['results'][j]['poster_path'])

    file_data.extend(filmo_count(i)['results'])

# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
# print(len(file_data))

with open('movies.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")