from dataclasses import dataclass


@dataclass
class testData:
    """
    test的数据类
    """
    title: str  # 标题
    stype: str  # SQL注入家族类型
    level: str  # 所属登记
    risk: str  # 所属风险
    clause: list  # payload在哪个SQL子句中有效
    where: list  # 可以在哪里添加我们的'<prefix（前缀）> <payload><注释> <suffix（后缀）>'字符串。
    vector: str  # 将用于利用注入点的payload。
    payload: str  # 发起请求1的payload
    comment: str  # 注释符号
    char: str  # 用于在联合查询SQL注入测试中暴力破解列数的字符。
    columns: str  # 在联合查询SQL注入测试中要测试的列数范围。
    comparison: str  # 布尔的盲注SQL注入的第二个请求，为False的请求，与正常请求的对比
    grep: str  # 基于报错的SQL注入所使用的正则表达式
    time: str  # 基于时间的盲注和堆叠查询SQL注入时所指定的时间
    union: str  #
    dbms: str  # 该test对应的dbms
    dbms_version: str  # dbms版本
    os: str  # os版本
