#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from BeautifulSoup import BeautifulSoup
from htmlmin.minify import html_minify
import simplejson as json
import urllib2
import string



def geturl(str):
	return urllib2.urlopen(str).geturl()

def curl(str):
	return urllib2.urlopen(str).read()

def decode(str):
	return json.JSONDecoder().decode(curl(str))

def facebook(str=''):
	return decode('https://graph.facebook.com/326419920716241/' + str + '?access_token=AAACEdEose0cBACdbvgkWyH39MymuCNYasl5UHSAcuzDgZC6z3qHZCYK2hkNW7qe9FPi7bUTxlmYeRvxtW6QTVioDRaSxUKetZBg7TTuuAZDZD')

def html(soup):
	return html_minify(string.replace(soup.prettify(), '\\n', '<br>'))


home = BeautifulSoup(open('template.txt', 'r').read())
homeout = open('index.html', 'w')

videos = BeautifulSoup(open('template.txt', 'r').read())
videosout = open('videos.html', 'w')
videosframe = BeautifulSoup(curl('http://www.youtube.com/user/blotchryanismi/videos'))
#videosframe = BeautifulSoup(curl('http://www.youtube.com/user/skymilesthemovement/videos'))
videosframeout = open('youtube.html', 'w')

photos = BeautifulSoup(open('template.txt', 'r').read())
photosout = open('photos.html', 'w')

sky = BeautifulSoup(open('template.txt', 'r').read())
skyout = open('sky.html', 'w')

carpet = BeautifulSoup(open('template.txt', 'r').read())
carpetin = open('carpet.txt', 'r').read()
carpetout = open('carpet.html', 'w')

community = BeautifulSoup(open('template.txt', 'r').read())
communityin = open('community.txt', 'r').read()
communityout = open('community.html', 'w')


home.find(attrs={'href' : '/'}).parent['class'] = 'active'
videos.find(attrs={'href' : 'videos'}).parent['class'] = 'active'
photos.find(attrs={'href' : 'photos'}).parent['class'] = 'active'
sky.find(attrs={'href' : 'sky'}).parent['class'] = 'active'
carpet.find(attrs={'href' : 'carpet'}).parent['class'] = 'active'
community.find(attrs={'href' : 'community'}).parent['class'] = 'active'


page = facebook()
links = facebook('links')['data']


linkshtml = ''
linkshtmlcount = 1
for link in links:
	if linkshtmlcount == 1:
		linkshtml += '</div><div class="row">'
	
	try:
		message = link['message']
	except:
		message = ''
	
	linkshtml += '''
		<div class="''' + ('span4' if linkshtmlcount == 2 else 'span5') + '''">
			<h5><a href="''' + link['link'] + '''" title="''' + message + '''">''' + link['name'] + '''</a></h5>
			<br>
			<p>''' + link['description'] + '''</p>
		</div>
	'''
	
	if linkshtmlcount == 3:
		linkshtmlcount = 1
	else:
		linkshtmlcount += 1


home.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		<div class="hero-unit">
			<h1>''' + page['name'] + '''</h1>
			<p>''' + page['description'] + '''</p>
		''' + linkshtml + '''
		</div>
	</div>
''')




videos.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		<iframe
			src="youtube.html" scrolling="yes" frameborder="0" style="border:none; overflow:hidden; width: 100%; height: 860px;" allowTransparency="true"></iframe>
	</div>
''')


videosframe.find(attrs={'id' : 'masthead-container'}).extract()
videosframe.find(attrs={'id' : 'footer-container'}).extract()
videosframe.find(attrs={'class' : 'channel-horizontal-menu ytg-box'}).extract()
videosframe.find(attrs={'class' : 'video-sort-btn yt-uix-button'}).extract()
videosframe.find(attrs={'class' : 'primary-filter-menu'}).extract()
videosframe.find(attrs={'class' : 'channel-filtered-page-head'}).extract()
videosframe.find(attrs={'role' : 'button'}).extract()

videosframe.style.replaceWith('''
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





curl('http://wordpress.heardmag.com/wordpress/wp-content/plugins/fotobook/cron.php?secret=1cfa130f1bdf&update')

photos.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		<iframe
			src="http://wordpress.heardmag.com/wordpress/?page_id=3" scrolling="yes" frameborder="0" style="border:none; overflow:hidden; width: 100%; height: 860px; border-radius:4px;'" allowTransparency="true"></iframe>
	</div>
''')





sky.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		<iframe
			src="http://skymiles3.tumblr.com/" scrolling="yes" frameborder="0" style="border:none; overflow:hidden; width: 100%; height: 860px; border-radius:4px;'" allowTransparency="true"></iframe>
	</div>
''')





carpet.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		''' + carpetin + '''
	</div>
''')





community.find(attrs={'id' : 'content'}).replaceWith('''
	<div id="content" class="content">
		''' + communityin + '''
	</div>
''')







homeout.write(html(home))
videosout.write(html(videos))
videosframeout.write(string.replace(string.replace(html(videosframe), '"//', '"http://'), '"/', '"http://youtube.com/'))
photosout.write(html(photos))
skyout.write(html(sky))
carpetout.write(html(carpet))
communityout.write(html(community))

