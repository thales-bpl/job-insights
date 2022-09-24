from .jobs import read


def get_unique_job_types(path: str):
    all_jobs = read(path)
    all_job_types = []
    for job in all_jobs:
        if job["job_type"] not in all_job_types:
            all_job_types.append(job["job_type"])

    return all_job_types


# print(get_unique_job_types('jobs.csv'))


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


def get_unique_industries(path: str):
    all_jobs = read(path)
    all_industry = [job["industry"] for job in all_jobs]
    return list(filter(None, set(all_industry)))

    # all_industry_types = []
    # for job in all_jobs:
    #     if job["industry"] not in all_industry_types:
    #         all_industry_types.append(job["job_type"])

    # return all_industry_types


# print(get_unique_industries('jobs.csv'))


def filter_by_industry(jobs, industry):
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


# print(filter_by_industry(read('jobs.csv'), 'Finance'))


def get_max_salary(path):
    """Get the maximum salary out of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass
    # all_jobs = read(path)
    # all_max_salaries = []
    # for job in all_jobs:
    #     if job["job_type"] not in all_job_types:
    #         all_job_types.append(job["job_type"])

    # return all_job_types
    job_list = read(path)
    all_max_salaries = [job['max_salary'] for job in job_list]
    return int(max(all_max_salaries))
    # min(seq)


# print(get_max_salary('jobs.csv'))


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
