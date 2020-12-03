import requests
from kobis import URLMaker
import json

def filmo_count(page):
    url_maker = URLMaker('a5ef8ead5c3cf54816872baad397f192')
    url = url_maker.get_url()
    payload = f'page={page}'
    # URL 요청
    r = requests.get(url,params = payload)
    # json파일을 해석하여 str 타입을 dic타입으로 변환
    people_dict = r.json()
    return people_dict

file_data = []
for i in range(1, 20):
    file_data.extend(filmo_count(i)['results'])
    for j in range(((i-1)*20), len(file_data)):
        file_data[j]['poster_path'] = 'https://image.tmdb.org/t/p/w500' + file_data[j]['poster_path']

for i in range(len(file_data)):
    for j in range(len(file_data[i]['genre_ids'])):
        if file_data[i]['genre_ids'][j] == 28:
            file_data[i]['genre_ids'][j] = '액션'
        elif file_data[i]['genre_ids'][j] == 12:
            file_data[i]['genre_ids'][j] = '모험'
        elif file_data[i]['genre_ids'][j] == 16:
            file_data[i]['genre_ids'][j] = '애니메이션'
        elif file_data[i]['genre_ids'][j] == 35:
            file_data[i]['genre_ids'][j] = '코미디'
        elif file_data[i]['genre_ids'][j] == 80:
            file_data[i]['genre_ids'][j] = '범죄'
        elif file_data[i]['genre_ids'][j] == 99:
            pass
        elif file_data[i]['genre_ids'][j] == 18:
            file_data[i]['genre_ids'][j] = '드라마'
        elif file_data[i]['genre_ids'][j] == 10751:
            file_data[i]['genre_ids'][j] = '가족'
        elif file_data[i]['genre_ids'][j] == 14:
            file_data[i]['genre_ids'][j] = '판타지'
        elif file_data[i]['genre_ids'][j] == 36:
            file_data[i]['genre_ids'][j] = '역사'
        elif file_data[i]['genre_ids'][j] == 27:
            file_data[i]['genre_ids'][j] = '공포'
        elif file_data[i]['genre_ids'][j] == 10402:
            file_data[i]['genre_ids'][j] = '음악'
        elif file_data[i]['genre_ids'][j] == 9648:
            file_data[i]['genre_ids'][j] = '미스터리'
        elif file_data[i]['genre_ids'][j] == 10749:
            file_data[i]['genre_ids'][j] = '로맨스'
        elif file_data[i]['genre_ids'][j] == 878:
            file_data[i]['genre_ids'][j] = 'SF'
        elif file_data[i]['genre_ids'][j] == 10770:
            file_data[i]['genre_ids'][j] = 'TV영화'
        elif file_data[i]['genre_ids'][j] == 53:
            file_data[i]['genre_ids'][j] = '스릴러'
        elif file_data[i]['genre_ids'][j] == 10752:
            file_data[i]['genre_ids'][j] = '전쟁'
        elif file_data[i]['genre_ids'][j] == 37:
            file_data[i]['genre_ids'][j] = '서부'

# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('movies.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")