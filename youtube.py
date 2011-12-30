#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2
import string

soup = BeautifulSoup(urllib2.build_opener().open('http://www.youtube.com/user/heardmagazine/videos').read())
#soup = BeautifulSoup(urllib2.build_opener().open('http://www.youtube.com/user/skymilesthemovement/videos').read())

soup.find(attrs={'id' : 'masthead-container'}).extract()
soup.find(attrs={'id' : 'footer-container'}).extract()
soup.find(attrs={'class' : 'channel-horizontal-menu ytg-box'}).extract()
soup.find(attrs={'class' : 'video-sort-btn yt-uix-button'}).extract()
soup.find(attrs={'class' : 'primary-filter-menu'}).extract()
soup.find(attrs={'class' : 'channel-filtered-page-head'}).extract()

soup.style.replaceWith('''
<style>
	.channel-filtered-page {
		padding-top: 0px !important;
	}
	
	#branded-page-body-container > *, .ytg-wide {
		width: auto !important;
		margin-top: 0px !important;
	}
	
	body, #branded-page-body-container, .tab-content-body {
		background: transparent !important;
	}
	* {
		color: whiteSmoke !important;
	}
	.yt-uix-button-content * {
		color: #111111 !important;
	}
</style>
''')

print string.replace(string.replace(soup.prettify(), '"//', '"http://'), '"/', '"http://youtube.com/')
