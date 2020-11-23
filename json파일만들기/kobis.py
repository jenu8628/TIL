class URLMaker:

    url = 'https://api.themoviedb.org/3/movie/top_rated'
    # url = 'https://api.themoviedb.org/3/genre/movie/list'
    key = 'a5ef8ead5c3cf54816872baad397f192'

    def __init__(self, key):
        self.key = key

    def get_url(self):
        return f'{self.url}?api_key={self.key}&language=ko-KR'
