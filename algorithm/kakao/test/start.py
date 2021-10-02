import requests

def start(problem):
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod' + '/start'
    h = {'X-Auth-Token': 'a3819b0b411c1b8f9c7e1bc6562392cb', 'Content-Type': 'application/json'}
    d = {'problem': problem}
    return requests.post(url, params=d, headers=h).json()

s = start(2)
print(s)
# # 시나리오 1
key1_5 = '11747e96-9798-48b8-91ae-aa3785eff0df'     # 236.32   50이젤잘나옴


# 시나리오 2
key3_3 = '5ce48368-9468-4d80-b44f-a4b66d9498a2'     # 182.57
key3_4 = 'cde33675-0e7f-4e66-a99e-6fbb22fb63ff'     # 183
key3_5 = 'b02327c1-0aa4-421c-bcd5-864c18d76eae'     # 176.2628


def score():
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod' + '/score'
    h = {'Authorization': key3_5, 'Content-Type': 'application/json'}
    return requests.get(url, headers=h).json()
print(score())


# win = [13, 9, 8, 16, 10, 6, 7, 11, 15, 3, 10, 6, 8, 11, 15, 7, 7, 5, 6, 3, 10, 15, 6, 5, 3, 3, 12, 6, 14, 12]
# lose = [7, 7, 9, 6, 8, 9, 10, 5, 2, 14, 6, 12, 6, 6, 2, 9, 8, 11, 10, 15, 6, 6, 9, 16, 13, 15, 5, 10, 8, 12]


