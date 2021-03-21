### JSON

```txt
概念：一种轻量级数据交换格式；后缀名.json
提示：
	接口测试一般使用JSON为接口传递数据规范格式，所以我们有必要对如何获取JSON数据做个了解
```

#### 5.1 JSON格式

```txt
格式：{"name":"张三","age":28}
提示：由键值对组成，健名和值之间使用分号（:）分割，多个键值对之间使用逗号（,）分割
```

#### 5.2 使用JSON实现三角形案例参数化-操作步骤

```txt
1. 编写JSON文件
2. 编写JSON读取模块函数
3. 单元测试-引用JSON读取函数
4. 执行
```

#### 5.3 难点分析

```txt
1. 导入JSON包（import JSON）
2. 打开JSON文件并解析
	with open('../DataXML/sjx.json','r','encoding='utf-8') as f:
	file=json.load(f)
```

#### 5.4 JSON-总结

```txt
1. JSON概念
2. JSON格式
3. 如何导入JSON包
```



