from setuptools import setup, find_packages

setup(
    name='srt-core',
    version='0.1.7',
    packages=find_packages(include=['srt_core', 'srt_core.*']),  # Ensure it includes the srt_core package
    install_requires=[
        'pyyaml',
        'logging',
    ],
    entry_points={
        'console_scripts': [
            'config-cli=srt_core.config.config:main',
            'logger-cli=srt_core.utils.logger:main',
        ],
    },
    author='Suparious',
    author_email='suparious@solidrust.net',
    description='SolidRusT Core Libraries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SolidRusT/srt-core',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
