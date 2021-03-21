### 自动化测试简介

1. UI自动化的本质

   - 定位元素

   - 操作元素

   - 模拟页面动作：不能跨步骤的实现

   - 断言结果：预期结果与实际结果的比对

   - 生成报告：给出结果，False/Pass
   
2. 适合自动化测试场景

   - 需求不会频繁变动
   - UI比较稳定
   - 项目周期较长
   - 大量回归测试任务：敏捷开发，不断添加新功能，之前老给功能不会被轻易改动。
   - 冒烟测试：（针对于新需求）对本次迭代新需求的P0级别case实现自动化。对主干功能进行验证
   - 回归测试：（对老功能的回归）如：1.1.1版本是在1.0版本基础上做的改动，需要测试新功能对老功能是否有影响，可以交给自动化去完成（不断的维护，不断的添加）

问题：之前所在企业自动化覆盖率达到多少？

- 自动化测试覆盖率达到70%左右：项目稳定的，改动小的国企项目，对之前老功能不会有太大的影响，处于稳定期。

- 自动化测试覆盖率达到60%左右：项目周期比较长6个月甚至1年的手机项目，用户界面已经非常稳定，开发都在调试底层（音质，驱动...）

- 自动化测试覆盖率达到30%左右：一个月一个迭代，我们把P0级+一些核心部分的P1级case实现了自动化

- 自动化测试覆盖率达到10-15%左右：两周一个迭代，只做了核心的P0级case自动化

- 核心的几个场景实现了自动化：一周一个迭代，没有回归验证的话，会对用户产生非常大的影响。（核心的场景十几条case）

3. 那些场景不适合做自动化

   - 图片核对类的
   - 视频内容核对类的（音频/画面）
   - 交互性非常强的（通话后要听...）

4. UI自动化测试原则

   - 一个Case完成一个功能点测试：一个自动化用例对应一条手工用例
   - 一个脚本是一个完整的场景：一条完整的手工用例是一个脚本
   - 脚本之间独立，不能有依赖：第一个脚本不会用到之前脚本的功能，不会依赖之前的脚本
   - 设置合适的检查点：用预期结果与实际结果比对
   - 设计良好的框架

5. Selenium的特点

   - 开源，免费：开始的自动化框架可能存在一些bug，开源便于修改
   - 多浏览器支持: FireFox、Chrome（居多）、IE、Opera、 Edge;
   - 多平台支持:Linux . Windows、MAC
   - 多语言支持: Java、Python、Ruby、C#、JavaScript、C++;·对Web页面有良好的支持;
   - 简单（API简单)、灵活（用开发语言驱动）
   - 足够成熟：Selenium经历了三个版本，Selenium 1.0和 Selenium 2.0到现在的selenium3.0。Selenium 不是由单独一个工具构成的，而是由一些插件、类库组成，每个部分都有其特点和应用场景

6. selenium3.x介绍

   - Selenium经历了三个版本，Selenium 1.0和 Selenium 2.0到现在的selenium3.0。Selenium3.x版本最大的变化应该是去掉了Selenium RC，Selenium RC是Selenium1.0的产物，Selenium2.0以WebDriver为主，也使用Selenium RC，到Selenium3.x完全去掉Selenium RC。

   - Selenium3.0中 的Firefox驱动独立了。Selenium3.0之前，Selenium库中移动包含了Firefox浏览驱动，然而，现在Firefox浏览器驱动与Selenium库分离，单独提供下载。

   - Edge 和safari原生驱动的支持

### 环境搭建

```shell
# 安装selenium
pip install selenium  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

下载 chromedriver或geckodriver `https://github.com/mozilla/geckodriver/releases`

```shell
# chrome官网下载
wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip

# 淘宝源（推荐）
wget http://npm.taobao.org/mirrors/chromedriver/2.41/chromedriver_linux64.zip
```

将下载的文件解压，放在如下位置

```shell
unzip chromedriver_linux64.zip

mv chromedriver /usr/bin/
```

给予执行权限

```shell
chmod +x /usr/bin/chromedriver
```



### 八大元素定位法则：

1. id：基于元素属性中的id的值来进行定位

2. name：基于元素属性中的name的值来进行定位

3. link text：主要用于超链接进行定位

4. partial link text：link text的模糊查询版本，类似于数据库的like %。当匹配多个元素的时候，选取第一个元素。

5. classname：基于元素样式测试，易遇到重复内容

6. tagname：用标签来进行定位

7. csselector：应用相对较多的一种行为，完全基于class属性来实现定位

