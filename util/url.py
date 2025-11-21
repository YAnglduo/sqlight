from urllib import parse


def parseUrl(url):
    """
    返回路径和查询参数
    目前只支持传统参数
    :param url:
    :return:
    """
    data = parse.urlparse(url)
    base = f"{data.scheme}://{data.netloc}"
    path = data.path
    params = paramsDict(params=data.query)
    return base, path, params
    # return url_path, url_params


def joinUrl(base, path):
    return parse.urljoin(base, path)


def paramsDict(url=None, params=None):
    """
    获取查询参数的字典表达方式(可传递url或查询参数)
    :param url:
    :return:
    """
    if url:
        parsed = parse.urlparse(url)
        query = parsed.query
    else:
        query = params
    params_dict = parse.parse_qs(query)

    return params_dict


def paramsList(path):
    """
    获取查询参数的列表表达方式
    :param path:
    :return:
    """
    parsed = parse.urlparse(path)
    query = parsed.query
    params_dict = parse.parse_qsl(query)

    return params_dict


def toParams(params_dict: dict | list):
    """
    将列表或字典格式转为查询字符串
    :param params_dict:
    :return:
    """
    if type(params_dict) is dict:
        return parse.urlencode(params_dict, doseq=True)
    else:
        return parse.urlencode(params_dict)


def urlPath(url):
    data = parse.urlparse(url)
    url_path = f'{data.scheme}://{data.netloc}{data.path}'
    return url_path
