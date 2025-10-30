import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("invalid nb of arguments")

word_to_define = sys.argv[1]

def construct_URL(word):
    return "https://dictionary.cambridge.org/dictionary/english/" + word

# had error 403 without this. found on stackoverflow
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

request = requests.get(construct_URL(word_to_define), headers=headers)

if request.status_code != 200:
    print("something went wrong with the GET req")
    print(request.status_code)

soup = BeautifulSoup(request.text, "html.parser")
key = soup.find("div", class_="def ddef_d db").get_text(" ",strip=True)



print(key)