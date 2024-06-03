from setuptools import setup, find_packages

setup(
    name='my_config_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'llama_cpp_agent',
        'llama_cpp',
        'logging',
        # Add other dependencies if needed
    ],
    entry_points={
        'console_scripts': [
            'config-cli=config.config:main',  # If you have a CLI entry point
        ],
    },
    author='Your Name',
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
    python_requires='>=3.11',
)
