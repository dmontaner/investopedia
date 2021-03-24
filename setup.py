import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(here, 'src', 'investopedia', '__init__.py'), encoding='utf-8') as f:
    init_lines = f.readlines()
    init_version = [x for x in init_lines if x.startswith('__version__')][0]
    init_version = init_version.split('=')[1].replace('"', '').replace("'", "").strip()

setup(
    name='investopedia',
    description='investopedia',
    author='David Montaner',
    author_email='david.montaner@gmail.com',
    url='https://github.com/dmontaner/investopedia',
    license='MIT',
    version=init_version,
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=['investopedia'],
    package_dir={'': 'src'},

    project_urls={
        'Source Code'  : 'https://github.com/dmontaner/investopedia',
        'Documentation': 'https://github.com/dmontaner/investopedia',
        'Issue Tracker': 'https://github.com/dmontaner/investopedia/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Database :: Database Engines/Servers'
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
    ],
    keywords=[
        'investopedia',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'beautifulsoup4',
        'markdown',
        'markdown-urlize',
    ],
    entry_points={
        'console_scripts': [
            'investopedia=investopedia.__main__:main',
        ],
    },
)
