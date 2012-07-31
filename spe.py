import sys
import urllib2
from BeautifulSoup import BeautifulSoup

target_properties = ['og:title', 'og:type', 'og:image', 'og:description', 'og:audio', 'og:audio:type', 'og:url']

def get_soup(url):
    page = urllib2.urlopen(url)
    return BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)


def parse_spotify_uri(url):
    soup = get_soup(url)
    return {prop[3:] : soup.find('meta', {'property' : prop})['content'] for prop in target_properties}


if __name__ == "__main__":

    if (len(sys.argv) > 1):
        with open( sys.argv[1], 'r') as fp:
            for line in fp:
                count = 0
                for item in parse_spotify_uri(line):
                    count += 1
                    print count, item
    else:
        print "USAGE: %s <filename with a list of spotify http uris>" % (sys.argv[0])
