from abc import ABC, abstractmethod

"""
该类主要用于标签的替换
"""


class ILabelPlace(ABC):
    """
    替换[ORIGINAL] 与 [ORIGVALUE] 标签
    """

    @abstractmethod
    def placeOrin(self, payload: str, orig_value: str) -> str: ...

    """替换RANDNUM标签"""


    @abstractmethod
    def placeNUM(self, payload: str) -> str: ...

    """替换RANDSTR标签"""


    @abstractmethod
    def placeStr(self, payload: str) -> str: ...

    """替换[GENERIC_SQL_COMMENT]标签"""


    @abstractmethod
    def placeComment(self, payload: str) -> str: ...


        # return self.placeOrin(self.placeNUM(self.placeStr(self.placeComment())),value)

    def place(self,payload: str,org_value) -> str:
        d1 = self.placeComment(payload)
        d2 = self.placeStr(d1)
        d3 = self.placeNUM(d2)
        d4 = self.placeOrin(d3,org_value)
        return d4

class IPayloadGenerator(ABC):
    """拼接匹配的test req与模版"""

    def reqPayload(self, value, test, boundary) -> str:
        """拼接test与模版"""
        parts = []
        if value:
            parts.append(value)
        if boundary.prefix:
            parts.append(boundary.prefix)
            parts.append(' ')
        # 添加payload，确保有前导空格
        if test.payload:
            # 如果payload不以空格开头且前一部分存在且不为空格，添加空格
            if parts and not test.payload.startswith(' ') and parts[-1] != ' ':
                parts.append(' ')
            parts.append(str(test.payload))
        # 添加comment，通常需要前导空格
        if test.comment:
            if parts and not test.comment.startswith(' '):
                parts.append(' ')
            parts.append(str(test.comment))
        # 添加suffix，通常需要前导空格
        if boundary.suffix:
            if parts and not boundary.suffix.startswith(' '):
                parts.append(' ')
            parts.append(str(boundary.suffix))
        return ''.join(parts)

    """拼接test resp与模版"""

    @abstractmethod
    def respPayload(self, value, test, boundary) -> str:
        ...
