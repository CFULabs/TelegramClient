"""Modules"""
from work_with_api import *

def name_group(string: str) -> str:
    """
    Пытается привести невернно введенную пользователем группу. \n
    В нормальную для ввода.
    """
    string = string.upper()
    string = string.replace("-Б-О-", "-")
    string = string.replace("-Б-", "-")
    string = string.replace("-О-", "-")


def find_group(provider: str, group_name: str) -> dict[str]:
    """
    Пытается найти группу, возвращает массив вариантов
    """
    arr = get_groups(provider)
    name = group_name.split('-')[0].upper() + "".join(f"{i.lower()}" for i in group_name.split('-')[1:])
    name = name.replace("бо", "-б-о-")
    print(name)
