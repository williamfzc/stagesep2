from stagesep2.analyser.base import BaseAnalyser
from stagesep2.config import MatchTemplateConfig
from findit import FindIt

fi = FindIt(cv_method_name=MatchTemplateConfig.cv_method)


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'

    @classmethod
    def run(cls, frame, ssv):
        result_dict = dict()
        template_pic_dict = ssv.template_manager.get_dict()

        for each_pic_name, each_pic in template_pic_dict.items():
            fi.load_template(pic_object_list=(each_pic.pic_path, each_pic.cv_object))
            match_result = fi.find(target_pic_object=frame)['data'][0]
            max_val, min_val = match_result['max_val'], match_result['min_val']

            result_dict[each_pic_name] = {
                'min': min_val,
                'max': max_val,
            }
            fi.reset()
        return result_dict
