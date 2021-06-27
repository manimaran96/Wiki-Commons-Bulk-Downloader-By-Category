# Wiki Commons Bulk Downloader By Category

Wikimedia Commons Bulk Downloader By Category


## Why this script
Wikimedia commons have lot of files in various creative commons license. There, all files are categorised.
Basically wikimedia commons have various files images, audio, video, ..etc.

We have one audio upload tool called Spell4Wiki that allows to upload the audio files to commons. That tool also categorised the uploaded audio files based on the country code.

For Tamil: [Category:Files uploaded by spell4wiki in ta](https://commons.wikimedia.org/wiki/Category:Files_uploaded_by_spell4wiki_in_ta)

For English: [Category:Files uploaded by spell4wiki in en](https://commons.wikimedia.org/wiki/Category:Files_uploaded_by_spell4wiki_in_en)

More details : [Category:Files uploaded by spell4wiki](https://commons.wikimedia.org/wiki/Category:Files_uploaded_by_spell4wiki)

We can use this uploaded audio files to some other FOSS related projects. 
So, this script help easy way to download all the files in specific category.

Note: This script not only for audio files we can use this same script for other file format also.


## How this script working
This script required category name and max record count. 

1. REQUIRED: `category` is the wikimedia commons category name that have list of files: "Category:Files uploaded by spell4wiki in ta"
2. OPTIONAL: `max_records` is the count of maximum records you want to download.

This script download latest uploaded items to old items. So, max records can help to download the some count of latest items only.

Ref: 

<img src="https://gitlab.com/manimaran/wiki-commons-bulk-downloader-by-category/-/raw/main/files/wikimedia_commons_category_page_ex.png" width="820px" height="420px"></img>

Here, **Category:Files uploaded by spell4wiki in ta** is the category name.


## How to Run


1. Download/Clone this Repo
```
git clone https://gitlab.com/manimaran/wiki-commons-bulk-downloader-by-category.git 
```
2. Open the `config.py` file in editor and do change the `category`, `max_records` and `limit`

Note: `max_records` and `limit` are optional 
```
Wikimedia commons category name that have list of files like: "Category:Files uploaded by spell4wiki in ta"
Ref: https://commons.wikimedia.org/wiki/Category:Files_uploaded_by_spell4wiki
```
`category = "Category:Files uploaded by spell4wiki in CHECK"`

```
Optional
Count of maximum records you want to download. 
Recommended -1, It means no max_records limit. Download all the files in the above category
Incase you want download recently uploaded files. Then, provide that limit. Ex. if you want to download recently uploaded 10 files then give 10.
```
`max_records = -1`

```
Optional
Minimum 1 & Maximum 500, Recommended 500/200
```
`limit = 500`

3. Install following libraries 
```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip install beautifulsoup4
pip install aiohttp
pip install asyncio
pip install aiofiles
```
4. Once all are done now we can run the script.

```shell
python3 wikimedia-commons-bulk-downloader-by-category.py
```

<img src="https://gitlab.com/manimaran/wiki-commons-bulk-downloader-by-category/-/raw/main/files/wikimedia_commons_download_script.png" width="820px" height="320px"></img>


## For Contributors
If you willing to contibute this code. Please read below todo list and do your contribution. Before start your contribution make sure to create issue and assign your self. Which is help to reduce rework.

## Todo
1. Some packages install so make requirements.txt based on that.
2. Fix: While downloding morethan 3000 or large files may failed. Bcz of concurrent download/scraping calls.

*Optional*
1. After downloaded files compressed in .zip file format
2. Make webportal for this.

## Contact 
* If you want to get in touch with the developer you can send an email to <a href="mailto:manimarankumar96@gmail.com">manimarankumar96@gmail.com</a> or [@manimarank](https://t.me/manimaran_k) in Telegram.
* Feel free to post suggestions, changes, ideas etc. on GitHub or Telegram!
