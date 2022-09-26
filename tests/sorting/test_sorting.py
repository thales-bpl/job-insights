from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    jobs = read('src/jobs.csv')
    sort_by(jobs, 'min_salary')
    assert jobs[0] == '19857'
