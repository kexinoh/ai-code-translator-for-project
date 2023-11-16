#Generate CFG graph
We have just successfully obtained the DAG graph, and we will use a similar method to obtain the CFG graph here.
Why don't we use AST to obtain CFG graphs?
Please review my explanation on GenDAG（ https://github.com/kexinoh/ai-code-translator-for-project/blob/main/src/GenDAG/readme.md ）
#Method
Similarly, we will first use string extraction to complete the preliminary extraction here.
##1. Slice the code section that contains function calls
##2. Extract the code portion that contains function calls
But without AST, slicing becomes very difficult, so during the formal completion process (perhaps other methods will be updated in the future).
I used the GPT in one step to extract the calling part of the code.
