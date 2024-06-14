from setuptools import setup, find_packages

setup(
    name='srt-core',
    version='0.1.3',
    packages=find_packages(),  # This will find and include all packages
    install_requires=[
        'pyyaml',
        'logging',
    ],
    entry_points={
        'console_scripts': [
            'config-cli=config.config:main',
            'logger-cli=utils.logger:main',  # Corrected this line
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
