import yaml
import os

def readyml(yamlPath):
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % yamlPath)
    # open 方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()

    #将其转化为字典形式
    d = yaml.load(cfg, Loader=yaml.FullLoader )
   # print(type(d))
  #  print("读取的测试文件数据： %s" %d)
    return d

if __name__ == '__main__':
    yamlPath = "../data/element.yaml"
    d = readyml(yamlPath)
    print(d['loging'][0]['user'])