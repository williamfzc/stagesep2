from setuptools import setup, find_packages


setup(
    name='stagesep2',
    version='0.2.3',
    description='Analyse, and convert video into useful data.',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/stagesep2',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'opencv-python',
        'structlog',
        'numpy',
        'jieba',
        'scikit-image',
        'pyecharts',
        'pyecharts_snapshot',
        'findit',
        'tesserocr',
        'Pillow',
    ]
)
