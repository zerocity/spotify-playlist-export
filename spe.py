import sys
import urllib2
import argparse
from BeautifulSoup import BeautifulSoup
from google import search
import gdata.youtube.service

DEVELOPER_KEY = 'INSERT_YOUR_DEVELOPER_KEY_HERE'
target_properties = ['og:title', 'og:type', 'og:image', 'og:description', 'og:audio', 'og:audio:type', 'og:url']

def get_soup(url):
    page = urllib2.urlopen(url)
    return BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)


def spotify_parse(url):
    soup = get_soup(url)
    return {prop[3:] : soup.find('meta', {'property' : prop})['content'] for prop in target_properties}


def main():
    parser = argparse.ArgumentParser(description='Import Spotify playlists into youtube.')
    parser.add_argument('-e','--email', help='Email used to access your youtube account.', required=True)
    parser.add_argument('-p','--password', help='Password for said account.', required=True)
    parser.add_argument('-t','--title', help='Title for the playlist.', required=True)
    parser.add_argument('-f','--filename', help='File holding list of HTTP spotify URIs.', required=True)
    args = vars(parser.parse_args())

    client = gdata.youtube.service.YouTubeService(developer_key=DEVELOPER_KEY)
    client.ClientLogin(args['email'], args['password'])
    playlist = client.AddPlaylist(args['title'], "This playlist was imported from spotify")
    playlist_uri = playlist.feed_link[0].href
    with open( args['filename'], 'r') as fp:
        for line in fp:
            meta = spotify_parse(line)
            song = meta['description'].replace(" on Spotify", "").replace("a song by ", "")
            searchfor = song + " site:youtube.com"
            youtube_url = search(searchfor.decode("utf-8").encode("ascii","replace"), stop=20).next()
            video_id = youtube_url[-11:]
            try:
                print "Adding", song, video_id
                client.AddPlaylistVideoEntryToPlaylist(playlist_uri, video_id)
            except gdata.service.RequestError, e:
                print "Problem adding", song, video_id

if __name__ == "__main__":
    main()
