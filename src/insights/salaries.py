from typing import Union, List, Dict
# from src.insights.jobs import read
from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

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
    try:
        all_jobs = read(path)
        all_max_salaries = set()
        for job in all_jobs:
            all_max_salaries.add(job["max_salary"])
        all_max_salaries = ' '.join(all_max_salaries).split()
        all_max_salaries_valid = set()
        for salary in all_max_salaries:
            all_max_salaries_valid.add(int(salary))
        return (max(all_max_salaries_valid))
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found file: {path}")


def get_min_salary(path: str) -> int:
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
    try:
        all_jobs = read(path)
        all_min_salaries = set()
        for job in all_jobs:
            all_min_salaries.add(job["min_salary"])
        all_min_salaries = ' '.join(all_min_salaries).split()
        all_min_salaries_valid = set()
        for salary in all_min_salaries:
            all_min_salaries_valid.add(int(salary))
        return (min(all_min_salaries_valid))
    except FileNotFoundError:
        raise FileNotFoundError(f"Not found file: {path}")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
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
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
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
    raise NotImplementedError
