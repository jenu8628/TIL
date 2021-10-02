import requests

class testFunc:
    x_auth_token = 'a3819b0b411c1b8f9c7e1bc6562392cb'

    def __init__(self, key, url):
        self.key = key
        self.url = url

    # 고유키 발급 API
    def start(self, problem):
        url = self.url + '/start'
        h = {'X-Auth-Token': self.x_auth_token, 'Content-Type': 'application/json'}
        d = {'problem': problem}
        return requests.post(url, params=d, headers=h).json()

    # 매칭 대기 API
    def watingLine(self):
        url = self.url + '/waiting_line'
        h = {'Authorization': self.key, 'Content-Type': 'application/json'}
        return requests.get(url, headers=h).json()

    # 게임 결과 API
    def gameResult(self):
        url = self.url + '/game_result'
        h = {'Authorization': self.key, 'Content-Type': 'application/json'}
        return requests.get(url, headers=h).json()

    # 유저 정보 API
    def userInfo(self):
        url = self.url + '/user_info'
        h = {'Authorization': self.key, 'Content-Type': 'application/json'}
        return requests.get(url, headers=h).json()

    # 유저 매칭 API
    def match(self, pairs):
        url = self.url + '/match'
        h = {'Authorization': self.key}
        d = {'pairs': pairs}
        return requests.put(url, json=d, headers=h).json()

    # 등급 수정 API
    def changeGrade(self, commands):
        url = self.url + '/change_grade'
        h = {'Authorization': self.key}
        d = {'commands': commands}
        return requests.put(url, json=d, headers=h).json()

