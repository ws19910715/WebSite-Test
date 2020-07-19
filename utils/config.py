import os
from utils.readyaml import readyml
import time
picture_time = time.strftime("%Y-%m-%d-%H_%M", time.localtime(time.time()))
image_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'image/')
element_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data/element.yaml')
d=readyml(element_path)
url="https://txqa.ziyun-cloud.com/factoryPortal/"
pt_user='于洪涛'
pt_password='156789'


print(d)

