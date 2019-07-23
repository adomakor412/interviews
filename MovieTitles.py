import urllib.request
import string
import json

def getMovieTitles(substr):
    myTitles = []
    search = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr
    contents = urllib.request.urlopen(search).read()
    if contents:
        contents = json.loads(contents.decode('utf-8'))
        totalPages = int(contents['total_pages'])
        for page in range(totalPages):
            pageR = search + '&page=' + str(page+1)
            newContent = urllib.request.urlopen(pageR).read()
            cursor = json.loads(newContent.decode('utf-8'))
            for result in cursor['data']:
                print(result)
                myTitles.append(result['Title'])
    return myTitles
