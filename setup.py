from setuptools import setup

VERSION = '1.1'

setup(
    name='crypto',
    version=VERSION,

    description='A CLI to interract with EM7.',
    url='https://github.jpl.nasa.gov/cgauge/em7-cli',

    author='Christophe Gauge',
    author_email='christophe.gauge@jpl.caltech.edu',

    packages=['crypto'],

    install_requires=['pycryptodome'],

    entry_points={
        'console_scripts': [
            'crypto = crypto.__main__:main'
        ]
    },

)
