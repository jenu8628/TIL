import requests
from sampleFunc import sample

token = '8a47ec7bbf849c8b13e4108b53e0af27'
url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
auth_key = '7cf463a3-bf1a-45dd-a85e-220d9ef7391c'
nn= [-1,5,60]
tt = [-1,5,10]
di,dj = [0,0,1,-1], [1,-1,0,0]

# 클래스 불러오기
sam = sample(token, url)

# 가장 빈도수가 많은 정거장과 가장 빈도수가 적은 정거장
# 빈도수 : 대여 - 반납으로 결정
max_rent, min_rent = sam.analysis()

# 자전거 위치
locations = sam.location(auth_key)['locations']
for i in locations:
    print(i)

# 트럭 위치
trucks = sam.truck(auth_key)['trucks']
for i in trucks:
    print(i)
command = []
for i in range(len(max_rent)):
    # 빈도수 많은 곳에 자전거가 다 떨어지면
    if locations[max_rent[i]]['located_bikes_count'] == 0:
        # 빈도수 적은곳에서 빌려오자
        count = 0
        near_truck = 0
        for j in range(len(min_rent)):
            count += 1
            # 빈도수 적은 곳 중 자전거가 있는 곳에서
            if locations[min_rent[j]]['located_bikes_count'] != 0:
                # 가장 근처의 트럭을 찾자!!
                min_num = 999999
                for truck in trucks:
                    if abs(min_rent[j] - truck['location_id']) < min_num:
                        near_truck = truck["id"]
                # 트럭 찾았으니 트럭 움직이는 커맨드!
                while True:

                    break
                break
        # 만약 빈도수 적은 애들이 다 자전거가 비어있다면!
        if count == len(min_rent):
            # 상하좌우! 가장 가까운 곳에서 가져오자!
            pass

# command = [
#         # {"truck_id": 0, "command": [2, 5, 4, 1, 6]},
#         # {"truck_id": 1, "command": [1, 3, 5, 2, 4]},
#         # {"truck_id": 2, "command": [3, 6, 3, 2, 6]},
#         # {"truck_id": 3, "command": [4, 0, 5, 2, 6]},
#         # {"truck_id": 4, "command": [5, 2, 4, 4, 6]},
#     ]