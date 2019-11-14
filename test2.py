from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

my_url = 'https://news.ycombinator.com/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("tr", {"class": "athing"})
containers_cc = page_soup.findAll("td", {"class": "subtext"})

title_list = []
comment_list = []
author_list = []
karma_list = []

# ----------to find the title-----------#
for container in containers:
    main_title = container.findAll("a", {"class": "storylink"})

    title = main_title[0].text
    title_list.append(title)

print(title_list)

# ----------to find the comment_count and author-----------#

for container_cc in containers_cc:
    sub_title = container_cc.findAll("a")

    comment_count = sub_title[3].text
    comment_list.append(comment_count)

    author = sub_title[0].text
    author_list.append(author)

# ----------to find the karma points-----------#
#     author_url = 'https://news.ycombinator.com/user?id='+author
#
#     uClient_auth = uReq(author_url)
#     author_html = uClient_auth.read()
#     uClient_auth.close()
#     page_auth = soup(author_html,"html.parser")
#
#     containers_ath = page_auth.findAll("td")
#     # print(len(containers_ath))
#     # print(containers_ath)
#
#     karma = containers_ath[-9].text.strip()
#     karma_list.append(karma)

print(comment_list)
print(author_list)
# print(karma_list)


# ----------creating dataframe-----------#
dict = {'Title': title_list, 'Comments': comment_list, 'Author': author_list}

df = pd.DataFrame(dict)
export_excel = df.to_excel (r'D:\Projects\test_project\export_dataframe.xlsx', index = None, header=True)

#changes3