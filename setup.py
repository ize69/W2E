from setuptools import setup

setup(
    name='where 2 eat',
    version='0.1.0',    
    description='A tool to see what dinning locations on rit\'s campus',
    url='https://github.com/ize69/W2E',
    author='Isaac Worsencroft',
    license='GNU v3.0',
    packages=['src'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      'BeautifulSoup'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: RIT Students, faculty, and visitors',       
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)