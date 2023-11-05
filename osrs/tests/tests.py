import csv
import os
import pytest

from web_retriever import grab_page_names, hiscores_retriever
from output_creator import write_hiscore_row, get_last_page
from main import main
from tests.test_vars import NAMES


class TestOutputCreator:
    file = "/home/jason/Jason/PersonalProjects/osrs/tests/test_output.csv"

    def test_write_hiscore_row(self):
        test_row = ["I AM A TEST CELL", "I AM THE SECOND TEST CELL"]

        write_hiscore_row(self.file, test_row)
        with open(self.file, "r") as csvfile:
            last_row = list(csv.reader(csvfile, delimiter=","))[-1:][0]
        assert last_row == test_row

    def test_get_last_page(self):
        test_page = [123456789123456789]
        write_hiscore_row(self.file, test_page)
        last_page = get_last_page(self.file)
        assert last_page == test_page[0]

    def test_get_last_page_error(self):
        last_page = get_last_page("non-existant_test_file.csv")
        assert last_page == 0


class TestWebRetriever:
    def test_grab_page_names(self):
        page = 1
        name_list = grab_page_names(page)
        assert type(name_list) is list
        assert len(name_list) == 25
        assert [type(i) is str for i in name_list]
        assert [len(i) > 0 for i in name_list]

    def test_hiscores_retriever(self):
        name = NAMES[0]
        stats = hiscores_retriever(name)
        print(stats)
        assert len(stats) == 223
        assert stats[0] is name


class TestMain:
    file = "/home/jason/Jason/PersonalProjects/osrs/tests/test_output.csv"

    def test_main(self):
        try:
            os.remove(self.file)
        except OSError:
            pass
        main(output_file=self.file, end_page=3)
        main(output_file=self.file, end_page=5)
        with open(self.file, "r") as csvfile:
            rows = list(csv.reader(csvfile, delimiter=","))
        assert len(rows) == 100
        assert rows[0][0] == "1"
        assert rows[50][0] == "3"
