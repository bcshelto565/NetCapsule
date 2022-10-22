from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20220922100932/https://en.wikipedia.org/wiki/University_of_North_Texas"

page = requests.get(url)        # pulls the url as a request.
soup = BeautifulSoup(page.text, "html.parser")      # uses beautiful soup to parse the "url" for only the html.parser
htmlfile = open("page.html", "w", encoding="utf-8")     # openning the output file // this is not gonna be the final version. Needs to be changed to output 
stringed_page = str(soup)       # turns the soup object into a string to use for the writing to a file.
htmlfile.write(stringed_page)       # writes the string to the file. 