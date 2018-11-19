# :)
from stagesep2.loader import VideoManager
from stagesep2.executor import AnalysisRunner
from stagesep2.config import NormalConfig


video = VideoManager.add('./demo_video.mp4')

# 逆时针旋转 90 * rotate 度
video.rotate = 3

# optional
video.template_manager.add('./template3.png')

# change config
NormalConfig.analyser_list = ['ocr', 'match_template']
NormalConfig.output_path = './output.txt'

# start
AnalysisRunner.run()
