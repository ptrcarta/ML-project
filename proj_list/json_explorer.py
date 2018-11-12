import json
import urllib.request
import sys
from pprint import pprint


JSON_FILE = 'list.json'
# Use FORUM_LINK.format(id) to get link to paper forum
FORUM_LINK = 'https://openreview.net/forum?id={}'
# Use REPLIES_LINK.format(id) to get link to paper replies
REPLIES_LINK = 'https://openreview.net/notes?forum={}'


def get_paper_scores(paper_id):
	contents = urllib.request.urlopen(REPLIES_LINK.format(paper_id))
	contents = json.load(contents)
	contents = contents['notes']
	ratings = []
	for note in contents:
		if 'rating' in note['content']:
			ratings.append(note['content']['rating'])
	return ratings


class PaperEntry(object):
	def __init__(self, json_paper_data):
		self.replies = json_paper_data['details']['replyCount']
		self.id = json_paper_data['id']
		self.tldr = None
		if "TL;DR" in json_paper_data['content']:
			self.tldr = json_paper_data['content']['TL;DR']
		self.keywords = None
		if "keywords" in json_paper_data['content']:
			self.keywords = json_paper_data['content']['keywords']
		self.title = json_paper_data['content']['title']
		self.ratings = get_paper_scores(self.id)
		self.data = json_paper_data

	def __repr__(self):
		s = "{}\n".format(self.title)
		s += "Replies: {}\n".format(self.replies)
		s += "Keywords: {}\n".format(self.keywords)
		s += "TL;DR {}\n".format(self.tldr)
		s += "Link: {}".format(FORUM_LINK.format(self.id))
		s += "Ratings:\n"
		for rating in self.ratings:
			s += "{}\n".format(rating)
		return s

if __name__ == '__main__':
	with open(JSON_FILE, 'r') as f:
		json_data = json.load(f)

	args = sys.argv

	top_k = 20
	if len(args) >= 2:
		top_k = int(args[1])

	papers = list(reversed(sorted(json_data, key=lambda paper: paper['details']['replyCount'])))
	papers = papers[:top_k]

	get_paper_scores(PaperEntry(papers[0]).id)

	if True:
		for p in papers:
			e = PaperEntry(p)
			print()
			print(e)
			print()
