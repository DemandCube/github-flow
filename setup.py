from setuptools import setup, find_packages

setup(
    name='github-flow',
    author='Steve Morin',
    author_email='steve@stevemorin.com',
    version='0.1',
    packages=find_packages(),
    url='http://github.com/Demandcube/github-flow',
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ghf=yourpackage.cli:cli
    ''',
    py_modules=['click'],
    description='A simple wrapper around github apis for '
                'ease of use of github using the commandline.',
    classifiers=[
        'License :: OSI Approved :: AGPL',
        'Programming Language :: Python',
    ],
)



