# :)
from stagesep2.loader import VideoManager
from stagesep2.executor import AnalysisRunner
from stagesep2.config import NormalConfig


video = VideoManager.add('./temp.avi')

# optional
video.template_manager.add('some_path/template1.png')
video.template_manager.add('some_path/template2.png')

# change config
NormalConfig.analyser_list = ['ocr', 'match_template']
NormalConfig.output_path = './output.txt'

# start
AnalysisRunner.run()
