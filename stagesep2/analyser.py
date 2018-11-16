"""
分析器

- OCR
- 特征识别
"""
from stagesep2.loader import VideoManager
from stagesep2.config import Config


class OCRAnalyser(object):
    @classmethod
    def run(cls):
        pass


class MatchTemplateAnalyser(object):
    @classmethod
    def run(cls):
        pass


ANALYSER_DICT = {
    'ocr': OCRAnalyser,
    'match_template': MatchTemplateAnalyser,
}


def check_analyser(analyser_list):
    new_analyser_list = list()
    for each in analyser_list:
        if each not in ANALYSER_DICT:
            raise NotImplementedError('analyser {} not found'.format(each))
        new_analyser_list.append(ANALYSER_DICT[each])
    return new_analyser_list


class AnalyserRunner(object):
    """
    主要逻辑

    - 从VideoManager中导入视频对象
    - 从config中读取需要使用的Analyser
    - 遍历视频列表
        - 切割视频，遍历帧
            - 用不同的Analyser分析帧
            - 记录结果
    - 将结果传递给reporter进行处理
    """

    @classmethod
    def run(cls):
        analyser_list = check_analyser(Config.analyser_list)
        video_dict = VideoManager.video_dict

        for each_video_name, each_video in video_dict.items():
            pass
