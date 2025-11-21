from typing import Optional, Iterator

from absInterface.payload import IPayloadGenerator
from absInterface.provider import ITestProvider, IBoundaryProvider, IPayloadBoundaryMatcher
from core.labelplace import LabelPlace


class PayloadBoundaryGenerator:
    """
    使用依赖注入的生成器类
    通过构造函数注入所有依赖
    """

    def __init__(
            self,
            org_value,
            test_provide: ITestProvider,  # test模版
            boundary_provider: IBoundaryProvider,  # 边界模版
            technology: IPayloadGenerator,  # 具体注入技术的payload生成器
            matcher: Optional[IPayloadBoundaryMatcher],  # 匹配器
            label_place:LabelPlace

    ):
        self.org_value = org_value
        self.test_provide = test_provide
        self.boundary_provider = boundary_provider
        self.matcher = matcher
        self.technology = technology
        self.label_place = label_place

    def generate_compatible_pairs(
            self,
            level: int = 1,
            risk: int = 5
    ) -> Iterator:
        """
        生成兼容的payload-boundary对
        这是主要的业务逻辑方法
        """
        for test in self.test_provide.getTests(level, risk):  # 获取test模块
            for boundary in self.boundary_provider.getBoundaries():  # 获取模版
                if self.matcher.isCompatible(test, boundary):  # 判断模块与模版是否匹配
                    req_payload = self.technology.reqPayload(self.org_value, test, boundary)  # 1 req进行拼接
                    place_payload = self.label_place.place(req_payload,self.org_value)
                    # 2 resp 拼接
                    yield place_payload
