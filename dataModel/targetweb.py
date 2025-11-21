class TargetWeb:
    def __init__(self, base:str, path:str, params:dict|str):
        self.path_injection:dict|None = None
        self.ua = None  # Ua头
        self.cookie = None  # Cookie
        self.header = None  # 表头
        self.json = None  # json类型数据
        self.data = None  # data类型数据
        self.base = base  # 根url
        self.path = path  # Path
        self.params = params
        self.method = 'GET'
        self.check = []  # 已测试的参数列表

    def setData(self, data, type='json'):
        if type == 'form':
            self.data = data
        elif type == 'json':
            self.json = data

    def setHeader(self, header):
        self.header = header

    def setCookie(self, cookie):
        self.cookie = cookie

    def setUa(self, ua):
        self.ua = ua

    def findInjection(self):
        keys = [key for key in self.params.keys()]
        path_list = self.path.split('/')
        path_add = {}
        for i,path in enumerate(path_list):
            if path == '':
                pass
            if path.isdigit():
                path_add[i] = path
        self.path_injection = path_add


    def joinPayload(self,func):
        # path1 = self.path.split('/')
        for key,value in self.params.items():
            if key in self.check:
                continue
            payload_list = func(value[0])
            yield payload_list

        if self.path_injection is None:
            self.findInjection()
        # for key,value in self.path_injection.items():
        #     path1[key] = func(value)


