from absInterface.payload import IPayloadGenerator


class BooleanTechnology(IPayloadGenerator):
    """拼接test resp与模版"""

    def respPayload(self, value, test, boundary) -> str:
        parts = []
        if value:
            parts.append(value)
        if boundary.prefix:
            parts.append(boundary.prefix)
            parts.append(' ')
        # 添加payload，确保有前导空格
        if test.comparison:
            # 如果payload不以空格开头且前一部分存在且不为空格，添加空格
            if parts and not test.comparison.startswith(' ') and parts[-1] != ' ':
                parts.append(' ')
            parts.append(str(test.comparison))
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