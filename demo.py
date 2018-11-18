# :)
from stagesep2.loader import VideoManager
from stagesep2.analyser import AnalyserRunner
from stagesep2.config import Config


video = VideoManager.add('./temp.avi')

# optional
video.template_manager.add('some_path/template1.png')
video.template_manager.add('some_path/template2.png')

# change config
Config.analyser_list = ['ocr', 'match_template']
Config.output_path = './output.txt'

# start
AnalyserRunner.run()
