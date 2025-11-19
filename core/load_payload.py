def load(value: str, prefix: str, payload: str, comment: str, suffix: str) -> str:
    """智能处理空格，避免多余空格"""
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