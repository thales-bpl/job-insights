from functools import lru_cache
import csv

@lru_cache
def read(file_path):
    with open(file_path, encoding="utf-8") as file:
        file_read = csv.DictReader(file, delimiter=",")
        csv_file_list = []
        for row in file_read:
            csv_file_list.append(row)

        # print(csv_file_list[0])
        return csv_file_list


# read('src/jobs.csv')