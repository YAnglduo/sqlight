import pathlib
from lxml import etree
from dataModel.testmodel import testData
from dataModel.boundmodel import BoundModel

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


def getTestDataClass(path:str) -> list[testData]:
    """
    获取全部的test的类的表示方式
    :return:
    """
    parser = etree.XMLParser(encoding="utf-8")
    tree = etree.parse(path, parser=parser)  # 查看解析出的tree的内容
    root = tree.getroot()
    tests = root.findall('test')
    tests_class = []
    for test in tests:
        title = safe_find_text(test, 'title')
        stype = safe_find_text(test, 'stype')
        level = safe_find_text(test, 'level')
        risk = safe_find_text(test, 'risk')
        clause = format_clause(safe_find_text(test, 'clause'))
        where = format_clause(safe_find_text(test, 'where'))
        vector = safe_find_text(test, 'vector')
        request_tree = test.find('request')
        response_tree = test.find('response')
        details_tree = test.find('details')
        request_payload = safe_find_text(request_tree, 'payload')
        request_comment = safe_find_text(request_tree, 'comment')
        request_char = safe_find_text(request_tree, 'char')
        request_columns = safe_find_text(request_tree, 'columns')
        response_comparison = safe_find_text(response_tree, 'comparison')
        response_grep = safe_find_text(response_tree, 'grep')
        response_time = safe_find_text(response_tree, 'time')
        response_union = safe_find_text(response_tree, 'union')
        details_dbms = safe_find_text(details_tree, 'dbms')
        details_dbms_version = safe_find_text(details_tree, 'dbms_version')
        details_os = safe_find_text(details_tree, 'os')
        tests_class.append(testData(title=title, stype=stype, level=level, risk=risk,
                                    clause=clause, where=where, vector=vector,
                                    payload=request_payload, comment=request_comment,
                                    char=request_char, columns=request_columns,
                                    comparison=response_comparison, grep=response_grep,
                                    time=response_time, union=response_union,
                                    dbms=details_dbms, dbms_version=details_dbms_version,
                                    os=details_os))
    return tests_class

def getBoundaryClass(path:str)->list[BoundModel]:
    """
    获取全部模版类
    """
    parser = etree.XMLParser(encoding="utf-8")
    tree = etree.parse(path, parser=parser)  # 查看解析出的tree的内容
    root = tree.getroot()
    boundaries = root.findall('boundary')
    boundaries_class = []
    for boundary in boundaries:
        level = safe_find_text(boundary, 'level')
        clause = format_clause(safe_find_text(boundary, 'clause'))
        where = format_clause(safe_find_text(boundary, 'where'))
        ptype = safe_find_text(boundary, 'ptype')
        prefix = safe_find_text(boundary, 'prefix')
        suffix = safe_find_text(boundary, 'suffix')
        boundaries_class.append(BoundModel(level=level, clause=clause, where=where,
                                           ptype=ptype, prefix=prefix, suffix=suffix))
    return boundaries_class