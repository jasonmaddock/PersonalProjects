from web_retriever import grab_page_names, hiscores_retriever
from output_creator import write_hiscore_row, get_last_page
import time

output_file = "hiscores.csv"

api_url = (
    "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player="
)
fe_url = (
    f"https://secure.runescape.com/m=hiscore_oldschool_ironman/overall?table=0&page="
)


if __name__ == "__main__":
    page = get_last_page(output_file) + 1
    for i in range(page, 7):
        page_names = grab_page_names(page)
        hiscores = []
        for name in page_names:
            hiscores.append([page] + hiscores_retriever(name))
        for score in hiscores:
            write_hiscore_row(output_file, score)
        print(f"Finished page {page}")
        page += 1
        time.sleep(0.5)
