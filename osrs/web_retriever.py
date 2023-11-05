from bs4 import BeautifulSoup
import requests
import time


api_url = (
    "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player="
)
fe_url = (
    f"https://secure.runescape.com/m=hiscore_oldschool_ironman/overall?table=0&page="
)


def grab_page_names(page):
    x = requests.get(fe_url + str(page))
    while (
        "Due to excessive use of the Hiscore system, your IP has been temporarily blocked"
        in x.text
    ):
        print("sleeping")
        time.sleep(600)
        x = requests.get(fe_url + str(page))

    soup = BeautifulSoup(x.content, "html.parser")
    rows = soup.find("table").find("tbody").findAll("tr")
    page_users = []
    for row in rows:
        cells = row.findAll("td")
        rank = cells[0].getText().replace("\n", "").replace(",", "")
        if not rank:
            continue
        user = cells[1].getText().replace("\n", "").replace("\xa0", " ")
        page_users.append(user)
    if not page_users:
        return
    return page_users


def hiscores_retriever(name):
    req = requests.get(api_url + name)
    stats = [name] + ",".join(req.text.split("\n")[:-1]).split(",")
    return stats