8. xpath：目前应用最多的一种行为，基于页面结构进行定位

   绝对路径：从html根路径下一层一层往下数，找到对应的层级，从而找到元素

   相对路径：基于匹配制度来查找元素，依照xpath语法结构

   - **[] 表示筛选条件（查找函数）**

     如果要基于text来定位元素

     在[]中添加text()="文本内容"进行查找

     例如：//a[text()="登录"]

     //input[contains(@id,'kw')]

   - contains表示进一步查找，匹配项模糊查找

     //input[contains(text(),'包含帅字的元素都是要找的元素')]

     

   **选取节点**

   XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。 下面列出了最有用的路径表达式：

   | 表达式   | 描述                                                       |
   | :------- | :--------------------------------------------------------- |
   | nodename | 选取此节点的所有子节点。                                   |
   | /        | 从根节点选取。                                             |
   | //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
   | .        | 选取当前节点。                                             |
   | ..       | 选取当前节点的父节点。                                     |
   | @        | 选取属性。                                                 |

   | 路径表达式      | 结果                                                         |
   | :-------------- | :----------------------------------------------------------- |
   | bookstore       | 选取 bookstore 元素的所有子节点。                            |
   | /bookstore      | 选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！ |
   | bookstore/book  | 选取属于 bookstore 的子元素的所有 book 元素。                |
   | //book          | 选取所有 book 子元素，而不管它们在文档中的位置。             |
   | bookstore//book | 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。 |
   | //@lang         | 选取名为 lang 的所有属性。                                   |

   **谓语（Predicates）**

   谓语用来查找某个特定的节点或者包含某个指定的值的节点。

   谓语被嵌在方括号中。

   在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

   | 路径表达式                          | 结果                                                         |
   | :---------------------------------- | :----------------------------------------------------------- |
   | /bookstore/book[1]                  | 选取属于 bookstore 子元素的第一个 book 元素。                |
   | /bookstore/book[last()]             | 选取属于 bookstore 子元素的最后一个 book 元素。              |
   | /bookstore/book[last()-1]           | 选取属于 bookstore 子元素的倒数第二个 book 元素。            |
   | /bookstore/book[position()<3]       | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。    |
   | //title[@lang]                      | 选取所有拥有名为 lang 的属性的 title 元素。                  |
   | //title[@lang='eng']                | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。   |
   | /bookstore/book[price>35.00]        | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。 |
   | /bookstore/book[price>35.00]//title | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

   **选取未知节点**

   XPath 通配符可用来选取未知的 XML 元素。

   | 通配符 | 描述                 |
   | :----- | :------------------- |
   | *      | 匹配任何元素节点。   |
   | @*     | 匹配任何属性节点。   |
   | node() | 匹配任何类型的节点。 |

   在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

   | 路径表达式   | 结果                              |
   | :----------- | :-------------------------------- |
   | /bookstore/* | 选取 bookstore 元素的所有子元素。 |
   | //*          | 选取文档中的所有元素。            |
   | //title[@*]  | 选取所有带有属性的 title 元素。   |

   **选取若干路径**

   通过在路径表达式中使用"|"运算符，您可以选取若干个路径。

   在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：R F

   | 路径表达式                       | 结果                                                         |
   | :------------------------------- | :----------------------------------------------------------- |
   | //book/title \| //book/price     | 选取 book 元素的所有 title 和 price 元素。                   |
   | //title \| //price               | 选取文档中的所有 title 和 price 元素。                       |
   | /bookstore/book/title \| //price | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。 |



今天讲的5大定位方式id/name/class_name/link_text/partial_link_text每个写2个代码
xpath的绝对路径定位写5个代码

```python
from selenium import webdriver
from time import sleep

webdriver = webdriver.Firefox()

webdriver.get('https://www.douban.com/')

webdriver.find_element_by_name("q").send_keys('星际穿越')
webdriver.find_element_by_xpath("//span[@class='bn']/input").click()
sleep(2)
webdriver.find_elements_by_link_text("星际穿越")[0].click()
# 获取handles
handles = webdriver.window_handles
# 关闭当前handles
webdriver.close()
# 切换handles
webdriver.switch_to.window(handles[1])
sleep(4)
try:
    webdriver.find_element_by_partial_link_text("当你想描写一个触手可及的").click()
except:
    print("没有定位到元素")
# 等待10秒
sleep(10)
# 释放进程
webdriver.quit()
```



```python
from selenium import webdriver
from time import sleep

webdriver = webdriver.Firefox()

webdriver.get('http://101.133.169.100/yuns/index.php')

# webdriver.find_element_by_name("q").send_keys('星际穿越')
webdriver.find_element_by_link_text("登录").click()

webdriver.find_element_by_name("username").send_keys("1234567")
webdriver.find_element_by_name("password").send_keys("123456")

webdriver.find_element_by_partial_link_text("忘记").click()
sleep(2)

webdriver.find_element_by_class_name("input1").send_keys("123")
webdriver.find_element_by_class_name("input2").send_keys("456")

# 等待10秒
sleep(10)
# 释放进程
webdriver.quit()
```



