# 生成CFG图

刚刚我们已经成功获取了DAG图，我们这里将会使用类似的方法来获取CFG图。  

为什么我们不使用AST来获取CFG图？  

请查看我在GenDAG的解释（https://github.com/kexinoh/ai-code-translator-for-project/blob/main/src/GenDAG/readmezh.md）

# 方法
同样，我们这里会先使用字符串提取来完成初步提取。
## 1.对存在函数调用的代码部分进行切片
## 2.对存在函数调用的代码部分进行提取
但是没有AST的话，切片都变得十分困难，因此在正式完成的过程中（也许未来会更新其他方法）。  
我使用的GPT一步到位，让它提取代码的调用部分。
