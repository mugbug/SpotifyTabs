import dbus # to access Spotify metadata on Linux
import webbrowser # to open link on browser
import platform # to get current OS


def adapt_string(text):
    translation_table = dict.fromkeys(map(ord, "’'-.()"), None)
    text = text.lower().translate(translation_table).replace(' ', '-').replace('&', 'e')
    return text

def get_song():
    song_title = ''
    artist_name = ''
    current_os = platform.system()
    if current_os == 'Linux':
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
        song_title = adapt_string(metadata['xesam:title'])
        artist_name = adapt_string(metadata['xesam:artist'][0])

    elif current_os == 'Windows':
        import spotilib # to access Spotify metadata on Windows
        song_title = adapt_string(spotilib.song())
        artist_name = adapt_string(spotilib.artist())

    return song_title, artist_name

def generate_url(tab_src, song, artist):
    # gambiarra
    if artist == 'onerepublic':
        artist = 'one-republic'

    # generating url according to source pattern (not 100% accurate yet)
    if tab_src == 'Songsterr':
        url_pt1 = 'http://www.songsterr.com/a/wa/bestMatchForQueryString?s='
        url_pt2 = '&a='
        return url_pt1+song+url_pt2+artist
    elif tab_src == 'CifraClub':
        url_pt1 = 'https://www.cifraclub.com.br/'
        return url_pt1+artist+'/'+song

def banner():
    tab_src = ''
    print('\tWelcome to SpotifyTabs!\n\n\tSupported tab sources:')
    while(tab_src != '1' and tab_src != '2'):
        print('\t1. Songsterr\t2. Cifra Club')
        tab_src = str(input('\tChoice: '))
    print('\nSpotifyTabs is now running.\nPress ctrl+c to stop.\n')

    if tab_src == '1':
        return 'Songsterr'
    elif tab_src == '2':
        return 'CifraClub'

def main():
    previous_url = ''
    tab_src = banner()
    while(True):
        song, artist = get_song()
        url = generate_url(tab_src, song, artist)

        if previous_url != url:
            webbrowser.open(url)
            previous_url = url

if __name__ == '__main__':
        main()
