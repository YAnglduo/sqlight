from pathlib import Path
from typing import Iterator
from lxml import etree
from absInterface.provider import IBoundaryProvider, ITestProvider
from dataModel.boundmodel import BoundModel
from dataModel.testmodel import testData
from encode.payloadencode import safe_find_text, format_clause


class BoundaryProvider(IBoundaryProvider):
    """从XML文件加载boundary的实现"""

    def __init__(self, boundary_path: Path = Path('data/xml/boundaries.xml')):
        self.boundary_path = boundary_path

    def getBoundaries(self) -> Iterator[BoundModel]:
        parser = etree.XMLParser(encoding="utf-8")
        tree = etree.parse(self.boundary_path, parser=parser)
        root = tree.getroot()
        boundaries = root.findall('boundary')

        for boundary in boundaries:
            level = safe_find_text(boundary, 'level')
            clause = format_clause(safe_find_text(boundary, 'clause'))
            where = format_clause(safe_find_text(boundary, 'where'))
            ptype = safe_find_text(boundary, 'ptype')
            prefix = safe_find_text(boundary, 'prefix')
            suffix = safe_find_text(boundary, 'suffix')

            yield BoundModel(
                level=level, clause=clause, where=where,
                ptype=ptype, prefix=prefix, suffix=suffix
            )


class TestProvider(ITestProvider):
    """从XML文件加载任意Test的实现"""
    def __init__(self, test_path: Path):
        self.test_path = test_path

    def getTests(self, level: int, risk: int) -> Iterator:
        parser = etree.XMLParser(encoding="utf-8")
        tree = etree.parse(self.test_path, parser=parser)  # 查看解析出的tree的内容
        root = tree.getroot()
        tests = root.findall('test')
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
            yield testData(title=title, stype=stype, level=level, risk=risk,
                           clause=clause, where=where, vector=vector,
                           payload=request_payload, comment=request_comment,
                           char=request_char, columns=request_columns,
                           comparison=response_comparison, grep=response_grep,
                           time=response_time, union=response_union,
                           dbms=details_dbms, dbms_version=details_dbms_version,
                           os=details_os)
