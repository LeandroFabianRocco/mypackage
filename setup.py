from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',    
    description='Personal functions and methods',
    url='https://github.com/leandroGHsoft/mypackage',
    author='Leandro F. Rocco',
    author_email='leandro.f.rocco@gmail.com',
    license='Free',
    packages=find_packages(),
    install_requires=['matplotlib',
                      'numpy',                     
                      'scipy'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Only me for now',
        'License :: Free :: Free',  
        'Operating System :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
)