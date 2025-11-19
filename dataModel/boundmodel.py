from dataclasses import dataclass


@dataclass
class BoundModel:
    level: str  # 等级
    clause: list  # payload在哪个SQL子句中有效
    where: list  # 含义通testmodel
    ptype: str  # 含义通testmodel
    prefix: str  # 前缀
    suffix: str  # 后缀
