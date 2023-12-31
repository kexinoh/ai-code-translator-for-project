# 工业级AI代码翻译系统

在每一个分类下面会有对应的中文readmezh.md，想看具体的模块细节请去相应的文件夹中查看。
## 项目目标：

实现代码之间的自动翻译，涵盖主流编程语言如Java、Python、C++等。
提高代码翻译的准确性，确保语义的一致性和功能的完整性。
为多语言开发团队提供便捷的代码转换工具，促进国际协作。
## 技术路线：

利用先进的自然语言处理技术(你懂的chatgpt)，解析不同编程语言的语法和结构。
建立编程语言间的映射关系，确保代码逻辑和功能的正确转换。
开发友好的用户界面，方便用户上传源代码和接收转换后的代码。
## 预期成果：

一个稳定、高效的代码翻译平台。
支持多种编程语言的互相转换。
显著提升跨语言开发团队的工作效率。
## 项目应用场景：

跨国公司内部的多语言开发协作。
开源社区中不同语言开发者的项目合作。
教育领域中编程语言学习和教学。

# 基本设定

## 1.知识库设定

在语言翻译的过程中必然会引入新的函数以及代码签名的变化。因此要设计一个函数知识库，存储新增或者已经完成的改造，当它进行调用的时候可以识别出具体的类型。

## 2.使用DAG图
对于多文件的项目而言，内部会存在复杂的引用问题，因此使用DAG图设计，可以从低部到顶部来逐步更新，减少依赖冲突。

## 3.使用CFG图
想要准确实现知识库中的代码传入，应该使用CFG图来提取调用的函数，以此保证代码段里面的函数的代码签名都在。

## 4.测试更新

在更新的时候，要同样将测试用例更新，且保证当前层级的测试用例可以正确使用。

因此流程如下：
![image](https://github.com/kexinoh/ai-code-translator-for-project/assets/91727108/589d04da-bd01-4a03-adba-6ed38dd81aea)

## 整体流程
 dag扫描，确定代码读写顺序-->代码更新-->知识库添加-->测试更新
