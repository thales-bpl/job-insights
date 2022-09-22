from functools import lru_cache
import csv


@lru_cache
def read(file_path):
    with open(file_path, mode="r") as file:
        jobs_dict = csv.DictReader(file, delimiter=",")
        jobs_list = [jobs for jobs in jobs_dict]
        # return jobs_list[0]
        return jobs_list


# print(read('./jobs.csv'))
