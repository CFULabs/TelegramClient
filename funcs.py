def get_direction(acronym: str):
    match acronym:
        case "ПИ":
            return "Программная инженерия"
        case "ИВТ":
            return "Информатика и вычислительная техника"
        case "АТП":
            return "Автоматизация технологических процессов и производств"
        case "ПМИ":
            return "Прикладная математика и инфроматика"
        case "КБ":
            return "Компьютерная безопасность"


def week(mes: str) -> str:
    match mes:
        case "Нечётная":
            return "oddweek"
        case "Чётная":
            return "evenweek"


def day(mes: str) -> str:
    match mes:
        case "Сегодня":
            return "today"
        case "Завтра":
            return "tomorrow"
        case "Понедельник":
            return "monday"
        case "Вторник":
            return "tuesday"
        case "Среда":
            return "wednesday"
        case "Четверг":
            return "thursday"
        case "Пятница":
            return "friday"


def get_full(mes: str) -> dict[str, str]:
    datamap = {}
    datamap['direction'], full_group = mes.split('-')
    datamap['group'], datamap['subgroup'] = full_group[:-1].split('(')
    datamap['direction'] = get_direction(datamap['direction'])
    return datamap
