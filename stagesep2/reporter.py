"""
处理分析结果

应至少支持：
- 文件（json）
- 对象
- 数据库交互
"""
import uuid
import json


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

    __repr__ = __str__


class ResultReporter(object):
    def __init__(self):
        self.result_id = str(uuid.uuid1())
        self.row_list = list()

    def add_row(self, new_row):
        self.row_list.append(new_row)

    def export(self, mode=None):
        # TODO mode: csv/json, file or str
        return self.row_list
