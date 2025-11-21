import re
from absInterface.payload import ILabelPlace
from util.randomvalue import randomNumber, randomString


class LabelPlace(ILabelPlace):

    def placeOrin(self, payload: str, orig_value: str) -> str:
        if '[ORIGINAL]' in payload:
            payload = payload.replace('[ORIGINAL]', orig_value)
        if '[ORIGVALUE]' in payload:
            if orig_value.isdigit():  # 防止不是数字时也被直接拼接到sql语句中导致sql语句出错
                payload = payload.replace('[ORIGVALUE]', orig_value)
            else:
                payload = payload.replace('[ORIGVALUE]', f'\'{orig_value}\'')
        return payload


    def placeNUM(self, payload: str) -> str:
        """
        替换NUMBER
        """
        for _ in set(re.findall(r"(?i)\[RANDNUM(?:\d+)?\]", payload)):
            payload = payload.replace(_, str(randomNumber()))
        return payload


    def placeStr(self, payload: str) -> str:
        """
        替换randstr
        """
        for _ in set(re.findall(r"(?i)\[RANDSTR(?:\d+)?\]", payload)):
            payload = payload.replace(_, randomString())

        return payload


    def placeComment(self, payload: str) -> str:
        if '[GENERIC_SQL_COMMENT]' in payload:
            payload = payload.replace('[GENERIC_SQL_COMMENT]', '-- [RANDSTR]')
        return payload

