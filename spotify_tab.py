import dbus
import webbrowser
import requests
from lxml import html

def get_parsed_page(url):
    """Return the content of the website on the given url in
    a parsed lxml format that is easy to query."""

    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page

def get_url():
    previous_url = ''
    while(True):
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                             "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

        # The property Metadata behaves like a python dict
        # for key, value in metadata.items():
        #    print(key, value)

        # Get song title and artist name
        translation_table = dict.fromkeys(map(ord, "’'-.()"), None)
        song_title = metadata['xesam:title'].lower().translate(translation_table).replace(' ', '-')
        artist_name = metadata['xesam:artist'][0].lower().translate(translation_table).replace(' ', '-')
        
        # gambiarra
        if artist_name == 'onerepublic':
            artist_name = 'one-republic'

        url_pt1 = 'http://www.songsterr.com/a/wa/bestMatchForQueryString?s='
        url_pt2 = '&a='
        url_songsterr = url_pt1+song_title+url_pt2+artist_name

        url_pt1 = 'https://www.cifraclub.com.br/'
        url_cifraclub = url_pt1+artist_name+'/'+song_title

        url = url_cifraclub
        if previous_url != url:
            try:
                webbrowser.open(url)
                # parsed_page = get_parsed_page(url)
                # Print the website's title
                # chords = parsed_page.xpath('//span[@class="tablatura"]/text()')
                # tabs = parsed_page.xpath('//span[@class="cnt"]/text()')
                # for chord in chords:
                #    print(chord)
            except:
                pass
            finally:
                previous_url = url

if __name__ == '__main__':
        get_url()

