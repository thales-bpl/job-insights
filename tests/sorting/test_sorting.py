from src.sorting import sort_by
from src.jobs import read

jobs = read('src/jobs.csv')


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs[0]['min_salary'] == '19857'
