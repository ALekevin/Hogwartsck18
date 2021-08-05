from setuptools import setup

setup(
    name='pytest_encode_logger',
    url='https://github.com/ALekevin/Hogwartsck18/tree/master/HomeWork/pytest_plugins_Hw_19',
    version='1.0',
    author="kevin",
    author_email='260317442@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # �������� ��pip ���������ķ���
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

    # ��Ҫ��װ������
    install_requires=[
        'pytest'
    ],
    # ���ģ�� ������ں���
    entry_points={
        'pytest11': [
            'pytest_encode_logger = pytest_encode_logger',
        ]
    },
    #   windows��Ҫ��
    zip_safe=False
)
