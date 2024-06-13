from bs4 import BeautifulSoup


def main():
    html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.find(id="link2")) #<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    print(soup.find(id="link2").string) #Lacie

    for link in soup.find_all('a'):
        print(link.get('href')) #a태그에 있는 모든 URL추출


if __name__ == '__main__':
    main()