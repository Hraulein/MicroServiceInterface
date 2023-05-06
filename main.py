"""
MicroServiceInterface
1. 读取yaml配置文件, 获取接口api信息
    1.1
2. 调用接口api, 获取接口返回信息
    2.1

"""
from lib import utils, interface
from datetime import datetime

if __name__ == '__main__':
    # interface_safety = interface.YamlInterface('interface/safety.yml', 'SAFETY')
    # print(interface.YamlInterface.interface_safety())
    # time = datetime.now().strftime('%Y%m%d%H%M%S')
    # print(time)
    # print(interface_safety.safety_json('TEST001'))
    # print(utils.md5_digest('20200819154300EESasdasdA0030016'))
    # print(interface.YamlInterface.safety_json())
    params = interface.YamlInterface('./interface/createImagePath.yml', 'PARAMS')
    print(params.interface_json())
