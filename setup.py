import codecs
from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="shadowsocksr",
    version="1.0.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A fast tunnel proxy that help you get through firewalls",
    author='graz',
    author_email='graz@gmail.com',
    url='https://github.com/hcaijin/shadowsocksr',
    packages=['shadowsocksr', 'shadowsocksr.crypto', 'shadowsocksr.obfsplugin'],
    package_data={
        'shadowsocksr': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocksr.local:main
    ssserver = shadowsocksr.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
