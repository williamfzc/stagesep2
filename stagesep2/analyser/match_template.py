from stagesep2.analyser.base import BaseAnalyser
from stagesep2.config import MatchTemplateConfig
from findit import FindIt
import cv2


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'

    @classmethod
    def run(cls, frame, ssv):
        # check conf
        assert MatchTemplateConfig.cv_method not in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED), 'SQDIFF NOT SUPPORT'

        # init
        fi = FindIt()
        fi.config.cv_method = MatchTemplateConfig.cv_method

        result_dict = dict()
        template_pic_dict = ssv.template_manager.get_dict()

        for each_pic_name, each_pic in template_pic_dict.items():
            fi.template[each_pic.pic_path] = each_pic.cv_object
            match_result = fi.find(target_cv_object=frame)['data'][0]
            max_val, min_val = match_result['max_val'], match_result['min_val']

            result_dict[each_pic_name] = {
                'min': min_val,
                'max': max_val,
            }
        return result_dict
