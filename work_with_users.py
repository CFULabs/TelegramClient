"""Modules"""
import re
from work_with_api import get_groups


def find_group(provider: str, group_name: str) -> dict[str]:
    """
    Пытается найти группу, возвращает массив возможных вариантов
    """
    res = []
    res_2 = []
    arr = get_groups(provider)
    name = group_name.split('-')[0].upper() + "".join(f"{i.lower()}" for i in group_name.split('-')[1:])
    name = name.replace("бо", "-б-о-")
    name = re.sub(r'(?<=[A-Za-zА-Яа-я])(?=\d)|(?<=\d)(?=[A-Za-zА-Яа-я])', '-б-о-', name)
    name_pref = f"{name}-".split("-")[0]
    num_group = f"{name}-".split("-")[-2]
    num_group = re.sub(r'\(.*?\)', '', num_group)
    print(name, name_pref, num_group)
    for i in arr:
        if i["name"] == name:
            return [i]
        elif (name_pref in i["name"]) and (num_group in i["name"]):
            res.append(i)
        elif name_pref in i["name"]:
            res_2.append(i)
    return res if len(res)>0 else res_2
