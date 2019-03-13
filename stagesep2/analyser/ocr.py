import jieba
from PIL import Image
from tesserocr import PyTessBaseAPI

from stagesep2.analyser.base import BaseAnalyser
from stagesep2.config import OCRConfig


def content_filter(old_content):
    """ remove unused content and rebuild a word list """
    new_content = old_content.replace(' ', '').replace('\n', '').replace('\r', '')
    return list(jieba.cut(new_content))


class OCRAnalyser(BaseAnalyser):
    """ ocr analyser """

    name = 'ocr'
    TAG = 'OCRAnalyser'
    tesserocr_api = PyTessBaseAPI(lang=OCRConfig.lang)

    @classmethod
    def run(cls, frame, *args, **kwargs):
        """
        run ocr analyser

        :param frame: ndarray
        :return:
        """
        frame = Image.fromarray(frame)
        cls.tesserocr_api.SetImage(frame)
        result = cls.tesserocr_api.GetUTF8Text()

        # content filter
        result = content_filter(result)

        return result
