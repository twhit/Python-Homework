import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			# Instead of using the meta tag keywords, list any content
                 # found in html heading tags (h1-h5). -- TW
			regexp = re.compile('<h[1-5].*>(.*)</h[1-5]>')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				print(title)
                 
			for (headings) in re.findall(regexp, content_string):
				print(headings)
			for (urls) in re.findall(regexp_url, content_string):
				if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
					crawler_backlog[urls] = 0
					visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")
