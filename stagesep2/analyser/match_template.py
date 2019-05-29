from stagesep2.analyser.base import BaseAnalyser
from stagesep2.config import MatchTemplateConfig
from findit import FindIt

fi = FindIt(
    engine=['template'],
    cv_method_name=MatchTemplateConfig.cv_method,
)


class MatchTemplateAnalyser(BaseAnalyser):
    """ match-template analyser """
    name = 'match_template'

    @classmethod
    def run(cls, frame, ssv):
        template_pic_dict = ssv.template_manager.get_dict()
        for each_pic_name, each_pic in template_pic_dict.items():
            fi.load_template(each_pic_name, pic_object=each_pic.cv_object)

        match_result = fi.find(
            'temp',
            target_pic_object=frame,
            engine_template_scale=(1, 2, 5)
        )['data']

        result_dict = dict()
        for each_pic_name, each_pic_result in match_result.items():
            result_dict[each_pic_name] = {
                # no min any more
                'min': -1,
                'max': each_pic_result['TemplateEngine']['target_sim'],
            }
        fi.clear()
        return result_dict
