from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

##################
# Crumbling Castle
##################
my_url1 = 'http://lyrics.wikia.com/wiki/King_Gizzard_%26_The_Lizard_Wizard:Crumbling_Castle'
# opening connection and grabbing the page
uclient1 = req(my_url1)
page_html1 = uclient1.read()
uclient1.close()

# parsing the html text
page_soup1 = soup(page_html1, "html.parser")

# variable for div with class lyricbox
lyrics1 = page_soup1.find("div", {"class": "lyricbox"})

file1 = open('output.txt', "w")
file1.write(f'{lyrics1}')
file1.close()

##################
# Polygondwanaland
##################
my_url2 = 'http://lyrics.wikia.com/wiki/King_Gizzard_%26_The_Lizard_Wizard:Polygondwanaland'
# opening connection and grabbing the page
uclient2 = req(my_url2)
page_html2 = uclient2.read()
uclient2.close()

# parsing the html text
page_soup2 = soup(page_html2, "html.parser")

# variable for div with class lyricbox
lyrics2 = page_soup2.find("div", {"class": "lyricbox"})

file2 = open('output.txt', "a")
file2.write(f'{lyrics2}')
file2.close()
