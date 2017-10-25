import setuptools

setuptools.setup(
    name="icssplit",
    version="1.0.0",
    url="https://github.com/beorn/icssplit",

    author="Bjorn Stabell",
    author_email="bjorn@stabell.org",

    description="Split big .ics/.ical files iinto smaller ones for easy import into Google Calendar",
    long_description=open('README.rst').read(),
    license="MIT",

    #packages=setuptools.find_packages(),
    packages=['icssplit'],

    #install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
