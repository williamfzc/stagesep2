"""
分析配置存放在此处
支持读取外部json配置
"""
import os


class OCRConfig(object):
    lang = 'eng'


class NormalConfig(object):
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

    analyser_list = ['ocr', 'match_template']
    output_path = './output.json'
