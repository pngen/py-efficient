# Gets list of front page HN article names.
# Searches anything (*) w/ class='title', and then
# searches for links w/ class='storylink'

from lxml import html
import requests

page = requests.get('https://news.ycombinator.com/')

tree = html.fromstring(page.content)
titles = tree.xpath('//*[@class="title"]/a[@class="storylink"]/text()')

for title in titles:
	print(title)