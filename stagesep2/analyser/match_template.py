import cv2

from stagesep2.analyser.base import BaseAnalyser
from stagesep2.config import MatchTemplateConfig


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'

    @classmethod
    def run(cls, frame, ssv):
        result_dict = dict()
        template_pic_dict = ssv.template_manager.get_dict()
        for each_pic_name, each_pic in template_pic_dict.items():
            # TODO match_template not always very match
            res = cv2.matchTemplate(frame, each_pic.cv_object, MatchTemplateConfig.cv_method)
            min_val, max_val, _, _ = cv2.minMaxLoc(res)
            result_dict[each_pic_name] = {
                'min': min_val,
                'max': max_val,
            }
        return result_dict
