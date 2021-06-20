import json
import requests
import urllib3
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from types import SimpleNamespace


ses = requests.Session()
wc_url = "https://commons.wikimedia.org/w/api.php"

category = "Category:Files uploaded by spell4wiki in ta"
limit = 3
max_records = 1
params_data = {
    "action": "query",
    "format": "json",
    "list": "categorymembers",
    "cmtitle": category,
    "cmlimit": limit,
    "cmsort": "timestamp",
    "cmdir": "desc"
}


def get_words_list(url):
	print("Fetching file names....")
	data = urllib.request.urlopen(urllib.parse.quote_plus(url)).read().decode()
	obj = json.loads(data)
	itemlist =obj["query"]["categorymembers"]
	file_names = []
	for item in itemlist:
	    file_names.append(item["title"])
	return file_names

def get_next_offset(res):
	if ("continue" in res and "cmcontinue" in res["continue"]):
		return res["continue"]["cmcontinue"]
		
	return None


next_offset = None
file_names = []
def parce_data():
	while True and len(file_names) < max_records:
		req = ses.get(url=wc_url, params=params_data)
		d = req.json()
		next_offset = get_next_offset(d)
		itemlist =d["query"]["categorymembers"]
		for item in itemlist:
		    file_names.append(item["title"])
		print("Total No of files ==> ", len(file_names))
		if (next_offset == None):
			break;
		else :
			if (max_records - len(file_names) < limit):
				params_data["cmlimit"] = max_records - len(file_names)
			if (next_offset != None):
				params_data["cmcontinue"] = next_offset
			
			parce_data()
			
	return file_names
		
if (max_records >= limit):
	print("Max records should be graterthan limit")

f_d = parce_data()
print(len(f_d))
print("After")
files = list(set(f_d))
print(len(files))

download_links = []

# Get Download link from commons
def fetch_download_links():
	print("Fetching download links.... of " + str(len(files)) + " files")
	for index, f in enumerate(files):
		url = "https://commons.wikimedia.org/wiki/"+f
		http = urllib3.PoolManager()
		response = http.request('GET', url)
		soup = BeautifulSoup(response.data, "html.parser")
		media = soup.findAll("div", attrs={"class":"fullMedia"})
		dl = media[0].find('a').get("href")
		f_dl = urllib.parse.unquote(dl)
		print(str(index+1) + ". " + f + " => " + f_dl)
		download_links.append(f_dl)
		

fetch_download_links()

# Download file from commons download link 
def download_files():
	print("Downloading started... Total files: " + str(len(download_links)))
	for index, dl in enumerate(download_links):
		d_filename = urllib.parse.unquote(dl).split("/")[-1]
		print(str(index+1) + "/" + str(len(download_links)) + " => " + d_filename)
		audio_request = requests.get(dl, allow_redirects=True)
		open(d_filename, 'wb').write(audio_request.content)
		
download_files()
