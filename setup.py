import setuptools

setuptools.setup(
    name="icssplit",
    version="0.9.3",
    url="https://github.com/beorn/icssplit",
    download_url = 'https://github.com/beorn/icssplit/archive/0.9.3.tar.gz',

    author="Bjorn Stabell",
    author_email="bjorn@stabell.org",

    description="Split big .ics/.ical files iinto smaller ones for easy import into Google Calendar",
    long_description=open('README.rst').read(),
    license="MIT",

    #packages=setuptools.find_packages(),
    #packages=['icssplit'],
    py_modules=['icssplit',],

    python_requires='~=3.0',
    install_requires=['docopt',],

    #scripts=['icssplit.py'],
    entry_points={ 'console_scripts': ['icssplit=icssplit:cli',] },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ics calendar ical vcal',
)
