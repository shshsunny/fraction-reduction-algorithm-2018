"""
interface.py
文件I/O接口模块
"""
from json import dumps

# 通用IO接口


def load2D(name):
    with open(name, 'r') as f:
        return eval(f.read())


def dump2D(name, data):
    with open(name, 'w') as f:
        f.write(dumps(data, indent=4))

# dump2D('d.json', {
#     "name": "RD",
#     "size": (1, 1),
#     "value": [(0, 0, 0.0001), (0, 1, 0.0002), (1, 0, 0.0003), (1, 1, 0.0004)]
# })