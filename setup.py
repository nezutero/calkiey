from setuptools import setup, find_packages

setup(
    name='calkiey',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
       'tk',
       'pillow',
       'numpy',
    ],
    entry_points={
        'console_scripts': [
            'calkiey=calkiey.calkiey:main',
        ],
    },
    description='GUI calculator using Tkinter called Calkiey',
    long_description='''\
    GUI calculator using Tkinter. It is a simple calculator with basic operations made as a project that i just have to do, not because i wanted to do it but because i had to do it, so i did it, and now it is here. And please, don't judge me, and don't laugh at me, coz i will cry. Really, i will cry.
    It provides basic arithmetic operations and additional functionalities such as
    calculating factorials, square roots, percentages, and logarithms.
    ''',
    long_description_content_type='text/plain',
)
