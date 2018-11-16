# :)
from stagesep2.loader import VideoManager
from stagesep2.analyser import AnalyserRunner
from stagesep2.config import Config


video1 = VideoManager.add('some_path/video1.mp4')
video2 = VideoManager.add('some_path/video2.mp4')

# optional
video1.template_manager.add('some_path/template1.png')
video2.template_manager.add('some_path/template2.png')

# change config
Config.analyser_list = ['ocr', 'match_template']
Config.output_path = './output.txt'

# start
AnalyserRunner.run()
