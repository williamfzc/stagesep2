"""
分析配置存放在此处
支持读取外部json配置
"""
import os
import cv2


class OCRConfig(object):
    lang = 'eng+chi_sim'


class MatchTemplateConfig(object):
    cv_method = 'cv2.TM_CCOEFF_NORMED'


class NormalConfig(object):
    # project root path
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

    # default analyser list (will run)
    ANALYSER_LIST = ['ocr', 'match_template', 'trend']

    # default encoding
    CHARSET = 'utf-8-sig'
