"""
分析配置存放在此处
支持读取外部json配置
"""


class Config(object):
    analyser_list = ['ocr', 'match_template']
    output_path = './output.json'
