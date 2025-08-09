"""
json.loads:将json数据转换为python数据格式
json.dumps:将python数据转换为json数据格式

"""

#导入json
import json

# 加载数据
with open('datas.json','r',encoding='utf-8') as f:
    j_data = f.read()
    print(j_data)

    # 将json数据转换为python数据格式
    py_data = json.loads(j_data)
    print(py_data)

datas2 = {"name": "张三",
          "age": "18",
          "skill": ["python","html","css","js","java"],
          "isDelete": True,
          "isActive": False,
          "addr": None
          }

# 将python数据转换为json数据格式
json_data2 = json.dumps(datas2,ensure_ascii=False,indent=4)
print(json_data2)

# 写入文件
with open("datas.json",'w',encoding='utf-8') as f:
    f.write(json_data2)