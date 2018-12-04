# stagesep2

[![PyPI version](https://badge.fury.io/py/stagesep2.svg)](https://badge.fury.io/py/stagesep2)

> detect stage in video, a better [stagesep](https://github.com/williamfzc/stagesep)

## 目的

[stagesep](https://github.com/williamfzc/stagesep)是边研究边开发的产物，在代码结构与工程性上都比较随意。

- 虽然它现在运作尚未发现大问题，但是很大程度上限制了可维护性与后续开发的可能
- 带有零碎的内容过多，而实际上它们可能作用不大
- 在API的设计上不够合理，难以应用到真实工程中

针对上述问题，对整个工程进行了重构，删繁就简。现在已经真正落地到现实项目中。

## 使用

### 安装

只在python3上测试通过。

```pip install stagesep2```

### 简单例子

```python
# :)
from stagesep2.loader import VideoManager
from stagesep2.executor import AnalysisRunner


video = VideoManager.add('./demo_video.mp4')

# add template picture
video.template_manager.add('./template1.png')

# start
result = AnalysisRunner.run()

# analyse it (is a dict)
dict_data = result.data

# or export your result
result.export('./result.json')
```

更多使用方式，推荐看[demo.py](demo.py)。

## 原理

更多介绍暂时移步：

- [stagesep](https://github.com/williamfzc/stagesep)
- [利用图像识别与 OCR 进行速度类测试](https://testerhome.com/topics/16063)

## 协议

MIT
