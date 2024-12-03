"""Need for parsing"""
import requests


def get_providers() -> dict[str]:
    """
    Ничего не принимает. \n
    Возвращает все универы/структурные  подразделения кфу, \n
    если может получить доступ к api иначе возвращает None
    """
    req = requests.get("http://sanyapilot.ru:10010/providers", timeout=1000)
    return req.json() if req.status_code == 200 else None


def get_groups(provider: str) -> dict[str]:
    """
    Возвращает все группы в данном структурном подразделении кфу.\n 
    Если такого подразделения не найденно возвращает None.
    """
    req = requests.get(f"http://sanyapilot.ru:10010/{provider}/groups", timeout=1000)
    return req.json() if req.status_code == 200 else None


def get_group(provider: str, group_id: int) -> dict[str]:
    """
    Возвращает расписание для данной конкретной группы. \n
    Если ничего не нашел или запрос не  удался возвращает None
    """
    req = requests.get(f"http://sanyapilot.ru:10010/{provider}/{group_id}", timeout=1000)
    return req.json() if req.status_code == 200 else None
