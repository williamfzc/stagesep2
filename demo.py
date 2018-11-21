# :)
from stagesep2.loader import VideoManager
from stagesep2.executor import AnalysisRunner
from stagesep2.config import NormalConfig


video = VideoManager.add('./temp.avi')

# 逆时针旋转 90 * rotate 度
video.rotate = 3

# optional
video.template_manager.add('./template.png')

# change config
NormalConfig.ANALYSER_LIST = ['ocr', 'match_template', 'trend']

# start
result = AnalysisRunner.run()

# analyse it (is a dict)
dict_data = result.data

# or export your result
result.export('./result.json')
