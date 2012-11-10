Export playlists from Spotify into YouTube
==========================================

### What does this do?

1. Takes a Spotify HTTP URI's list, parses the URI's for artist &amp; song info.
2. Takes that info &amp; searches Google for a YouTube video.
3. Sticks those videos into a new playlist in your YouTube account.

### Python Dependencies

* BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)
  - pip install BeautifulSoup
* googleplex (http://googolplex.sourceforge.net/)
  - or https://github.com/MarioVilas/google
* gdata (http://code.google.com/p/gdata-python-client/)
  - pip install gdata

### Requirements

You'll need a developer key which you can obtain from: -

(http://code.google.com/apis/youtube/dashboard/gwt/index.html)