import requests

class sample:

    def __init__(self, token, url):
        self.token = token
        self.url = url

    def analysis(self):
        scenario1 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-1.json').json()
        scenario2 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-2.json').json()
        scenario3 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-3.json').json()
        rent = [0] * 25
        for key, val in scenario1.items():
            for i in val:
                rent[i[0]] += 1
                rent[i[1]] -= 1
        for key, val in scenario2.items():
            for i in val:
                rent[i[0]] += 1
                rent[i[1]] -= 1
        for key, val in scenario3.items():
            for i in val:
                rent[i[0]] += 1
                rent[i[1]] -= 1

        min_num = sorted(rent)[0:5]
        max_num = sorted(rent, reverse=True)[0:5]

        min_idx = []
        max_idx = []
        cnt = 0
        while len(max_idx) < 5:
            min_n = min_num[cnt]
            max_n = max_num[cnt]
            for i in range(len(rent)):
                if rent[i] == max_n and i not in max_idx:
                    max_idx.append(i)
                    break
            for i in range(len(rent)):
                if rent[i] == min_n and i not in min_idx:
                    min_idx.append(i)
                    break
            cnt += 1
        return min_idx, max_idx



    def start(self, problem):
        uri = self.url + '/start'
        h = {'X-Auth-Token': self.token, 'Content-Type': 'application/json' }
        d = {'problem': problem}
        return requests.post(uri, params=d, headers=h).json()

    def location(self, key):
        uri = self.url + '/locations'
        h = {'Authorization': key, 'Content-Type': 'application/json'}
        return requests.get(uri, headers=h).json()

    def truck(self, key):
        uri = self.url + '/trucks'
        h = {'Authorization': key, 'Content-Type': 'application/json'}
        return requests.get(uri, headers=h).json()

    def simulate(self, key, command):
        uri = self.url + '/simulate'
        h = {'Authorization': key}
        d = {'commands': command}
        return requests.put(uri, json=d, headers=h).json()

    def score(self, key):
        uri = self.url + '/score'
        h = {'Authorization': key, 'Content-Type': 'application/json'}
        return requests.get(uri, headers=h).json()