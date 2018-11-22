# stagesep2

[![PyPI version](https://badge.fury.io/py/stagesep2.svg)](https://badge.fury.io/py/stagesep2)

> detect stage in video, a better [stagesep](https://github.com/williamfzc/stagesep)

## 目的

[stagesep](https://github.com/williamfzc/stagesep)是边研究边开发的产物，在代码结构与工程性上都比较随意。

- 虽然它现在运作尚未发现大问题，但是很大程度上限制了可维护性与后续开发的可能
- 带有零碎的内容过多，而实际上它们可能作用不大
- 在API的设计上不够合理

针对上述问题，对整个工程进行了重构，删繁就简。

## 使用

主要支持 OCR / 模板匹配 / 首尾帧相似度。

提供了用户友好的API供用户调用：

```python
# :)
from stagesep2.loader import VideoManager
from stagesep2.executor import AnalysisRunner
from stagesep2.config import NormalConfig


video = VideoManager.add('./demo_video.mp4')

# 逆时针旋转 90 * rotate 度
video.rotate = 3

# optional
video.template_manager.add('./template1.png')

# change config
NormalConfig.ANALYSER_LIST = ['ocr', 'match_template', 'trend']

# start
result = AnalysisRunner.run()

# analyse it (is a dict)
dict_data = result.data

# or export your result
result.export('./result.json')
```

更多使用方式见[demo.py](demo.py)。

## 原理

更多介绍暂时移步：

- [stagesep](https://github.com/williamfzc/stagesep)
- [利用图像识别与 OCR 进行速度类测试](https://testerhome.com/topics/16063)

## 协议

MIT
