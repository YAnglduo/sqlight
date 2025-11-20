import re

from util.randomvalue import randomNumber, randomString


def load(value: str, prefix: str, payload: str, comment: str, suffix: str) -> str:
    """进行payload的拼接"""
    parts = []
    if value:
        parts.append(value)
    if prefix:
        parts.append(prefix)
        parts.append(' ')
    # 添加payload，确保有前导空格
    if payload:
        # 如果payload不以空格开头且前一部分存在且不为空格，添加空格
        if parts and not payload.startswith(' ') and parts[-1] != ' ':
            parts.append(' ')
        parts.append(str(payload))
    # 添加comment，通常需要前导空格
    if comment:
        if parts and not comment.startswith(' '):
            parts.append(' ')
        parts.append(str(comment))
    # 添加suffix，通常需要前导空格
    if suffix:
        if parts and not suffix.startswith(' '):
            parts.append(' ')
        parts.append(str(suffix))

    return ''.join(parts)


def place(value:str,orig_value:str)->str:
    """
    完整的替换流程
    """
    value = placeOrin(placeStr(placeNUM(placeComment(value))),orig_value)
    return value
def placeOrin(value:str,orig_value:str)->str:
    #替换原值标签。
    if '[ORIGINAL]' in value:
        value = value.replace('[ORIGINAL]', orig_value)
    if '[ORIGVALUE]' in value:
        if orig_value.isdigit(): # 防止不是数字时也被直接拼接到sql语句中导致sql语句出错
            value = value.replace('[ORIGVALUE]', orig_value)
        else:
            value = value.replace('[ORIGVALUE]', f'\'{orig_value}\'')
    return value
def placeNUM(value: str) -> str:
    """
    替换NUMBER
    """
    for _ in set(re.findall(r"(?i)\[RANDNUM(?:\d+)?\]", value)):
        value = value.replace(_, str(randomNumber()))
    return value


def placeStr(value: str) -> str:
    """
    替换randstr
    """
    for _ in set(re.findall(r"(?i)\[RANDSTR(?:\d+)?\]", value)):
        value = value.replace(_, randomString())

    return value

def placeComment(value: str) -> str:
    if '[GENERIC_SQL_COMMENT]' in value:
        value = value.replace('[GENERIC_SQL_COMMENT]', '-- [RANDSTR]')
    return value