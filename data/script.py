import json
import yaml


#==============json==================
# data = {"tests": {"suite_1": [],
#                   "suite_2": [],
#                   "suite_3": []}}
#
# заполнение рандомными 10ю значениями suite_1
# for i in range(10):
#     data["tests"]["suite_1"].append(("value", i))
#
# сохранение в заполненых значений в  data.json
# with open("data.json", "w") as f:
#     json.dump(data, f)
#
# чтение файла и вывод в консоль
# with open("data.json", "r") as f:
#     data = json.load(f)
#
# print(data["tests"])
# print(data["tests"].keys())


#====================yaml==================
# чтение json
# with open("data.json", "r") as f:
#     data = json.load(f)
#
# print(data["tests"])
#
# запись прочитаного json в yaml
# with open("data.yaml", "w") as f:
#     yaml.dump(data, f)


with open("data.yaml", "r") as f:
    data = yaml.safe_load(f)

print(data['tests']["suite_2"][0])