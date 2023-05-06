"""
读取接口文件, 返回调用的json参数
"""
from datetime import datetime

import yaml
import json

from lib import utils


class YamlInterface:

    def __init__(self, file, root):
        self.root = root
        self.file = file
        self.barcode = None

    def _read_yaml(self) -> yaml:
        """
        读取yaml文件
        :return: 读取后的yaml值
        """
        with open(self.file, 'r', encoding='utf-8') as yml:
            result = yaml.load(yml, yaml.FullLoader)
        return result

    def interface_json(self):
        """
        生成接口调用的json值
        :return: 完整的json值
        """
        params = self._read_yaml()[self.root]
        self.barcode = params['barcode']
        if self.barcode is None:
            exit(101)
        with open('./interface/safety.yml', 'r', encoding='utf-8') as yml:
            safety = yaml.load(yml, yaml.FullLoader)['SAFETY']
        safety['time'] = datetime.now().strftime('%Y%m%d%H%M%S')
        safety['barcode'] = self.barcode
        # 安全校验节点
        safety['ticket'] = utils.md5_digest('{0}{1}{2}{3}'.format(
            safety['time'], safety['clientcode'], safety['barcode'], safety['username'])
        )
        return f'{{"safety": {json.dumps(safety)}, "params": {json.dumps(params)}}}'


    # def params_json(self):
    #     params = self._read_yaml()[self.root]
    #     self.barcode = params['barcode']
    #     return f'{{{self.interface_json()}, "params": {json.dumps(params)}}}'
