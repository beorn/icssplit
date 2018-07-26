import setuptools

setuptools.setup(
    name="icssplit",
    version="1.0.2",
    url="https://github.com/beorn/icssplit",
    download_url = 'https://github.com/beorn/icssplit/archive/1.0.0.tar.gz',

    author="Bjorn Stabell",
    author_email="bjorn@stabell.org",

    description="Split big .ics/.ical files into smaller ones for easy import into Google Calendar",
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
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Topic :: Office/Business :: Scheduling',
    ],
    keywords='ics calendar ical vcal google gcal',
)
