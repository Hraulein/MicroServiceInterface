import hashlib


def md5_digest(_str: str) -> str:
    """
    将字符串以md5形式加密
    :param _str: 需要加密的字符串
    :rtype: str
    :return: 加密后的md5字符串
    """
    md5 = hashlib.md5()
    md5.update(_str.encode('utf-8'))
    return md5.hexdigest()
