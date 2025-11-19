import pathlib
from core.load_payload import load
from encode.payloadencode import getTestDataClass, getBoundaryClass


def boolean_payload(level: str = '5', risk: str = '3'):
    path_lists = pathlib.Path('data/xml/payload').glob('*.xml')
    boundary_path = pathlib.Path('data/xml/boundaries.xml')
    boundary_list = getBoundaryClass(str(boundary_path))
    # print(path_list)
    payload_list = []
    for path in path_lists:
        payloads = getTestDataClass(str(path))
        for payload in payloads:
            if int(payload.risk) > int(risk) or int(payload.level) > int(level):  # 如果危险等级与测试等级大于用户指定的，则不进行测试
                continue
            for boundary in boundary_list:  # 选取模版
                # if int(boundary.level) > int(level):    # 如果模版等级大于指定等级，不进行测试
                #     continue
                for clause in payload.clause:
                    if clause not in boundary.clause:  # 如果payload的clause不在模版中，不进行测试
                        continue
                    for where in payload.where:
                        if where not in boundary.where:  # 如果payload的where不在模版中，不进行测试
                            continue
                        payload_result = load(value='1', prefix=boundary.prefix,
                                              payload=payload.payload, comment=payload.comment,
                                              suffix=boundary.suffix)
                        payload_rep = load(value='1', prefix=boundary.prefix,
                                           payload=payload.comparison, comment=payload.comment,
                                           suffix=boundary.suffix)
                        payload_list.append(payload_result)
                        print(payload_result)
                        print(payload_rep)
                        print("="*20)
        print(len(payload_list))
