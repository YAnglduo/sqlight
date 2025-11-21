from pathlib import Path
from core.generator import PayloadBoundaryGenerator
from core.labelplace import LabelPlace
from core.matcher import Matcher
from core.technology import BooleanTechnology
from core.xmlprovide import BoundaryProvider, TestProvider





bp = BoundaryProvider()  # 边界模版提供器
tp = TestProvider(Path('data/xml/payload/boolean_blind.xml'))  # 注入模版提供器
match = Matcher()  # 边界与注入模版匹配器
technology = BooleanTechnology()  # 注入边界模版拼接器
label_place = LabelPlace()
generator = PayloadBoundaryGenerator(org_value='ad', test_provide=tp, boundary_provider=bp, matcher=match,
                                     technology=technology, label_place=label_place)
data = generator.generate_compatible_pairs()
for data_p in data:
    print(data_p)
