from typing import Iterator

from absInterface.payload import ILabelPlace
from absInterface.provider import IPayloadBoundaryMatcher
from dataModel.boundmodel import BoundModel


class Matcher(IPayloadBoundaryMatcher):
    def __init__(self, payload_process:ILabelPlace =None):
        self.payload_process = payload_process

    def isCompatible(self, payload, boundary: BoundModel) -> bool:
        for clause in payload.clause:
            if clause not in boundary.clause:  # 如果payload的clause不在模版中，不进行测试
                return False
            for where in payload.where:
                if where not in boundary.where:  # 如果payload的where不在模版中，不进行测试
                    return False
            return True


