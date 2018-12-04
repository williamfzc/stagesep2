# :)
from stagesep2 import VideoManager, AnalysisRunner, NormalConfig, OCRConfig


# 添加待测视频
# 虽然能够支持多视频，但还是建议每次只分析一个
video = VideoManager.add('./temp.avi')

# 旋转视频
# 因为拍摄设备的差异，拍摄的视频可能方向是不同预期的，容易导致分析器分析不出有效结果
# 设定该参数能够旋转视频，使分析器可以正常生效
# 逆时针旋转 90 * rotate 度
video.rotate = 3

# 添加match template的样本图
video.template_manager.add('./template.png')

# 分析器列表
# 默认情况下会全选，使用 OCR/模型匹配/首尾帧相似度 进行处理
NormalConfig.ANALYSER_LIST = ['ocr', 'match_template', 'trend']

# 修改OCR的语种
# 默认情况下是英文（tesseract自带了英文）
# 如果使用中文，则需要自行安装tesseract的中文支持包，详见tesseract wiki：
# https://github.com/tesseract-ocr/tesseract/wiki
OCRConfig.lang = 'chi_sim'

# 启动分析
result = AnalysisRunner.run()

# 分析的结果（dict）
dict_data = result.data

# 或者输出到文件内（json）
result.export('./result.json')
