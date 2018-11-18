"""
分析器

- OCR
- 特征识别
"""
import contextlib
import tempfile
import subprocess
import cv2
import os
import uuid
import platform

from stagesep2.loader import VideoManager
from stagesep2.config import NormalConfig, OCRConfig
from stagesep2.logger import logger
from stagesep2.reporter import ResultReporter, ResultRow


class BaseAnalyser(object):
    name = ''

    @classmethod
    def run(cls, frame):
        return ''


class OCRAnalyser(BaseAnalyser):
    """ ocr analyser """
    name = 'ocr'

    @staticmethod
    def is_windows():
        return platform.system() == 'Windows'

    @classmethod
    def exec_tesseract(cls, src, dst):
        cmd = ['tesseract', src, dst, '-l', OCRConfig.lang]
        need_shell = cls.is_windows()
        tesseract_process = subprocess.Popen(
            cmd,
            shell=need_shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        tesseract_process.communicate(timeout=5)
        if tesseract_process.returncode:
            error_msg = tesseract_process.stderr.read()
            raise RuntimeError('tesseract error: {}'.format(error_msg))

    @classmethod
    def run(cls, frame):
        """
        run ocr analyser

        1. write frame to file
        2. execute tesseract to analyse it
        3. and get its result
        4. delete temp file and return result

        :param frame:
        :return:
        """
        # create temp picture file
        temp_pic = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_pic_path = temp_pic.name
        temp_pic.close()
        # tesseract will auto create result file
        # and add '.txt' after its name!
        temp_result_path = os.path.join(NormalConfig.PROJECT_PATH, str(uuid.uuid1()))
        real_temp_result_path = temp_result_path + '.txt'

        # write in
        cv2.imwrite(temp_pic_path, frame)
        # execute tesseract
        cls.exec_tesseract(temp_pic_path, temp_result_path)
        # get result
        with open(real_temp_result_path, encoding='utf-8') as result_file:
            result = result_file.read()
        # remove temp files
        os.remove(temp_pic_path)
        os.remove(real_temp_result_path)
        return result


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'


ANALYSER_DICT = {
    'ocr': OCRAnalyser,
    'match_template': MatchTemplateAnalyser,
}


def check_analyser(analyser_list):
    """ check if analyser existed, and return list of runnable analyser """
    new_analyser_list = list()
    for each in analyser_list:
        if each not in ANALYSER_DICT:
            raise NotImplementedError('analyser {} not found'.format(each))
        new_analyser_list.append(ANALYSER_DICT[each])
    return new_analyser_list


@contextlib.contextmanager
def video_capture(ssv):
    """ 打开视频的上下文控制 """
    video_cap = cv2.VideoCapture(ssv.video_path)
    yield video_cap
    video_cap.release()


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
    TAG = 'AnalyserRunner'
    result_reporter = ResultReporter()

    @classmethod
    def run(cls):
        analyser_list = check_analyser(NormalConfig.analyser_list)
        video_dict = VideoManager.video_dict
        logger.info(cls.TAG, analyser=analyser_list, video=video_dict)

        for each_video_name, each_ssv in video_dict.items():
            cls.analyse_video(each_ssv, analyser_list)

        # export result
        result = cls.result_reporter.export()
        print(result)

    @classmethod
    def analyse_video(cls, ssv_video, analyser_list):
        """ analyse ssv video """
        with video_capture(ssv_video) as each_video:
            ret, frame = each_video.read()
            while ret:
                if not ret:
                    # end of video
                    break

                # current status
                cur_frame_count = int(each_video.get(cv2.CAP_PROP_POS_FRAMES))
                cur_second = each_video.get(cv2.CAP_PROP_POS_MSEC) / 1000
                logger.info(cls.TAG, msg='analysing', video=ssv_video.video_name, frame=cur_frame_count, time=cur_second)

                # new row of result
                new_row = ResultRow(
                    cls.result_reporter.result_id,
                    ssv_video.video_path,
                    cur_frame_count,
                    cur_second,
                )

                for each_analyser in analyser_list:
                    result = each_analyser.run(frame)
                    new_row.add_analyser_result(each_analyser.name, result)

                cls.result_reporter.add_row(new_row)
                ret, frame = each_video.read()
