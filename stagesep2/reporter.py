"""
处理分析结果

应至少支持：
- 文件（json）
- 对象
- 数据库交互
"""
import uuid
import json
import os

from stagesep2.logger import logger
from stagesep2.painter import ReportPainter


class ResultRow(object):
    def __init__(
        self,
        # must
        result_id,
        video_name,
        frame_id,
        current_time,
    ):
        # task id
        self.result_id = result_id
        # video name (id), a task may contains more than one video
        self.video_name = video_name
        # current frame number
        # 当前的结果对应的帧编号
        self.frame_id = frame_id
        # current time
        # 当前的结果对应的帧，在视频中对应的时间
        self.current_time = current_time

    def add_analyser_result(self, name, result):
        """
        add result of analyser

        :param name: analyser name
        :param result: result of analyser
        :return:
        """
        # analyse result
        # ocr: list, eg: ['some_word', 'other_word']
        # match_template: dict, eg: {'pic1': 0.85, 'pic2': 0.90}

        self.__dict__[name] = result

    def __str__(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__

    __repr__ = __str__


class ResultReporter(object):
    TAG = 'ResultReporter'

    def __init__(self, video_name):
        self.video_name = video_name
        self.result_id = str(uuid.uuid1())
        self._row_list = list()

    def add_row(self, new_row):
        self._row_list.append(new_row)

    def export(self, file_path):
        """ export result to json file. Path can be file, dir. """

        # check file path
        if os.path.isfile(file_path):
            logger.warn(self.TAG, msg='File "{}" already existed'.format(file_path))
            file_path = os.path.join(os.path.dirname(file_path), self.result_id + '.json')
        elif os.path.isdir(file_path):
            logger.warn(self.TAG, msg='Path "{}" is a directory'.format(file_path))
            file_path = os.path.join(file_path, self.result_id + '.json')

        # write file
        with open(file_path, 'w+') as json_file:
            json_file.write(str(self.data))
            logger.info(self.TAG, msg='Result saved in "{}"'.format(file_path))

    @property
    def data(self):
        """ return data, consisted by pyobject """
        return self._row_list

    def draw(self, dst):
        """ draw analysis report to file named dst """
        ReportPainter.draw_with_json(str(self.data), dst)
