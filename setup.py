from setuptools import setup

VERSION = '1.0'

setup(
    name='crypto',
    version=VERSION,

    description='A CLI to interract with EM7.',
    url='https://github.com/Videre-Research-LLC/python-crypto',

    author='Christophe Gauge',
    author_email='chris@videreresearch.com',

    packages=['crypto'],

    install_requires=['pycryptodome'],

    entry_points={
        'console_scripts': [
            'crypto = crypto.__main__:main'
        ]
    },

)
