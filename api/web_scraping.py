import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from cleantext import clean


def get_pd_df(link):
    URL = link
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    archive_links = []
    for link in soup.select('a.title'):
        vol = link.text
        link = link.get('href')
        # split year from the volume eg Vol. 73 (2020)
        year = int(vol[vol.find("(")+1:vol.find(")")])
        if year >= 2020:
            archive_links.append({'year': year, 'link': link})

    papers = []
    for archive in archive_links:
        page = requests.get(archive['link'])
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.select('h3.media-heading a')
        for link in links:
            # clean the title
            title = clean(text=link.text,
                          lower=True,
                          no_line_breaks=False,
                          no_numbers=False,
                          no_punct=False,
                          lang="en")
            papers.append(
                {'year': archive['year'], 'title': title, 'link': link.get('href')})
    df = pd.DataFrame(papers)
    return df
