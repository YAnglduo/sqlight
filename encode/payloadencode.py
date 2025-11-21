from lxml import etree


def safe_find_text(element: etree._Element, tag_name: str, default=None) -> str | None:
    """安全地查找标签并获取文本内容"""
    if element is None:
        return default
    found = element.find(tag_name)
    return found.text if found is not None else default


def format_clause(data: str) -> list:
    """
    标准化clause和where，将，或-分隔的字符串转为数组
    :param data:
    :return:
    """
    if '-' in data:
        data = data.split('-')
        data = [i for i in range(int(data[0]), int(data[1]))]
    elif ',' in data:
        data = data.split(',')
    else:
        data = [data]
    return data
