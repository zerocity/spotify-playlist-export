Export playlists from Spotify into YouTube
==========================================

### What does this do?

1. Takes a Spotify HTTP URI's list, parses the URI's for artist &amp; song info.
2. Takes that info &amp; searches Google for a YouTube video.
3. Sticks those videos into a new playlist in your YouTube account.

### Python Dependencies

* BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)
* googleplex (http://googolplex.sourceforge.net/)
* gdata (http://code.google.com/p/gdata-python-client/)