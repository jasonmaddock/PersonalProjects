import csv


def write_hiscore_row(csvfile, row):
    with open(csvfile, "a+", newline="") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=",",
        )
        writer.writerow(row)


def get_last_page(file):
    try:
        with open(file, "r") as csvfile:
            page = list(csv.reader(csvfile, delimiter=","))[-1:][0][0]
            return int(page)
    except OSError:
        return 0
