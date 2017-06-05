# coding: utf-8
import webbrowser # to open link on browser
import platform # to get current OS
import tab_sources as s


def text_adapter(text):
    translation_table = dict.fromkeys(map(ord, "’'-.,()"), None)
    text = text.lower().translate(translation_table).replace(' ', '-').replace('&', 'e')
    return text


def get_song():
    song_title = ''
    artist_name = ''
    current_os = platform.system()
    if current_os == 'Linux':
        import dbus # to access Spotify metadata on Linux
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
        song_title = text_adapter(metadata['xesam:title'])
        artist_name = text_adapter(metadata['xesam:artist'][0])

    elif current_os == 'Windows':
        import spotilib # to access Spotify metadata on Windows
        song_title = text_adapter(spotilib.song())
        artist_name = text_adapter(spotilib.artist())

    return song_title, artist_name


def generate_url(tab_src, song, artist):
    # gambiarra
    # if artist == 'onerepublic':
    #     artist = 'one-republic'

    # generating url according to source pattern (not 100% accurate yet)
    try:    
        if tab_src == 'Songsterr':
            return s._songsterr(song, artist)[0]
        elif tab_src == 'CifraClub':
            return s._cifraclub(song, artist)[0]
        elif tab_src == 'UltimateGuitar':
            return s._ultimateguitar(song, artist)[0]
    except Exception as e:
        print(e)

def banner():
    tab_src = ''
    print('\tWelcome to SpotifyTabs!\n\n\tSupported tab sources:')
    while tab_src != '1' and tab_src != '2' and tab_src != '3':
        print('\t1. Songsterr\t2. Cifra Club\t3. UltimateGuitar')
        tab_src = str(input('\tChoice: '))
    print('\nSpotifyTabs is now running.\nPress ctrl+c to stop.\n')

    if tab_src == '1':
        return 'Songsterr'
    elif tab_src == '2':
        return 'CifraClub'
    elif tab_src == '3':
        return 'UltimateGuitar'


def main():
    previous_url = ''
    tab_src = banner()
    while True:
        song, artist = get_song()
        url = generate_url(tab_src, song, artist)

        if previous_url != url:
            webbrowser.open(url)
            previous_url = url

if __name__ == '__main__':
        main()
