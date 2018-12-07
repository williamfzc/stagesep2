# stagesep2

[![PyPI version](https://badge.fury.io/py/stagesep2.svg)](https://badge.fury.io/py/stagesep2)

Analyse, and convert video into useful data.

## 目的

### 为什么介入图像识别

以下暂时用移动端的例子。

#### UI

现阶段的UI测试大多属于纯代码层面的行为（大多数的实现方案都是基于uiautomator的控件树）。而对于控件是否真的渲染成为我们希望的样子我们并不知晓。

#### 性能

在常规速度类性能测试中通常通过提前埋点进行app层面的测试，这会有两个问题：

- 具有侵入性（需要改动源码）
- 对于界面相关的场景不适用（并不知道界面是否已经被真正渲染出来）

### 图像识别在测试中的应用

一般来说，通过图像识别来进行测试分为三个步骤：

- 图像/视频 采集
    - 这个部分通常由高速摄像机或稳定帧率的外置相机进行拍摄，得到固定帧率的视频
    - 软件录制是不靠谱的，很容易出现帧率不稳定。而如果时间与帧数不能精确对应的话数据会失真

- 视频处理
    - 提取视频中的信息，输出成为我们需要的形式
    - 也是整个流程最关键的部分

- 数据分析
    - 将视频处理的结果进行分析，得到结论或生成报告

该项目将承载视频处理的部分，将录制好的视频解析成开发者需要的格式。

### 与[stagesep](https://github.com/williamfzc/stagesep)相比

stagesep 是边研究边开发的产物，在代码结构与工程性上都比较随意。

- 虽然它现在运作尚未发现大问题，但是很大程度上限制了可维护性与后续开发的可能
- 带有零碎的内容过多，而实际上它们可能作用不大
- 在API的设计上不够合理，难以应用到真实工程中

针对上述问题，对整个工程进行了重构，删繁就简。该项目目前已经真正落地到现实项目中。

## 使用

### 安装

- 基于python3开发
- python2上没试过

```
pip install stagesep2
```

### 安装 tesseract-ocr

如果不想使用ocr，可以用下列方法将其去除：

```python
from stagesep2 import NormalConfig


NormalConfig.ANALYSER_LIST = ['match_template', 'trend']

# default:
# NormalConfig.ANALYSER_LIST = ['ocr', 'match_template', 'trend']
```

安装tesseract及其语言库的方法已经越来越方便，参考[官方文档](https://github.com/tesseract-ocr/tesseract/wiki)

就常规应用而言，OCR达到的效果是相当好的，推荐使用。

> 但该方法由于大量IO会略微降低效率。

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

# draw html report
result.draw('./result_report.html')
```

分析多个视频：

```python
video1 = VideoManager.add('./demo_video.mp4')
video2 = VideoMangaer.add('./demo_video2.mp4')

# 不同视频可以对应不同的模板
video1.template_manager.add('./template1.png')
video2.template_manager.add('./template2.png')

# 运行完的结果会以列表形式出现
result1, result2 = AnalysisRunner.run()
```

更多使用方式，推荐看[demo.py](demo.py)。

### 结果

以 dict/json 形式出现。下面是数据示例：

```
[
    {
        # 本次测试的id
        "result_id": "6778aee8-f7cc-11e8-988d-4a0001b8c310",

        # 视频名称
        "video_name": "./temp.avi",

        # 帧编号
        "frame_id": 1,

        # 帧对应的时间
        "current_time": 0.03333333333333333,

        # ocr分析结果
        # 该列表中出现的文字即该帧中检测出来的文字
        # 已用 jieba分词 进行进一步处理使结果更加合理
        "ocr": [
            "微信",
            "支付宝"
        ],

        # match template分析结果
        # 此处使用的算法是opencv自带的match_template
        # 此处提供了两个值是 cv2.minMaxLoc(res) 的最值
        # 默认算法是 cv2.TM_CCOEFF_NORMED
        # 可以通过 MatchTemplateConfig.cv_method = cv2.TM_SQDIFF_NORMED 修改算法
        # 参考 https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
        "match_template": {
            "template1": {
                "min": -0.19261789321899414,
                "max": 0.1495080292224884
            }
        },

        # 趋势分析结果 分别是
        # 与前一帧的相似程度（0-1）
        # 与视频首尾帧的相似度（0-1）
        # 主要用于鉴定视频从何时进入稳态
        "trend": {
            "previous": 0.456235276681221
            "first": 1,
            "last": 0.9767144457213878
        }
    },

    ...
]
```

## 相关内容

### 依赖

- [opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html): 图像与视频处理
- [tesseract-ocr](https://github.com/tesseract-ocr/tesseract/wiki/Downloads): 文本检测
- [skimage](https://github.com/scikit-image/scikit-image): 主要用于图片相似度比较
- [jieba](https://github.com/fxsjy/jieba)：ocr结果的进一步处理

### 旧版本

- [stagesep](https://github.com/williamfzc/stagesep)
- [利用图像识别与 OCR 进行速度类测试](https://testerhome.com/topics/16063)

## 协议

MIT
