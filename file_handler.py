import os
from typing import List
import csv


class FileHandler(object):

    _path = "./outputs/"
    _json_file_suffix = "output.json"
    _csv_file_suffix = "output.csv"
    _excel_file_suffix = "output_.xlsx"

    def __init__(self):
        os.makedirs(self._path, exist_ok=True)

    def _get_file_path(self, file_type: str, file_prefix: str) -> str:
        file_path = self._path + file_prefix + "_"
        if file_type == "json":
            file_path = file_path + self._json_file_suffix
        elif file_type == "csv":
            file_path = file_path + self._csv_file_suffix
        elif file_type == "excel":
            file_path = file_path + self._excel_file_suffix
        return file_path

    def create_csv(self, file_prefix: str, collum_titles: List[str], override: bool = True):
        file_path = self._get_file_path("csv", file_prefix)
        file_exist = os.path.exists(file_path)
        if override or (not override and not file_exist):
            with open(file_path, "w+", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(collum_titles)

    def save_csv(self, file_prefix: str, row_list: List[List[str]]):
        file_path = self._get_file_path("csv", file_prefix)
        with open(file_path, "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in row_list:
                writer.writerow(row)

    def get_csv(self, file_prefix: str, with_column_titles: bool = True) -> List[List[str]]:
        line_list = []

        file_path = self._get_file_path("csv", file_prefix)
        with open(file_path, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                line_list.append(row)

        if not with_column_titles:
            line_list.pop(0)

        return line_list

