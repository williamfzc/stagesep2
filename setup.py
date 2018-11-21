from setuptools import setup, find_packages


setup(
    name='stagesep2',
    version='0.1.1',
    description='detect stages in video',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/stagesep2',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'structlog',
        'numpy',
        'jieba',
        'scikit-image'
    ]
)