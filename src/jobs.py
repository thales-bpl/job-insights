from functools import lru_cache
import csv


@lru_cache
def read(file_path):
    with open(file_path, mode="r") as file:
        jobs_dict = csv.DictReader(file, delimiter=",")
        jobs_list = [job for job in jobs_dict]
        return jobs_list
        # return jobs_list[0]
        # return list(jobs_dict)


# print(read('./jobs.csv'))
