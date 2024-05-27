# setup.py
from setuptools import setup, find_packages

setup(
    name='audio_searcher',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'SpeechRecognition',
        'pydub'
    ],
    entry_points={
        'console_scripts': [
            'audio-searcher=audio_searcher.audio_searcher:main',
        ],
    },
    author='yutamagara',
    author_email='s2222033@stu.musashino-u.ac.jp',
    description='A tool to search for keywords in audio files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yutamagara/mypackage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
