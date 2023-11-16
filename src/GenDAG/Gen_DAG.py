import os
import json
import requests
import config
def file_content(dir_path):
    str=""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            str+="File path:"+file_path+"\n"
            print("File path:", file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    content = f.read()
                    str += "Content: " + content + "\n"
                    print("Content:  ", content)
                except Exception as e:
                    print("无法读取文件内容: ", e)
            print("\n")

    return str



def GetanswerforAI(question):
    api_key=config.api_key
    api_url=config.api_key

    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data={
        "model":'gpt-3.5-turbo-16k',
        "temperature":0.2,
        "messages":[
            {
                "role":"user",
                "content":question
            }
        ]
    }
    # 示例问题
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        result = response.json()
        print(result)
        print(result['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

    return result['choices'][0]['message']['content']

getDAGprompt=r"""
Please do not return any text other than json, otherwise it will interfere with subsequent analysis.
Please do not provide your thought process and understanding.
You don't need to provide code, just complete the final simple task interface.
All path separators uniformly use "/".
Please analyze several similar code paths and import statements to get the referenced files for each code file, for example:
"File path: mul.py
Content: import sum
File path: pow.py
Content: import mul

File path: sum.py
Content:
", then you return {"mul.py":{"sum.py},"pow.py":{"mul.py},"sum.py":{} }
Below is the task you need to analyze:
"""


def genDAG(dict_obj):
    str=""
    while dict_obj:
        empty_keys = [k for k, v in dict_obj.items() if not v]

        if not empty_keys:
            break

        for key in empty_keys:
            str+=key+"\n"
            del dict_obj[key]

            for v in dict_obj.values():
                v.discard(key)
    return str
if __name__ == '__main__':
    file = file_content(config.temp_file_path)
    DAG = eval(GetanswerforAI(getDAGprompt + file))
    print(genDAG(DAG))
# output such as:
# temp/c.py
# temp/b.py
# temp/a.py
