from .jobs import read


def get_unique_job_types(path: str):
    all_jobs = read(path)
    all_job_types = []
    for job in all_jobs:
        if job["job_type"] not in all_job_types:
            all_job_types.append(job["job_type"])

    return all_job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


def get_unique_industries(path: str):
    all_jobs = read(path)
    all_industry = [job["industry"] for job in all_jobs]
    return list(filter(None, set(all_industry)))


def filter_by_industry(jobs, industry):
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


def get_max_salary(path):
    job_list = read(path)
    all_max_salaries = [
        int(job['max_salary'])
        for job in job_list
        if job["max_salary"].isnumeric()
        ]
    return max(all_max_salaries)


def get_min_salary(path):
    job_list = read(path)
    all_max_salaries = [
        int(job['min_salary'])
        for job in job_list
        if job["min_salary"].isnumeric()
        ]
    return min(all_max_salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("'min_salary' or 'max_salary' is undefined")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("'min_salary' and 'max_salary' must be integer")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("'min_salary' is greater than 'max_salary'")
    elif type(salary) != int:
        raise ValueError("'salary' must be an integer")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_in_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_in_range.append(job)
        except ValueError:
            print("Some job has invalid data")
    return jobs_in_range
