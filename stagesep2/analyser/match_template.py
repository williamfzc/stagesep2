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
        result_dict = dict()
        template_pic_dict = ssv.template_manager.get_dict()

        for each_pic_name, each_pic in template_pic_dict.items():
            fi.load_template(each_pic_name, pic_object=each_pic.cv_object)
            match_result = list(fi.find('temp', target_pic_object=frame)['data'].values())[0]['TemplateEngine']
            max_val = match_result['target_sim']

            result_dict[each_pic_name] = {
                # no min any more
                'min': -1,
                'max': max_val,
            }
            fi.clear()
        return result_dict
