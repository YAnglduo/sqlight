# sqlight
轻量化sql漏洞检测_毕设代码，20251119开始设计。哪位大佬可以指点一二


# 更新日志
- 20251119：将代码转移至对应目录
- 20251120: 实现了payload生成逻辑


# 设计想法
每个sql类型都有其对应的xml文件，每个xml文件都有request和response，但是类型不同的sql注入其response也是不同的。所以应该使用函数的方法，写每个sql类型的payload生成与request和response的处理逻辑然后再一个个调用。还是做一个抽象类，让每个类都实现payload生成，request处理，response处理以及检测逻辑。最后在使用依赖注入？？？

# 缺陷
- 代码结构混乱
- 无框架、无设计思路