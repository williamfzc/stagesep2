"""
分析器

- OCR
- 特征识别
"""
import cv2

from stagesep2.loader import VideoManager, frame_prepare, SSVideo
from stagesep2.config import NormalConfig
from stagesep2.logger import logger
from stagesep2.reporter import ResultReporter, ResultRow
from stagesep2.utils import *


class AnalysisRunner(object):
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

    @classmethod
    def run(cls) -> (ResultReporter, list):
        analyser_list = check_analyser(NormalConfig.ANALYSER_LIST)
        video_dict = VideoManager.video_dict
        logger.info(cls.TAG, analyser=analyser_list, video=video_dict)

        result_reporter_list = list()
        for each_video_name, each_ssv in video_dict.items():
            result_reporter = ResultReporter(each_video_name)
            cls.analyse_video(each_ssv, analyser_list, result_reporter)
            result_reporter_list.append(result_reporter)

        # export result
        # 如果同时分析多个视频，最终结果是一个装着Reporter的list
        # 如果只分析一个视频，最终结果是一个Reporter
        if len(result_reporter_list) <= 1:
            return result_reporter_list[0]
        return result_reporter_list

    @classmethod
    def analyse_video(cls, ssv_video: SSVideo, analyser_list: list, result_reporter: ResultReporter):
        """ analyse ssv video """
        with video_capture(ssv_video) as each_video:
            ret, frame = each_video.read()
            while ret:
                if not ret:
                    # end of video
                    break

                # prepare frame
                frame = frame_prepare(frame)
                # rotate
                frame = rotate_pic(frame, ssv_video.rotate)

                # current status
                cur_frame_count = int(each_video.get(cv2.CAP_PROP_POS_FRAMES))
                cur_second = each_video.get(cv2.CAP_PROP_POS_MSEC) / 1000

                # new row of result
                new_row = ResultRow(
                    result_reporter.result_id,
                    ssv_video.video_path,
                    cur_frame_count,
                    cur_second,
                )

                for each_analyser in analyser_list:
                    result = each_analyser.run(frame, ssv_video)
                    new_row.add_analyser_result(each_analyser.name, result)

                logger.info(cls.TAG, msg='analysing', **new_row.__dict__)
                result_reporter.add_row(new_row)

                # read new frame
                ret, frame = each_video.read()

        # clean analyser
        for each in analyser_list:
            each.clean()
