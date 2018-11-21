"""
负责资源导入、模块检查
"""
import os
import cv2

from stagesep2.logger import logger
from stagesep2.utils import *


def path_to_name(file_path):
    """ full path -> file name """
    _, name = os.path.split(file_path)
    name, _ = os.path.splitext(name)
    return name


def is_path_existed(file_path):
    """ check if file is existed """
    return os.path.isfile(file_path)


def frame_prepare(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_gray_frame = cv2.medianBlur(gray_frame, 3)
    return blur_gray_frame


class TemplatePicture(object):
    def __init__(self, pic_path):
        if not is_path_existed(pic_path):
            raise FileNotFoundError('file not existed: {}'.format(pic_path))

        self.pic_name = path_to_name(pic_path)
        self.pic_path = pic_path
        self.cv_object = frame_prepare(cv2.imread(self.pic_path))


class TemplateManager(object):
    TAG = 'TemplateManager'
    # match template 需要模板图片
    # 该视频需要的模板图片会被放置在此处
    _match_template_pic_dict = dict()
    # eg:
    # { pic_name: TemplatePicture(pic_path), }

    def add(self, pic_path):
        new_pic = TemplatePicture(pic_path)
        new_pic_name = new_pic.pic_name
        self._match_template_pic_dict[new_pic_name] = new_pic
        logger.info(self.TAG, msg='LOAD PICTURE', path=pic_path, name=new_pic_name)

    def remove(self, pic_name):
        if pic_name in self._match_template_pic_dict:
            del self._match_template_pic_dict[pic_name]
            return True
        logger.warn(self.TAG, msg='no pic named {}'.format(pic_name))
        return False

    def get_dict(self):
        return self._match_template_pic_dict


class SSVideo(object):
    """ video object """

    def __init__(self, video_path):
        if not is_path_existed(video_path):
            raise FileNotFoundError('file not existed: {}'.format(video_path))

        self.video_name = path_to_name(video_path)
        self.video_path = video_path

        # add template example:
        # ssv = SSVideo('some_path/123.mp4')
        # ssv.template_manager.add('some_path/123.png')
        self.template_manager = TemplateManager()

        # degree = rotate * 90, 逆时针
        self._rotate = 0

        # video info
        # total frame count
        self.total_frame = None

        # first and last frame
        self.first_frame = None
        self.last_frame = None

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        if not isinstance(value, int):
            raise TypeError('rotate should be int')
        self._rotate = value
        self.load_video_info()

    def load_video_info(self):
        # TODO need more info?
        # get info from video
        with video_capture(self) as video_src:
            total_frame = video_src.get(cv2.CAP_PROP_FRAME_COUNT)

            _, first_frame = video_src.read()
            video_src.set(1, total_frame - 1)
            _, last_frame = video_src.read()

            # prepare, and rotate
            first_frame, last_frame = [
                frame_prepare(rotate_pic(each, self._rotate))
                for each in (first_frame, last_frame)]

        # init
        self.first_frame = first_frame
        self.last_frame = last_frame
        self.total_frame = total_frame


class VideoManager(object):
    """
    Analyser需要的信息都应该在此处被导入
    例如 作为分析主体的 视频
    例如 match template需要的 模板图片
    """
    TAG = 'VideoManager'

    # 待测视频会被添加到这里
    # 在分析开始时，会遍历此字典
    video_dict = dict()
    # eg:
    # { video_name: SSVideo(video_path), }

    def __init__(self):
        raise NotImplementedError('should not init')

    @classmethod
    def add(cls, video_path):
        new_video = SSVideo(video_path)
        new_video_name = new_video.video_name
        cls.video_dict[new_video_name] = new_video
        logger.info(cls.TAG, msg='LOAD VIDEO', path=video_path, name=new_video_name)
        return new_video

    @classmethod
    def remove(cls, video_name):
        if video_name in cls.video_dict:
            del cls.video_dict[video_name]
            return True
        logger.warn(cls.TAG, msg='no video named {}'.format(video_name))
        return False
