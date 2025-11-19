from dataclasses import dataclass


@dataclass
class testData:
    """
    test的数据类
    """
    title: str #标题
    stype: str
    level: str
    risk: str
    clause: list
    where: list
    vector: str
    payload: str
    comment: str
    char: str
    columns: str
    comparison: str
    grep: str
    time: str
    union: str
    dbms: str
    dbms_version: str
    os: str