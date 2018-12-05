class BaseAnalyser(object):
    name = ''

    @classmethod
    def run(cls, *args, **kwargs):
        """
        normally,

        1. frame (opencv image object)
        2. ssv (provide necessary info, eg: template pictures)

        :param args:
        :param kwargs:
        :return:
        """
        return ''

    @classmethod
    def clean(cls, *args, **kwargs):
        """
        clean Analyser config after usage

        :param args:
        :param kwargs:
        :return:
        """
