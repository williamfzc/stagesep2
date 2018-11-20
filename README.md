# stagesep2

[![PyPI version](https://badge.fury.io/py/stagesep2.svg)](https://badge.fury.io/py/stagesep2)

> detect stage in video, a better [stagesep](https://github.com/williamfzc/stagesep)

## 目的

[stagesep](https://github.com/williamfzc/stagesep)是边研究边开发的产物，在代码结构与工程性上都比较随意。

- 虽然它现在运作尚未发现大问题，但是很大程度上限制了可维护性与后续开发的可能
- 带有零碎的内容过多（如阶段分析、首尾帧分析等），而实际上它们的作用不大
- 在API的设计上不够合理

针对上述问题，对整个工程进行了重构，删繁就简。

## 使用

见[demo.py](demo.py)。

## 原理

更多介绍暂时移步[stagesep](https://github.com/williamfzc/stagesep)

## 协议

MIT
