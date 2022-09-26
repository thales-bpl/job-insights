from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = {'title': 'Maquinista', 'salario': 2000, 'tipo': 'trainee'}
    assert read_brazilian_file('tests/mocks/brazilians_jobs.csv')[0] == result
