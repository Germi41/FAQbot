import csv
import requests
import sys
from bs4 import BeautifulSoup

def main():
    url = "https://kiwi.aicheck.tech/web/"
    payload = {
        'inUserName': 'pilot',
        'inUserPass': 'P1l0TNotSoVeryLongPassword'
    }

    with requests.Session() as s:
        p = s.post(url, data=payload)
        # print the html returned or something more intelligent to see if it's a successful login page.
        # print p.text