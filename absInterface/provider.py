from typing import Iterator, Protocol
from dataModel.boundmodel import BoundModel


class ITestProvider(Protocol):
    """Payload提供者接口"""

    def getTests(self, level: int, risk: int) -> Iterator: ...


class IBoundaryProvider(Protocol):
    """Boundary提供者接口"""

    def getBoundaries(self) -> Iterator[BoundModel]: ...


class IPayloadBoundaryMatcher(Protocol):

    """判断模版与test是否匹配"""
    def isCompatible(self, payload, boundary: BoundModel) -> bool: ...
