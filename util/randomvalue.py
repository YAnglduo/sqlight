import random
import string


def randomNumber():
    """生成随机数字"""
    length = random.randint(1, 4)  #长度
    number_str_list = [str(random.randrange(10)) for _ in range(length)]
    number_int = int(''.join(number_str_list))
    return number_int


def randomString():
    """生成随机字母串"""
    length = random.randint(1, 4)  # 长度范围1-4
    # 从字母表中随机选择字符
    letters = string.ascii_letters  # 包含所有大小写字母
    # 生成指定长度的随机字母串
    random_str = ''.join(random.choice(letters) for _ in range(length))
    return random_str
