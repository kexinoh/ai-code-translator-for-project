# Generate DAG graph
This is where the DAG diagram code is generated.
Only by generating a DAG graph can the orderliness of code generation be ensured.
The DAG diagram of project files is also completed using AI, with the following main considerations:;
## Introducing third-party DAG recognition can make the project cumbersome
In most cases, we will use AST to complete the drawing of DAG diagrams, but for a multilingual management tool, it is very difficult to achieve this. You need to prepare AST parsers for all languages to start working.
This will greatly weaken the cross platform and cross language capabilities of the project itself.
## Finding AST packages for py in all languages may also be difficult
For example, it may be difficult for you to find the AST package that parses Lua in Python (probably, I haven't actually looked for it).
Therefore, we use AI to complete DAG rendering.
# method
## 1. Find the import statement
In most languages (possibly all?), importing the corresponding file or inventory in a prominent keyword, such as import in Python, require in Lua, or include in C.
For portability, we do not recommend using absolute addresses when importing, as this will increase the difficulty of AI recognition.
Our first step is to use a simple filter py script to filter the imports contained in each code file in the project and copy them to the temporary folder we have prepared.  
We have prepared a scanconfig.py to define which languages will scan which statements.
## 2. Conduct splicing and generation
All code files will be assigned a unique ID (referring to the specific code file address from the root directory).
Then there will be a dict that stores the corresponding import packages for each code file, similar to DAG dict={"a.py": {b. py, c.py}, "b. py": {c.py}, "c.py": {}}. After we extract c.py, we update DAGdict and delete any c.py present in each code file, making it DAGdict={"a.py": {b. py}, "b. py": {}}. This will help us successfully sort out the order of the files and ultimately import them all into CodeOrder.txt, laying a solid foundation for subsequent analysis.
