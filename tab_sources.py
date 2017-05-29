from bs4 import BeautifulSoup
import requests

def text_adapter(text):
    translation_table = dict.fromkeys(map(ord, "’'-.()"), None)
    text = text.lower().translate(translation_table).replace(' ', '-').replace('&', 'e')
    return text


def _ultimateguitar(song, artist):
    url_pt1 = 'https://www.ultimate-guitar.com/search.php?view_state=advanced&band_name='
    url_pt2 = '&song_name='
    url_pt3 = '&type%5B%5D=300&type%5B%5D=200&rating%5B%5D=5&version_la='
    song = song.replace('-', '+')
    artist = artist.replace('-', '+')
    url = url_pt1+artist+url_pt2+song+url_pt3
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    urls = []
    for a in soup.find_all(class_='song result-link js-search-spelling-link', href=True):
        urls.append(a['href'])

    return urls


def _cifraclub(song, artist):
    url_pt1 = 'https://www.cifraclub.com.br/'
    url = url_pt1 + artist + '/' + song
    return [url, ]


def _songsterr(song, artist):
    url_pt1 = 'http://www.songsterr.com/a/wa/bestMatchForQueryString?s='
    url_pt2 = '&a='
    url = url_pt1+song+url_pt2+artist
    return [url, ]
