"""
分析配置存放在此处
支持读取外部json配置
"""
import os


class OCRConfig(object):
    lang = 'eng'


class NormalConfig(object):
    # project root path
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

    # default analyser list (will run)
    ANALYSER_LIST = ['ocr', 'match_template', 'trend']
