import webbrowser

keywords = ['손흥민','헐크','아이언맨','토르']
for keyword in keywords:
    url = 'https://www.google.com/search?q={}'.format(keyword)
    webbrowser.open(url)

   