import dbus
import webbrowser

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

    # To just print the title
    song_title = metadata['xesam:title'].replace(' ', '-')
    artist_name = metadata['xesam:artist'][0].replace(' ', '-')

    url_pt1 = 'http://www.songsterr.com/a/wa/bestMatchForQueryString?s='
    url_pt2 = '&a='
    url_songster = url_pt1+song_title+url_pt2+artist_name

    url_pt1 = 'https://www.cifraclub.com.br/'
    url_cifraclub = url_pt1+artist_name+'/'+song_title

    url = url_cifraclub
    if previous_url != url:
        try:
            webbrowser.open(url)
        except e:
            print(e)
        finally:
            previous_url = url
