"""
负责资源导入、模块检查
"""
from stagesep2.logger import logger


class TemplatePicture(object):
    def __init__(self, pic_path):
        # should contains:
        # self.pic_name
        # self.pic_path
        # self.cv_object
        pass


class TemplateManager(object):
    TAG = 'TemplateManager'
    # match template 需要模板图片
    # 该视频需要的模板图片会被放置在此处
    _match_template_pic_dict = dict()
    # eg:
    # { pic_name: TemplatePicture(pic_path), }

    def add(self, pic_path):
        logger.info(self.TAG, msg='load pic', path=pic_path)

    def remove(self, pic_name):
        pass


class SSVideo(object):
    """ video object """

    def __init__(self, video_path):
        self.video_path = video_path
        self.template_manager = TemplateManager()

    # add template example:
    # ssv = SSVideo('some_path/123.mp4')
    # ssv.template_manager.add('some_path/123.png')


class VideoManager(object):
    """ singleton """
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
        cls.video_dict[new_video] = new_video
        logger.info(cls.TAG, msg='load video', path=video_path)
        return new_video

    @classmethod
    def remove(cls, video_name):
        pass
