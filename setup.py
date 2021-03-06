from setuptools import setup

setup(
    name='pinocchio',
    version="0.2",
    download_url = 'https://github.com/unpluggd/pinocchio/tarball/0.2',

    description = 'pinocchio plugins for the nose testing framework, hosted by unpluggd on github',
    author = 'C. Titus Brown and Michal Kwiatkowski',
    author_email = 'titus@idyll.org,constant.beta@gmail.com',
    license = 'MIT',

    url = 'https://github.com/unpluggd/pinocchio/',

    long_description = """\
Extra plugins for the nose testing framework.  Provides tools for flexibly
assigning decorator tags to tests, choosing tests based on their
runtime, doing moderately sophisticated code coverage analysis
of your unit tests, and making your test descriptions look like
specifications.

This version has been fixed to work with Python 2.7
""",

    packages = ['pinocchio'],
    entry_points = {
        'nose.plugins': [
            'figleaf-sections = pinocchio.figleaf_sections:FigleafSections',
            ],
        'nose.plugins.0.10': [
            'decorator = pinocchio.decorator:Decorator',
            'output-save = pinocchio.output_save:OutputSave',
            'spec = pinocchio.spec:Spec',
            'stopwatch = pinocchio.stopwatch:Stopwatch',
        ]},
)
