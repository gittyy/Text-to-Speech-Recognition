import requests
import BeautifulSoup as bs
import re

def parse_link(link):
	r = requests.get(link)
	soup = bs.BeautifulSoup(r.content)
	content = soup.find("div", {"id" : "mw-content-text"})
	text_para = content.findAll("p")
	text = ""
	for para in text_para:
		text += clean_text(para.getText())
	return text

def clean_text(text):
	return re.sub(r"\[\d*\]", "", text)