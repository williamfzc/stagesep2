import cv2

from stagesep2.analyser.base import BaseAnalyser


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'

    @classmethod
    def run(cls, frame, ssv):
        result_dict = dict()
        template_pic_dict = ssv.template_manager.get_dict()
        for each_pic_name, each_pic in template_pic_dict.items():
            # TODO match_template not always very match
            res = cv2.matchTemplate(frame, each_pic.cv_object, cv2.TM_SQDIFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)
            result_dict[each_pic_name] = max_val
        return result_dict
