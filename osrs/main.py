from web_retriever import grab_page_names, hiscores_retriever
from output_creator import write_hiscore_row, get_last_page
import time

output_file = "hiscores.csv"


def main(output_file=output_file, end_page=54000):
    page = get_last_page(output_file) + 1
    for i in range(page, end_page):
        page_names = grab_page_names(page)
        hiscores = []
        for name in page_names:
            hiscores.append([page] + hiscores_retriever(name))
        for score in hiscores:
            write_hiscore_row(output_file, score)
        print(f"Finished page {page}")
        page += 1
