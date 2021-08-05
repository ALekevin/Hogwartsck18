from setuptools import setup

setup(
    name='pytest_encode_logger',
    url='https://github.com/ALekevin/Hogwartsck18/tree/master/HomeWork/pytest_plugins_Hw_19',
    version='1.0',
    author="kevin",
    author_email='260317442@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode_logger'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode', 'logger'
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest_encode_logger = pytest_encode_logger',
        ]
    },
    #   windows需要的
    zip_safe=False
)
