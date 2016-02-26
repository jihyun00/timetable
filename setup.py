from setuptools import find_packages, setup


install_requires = [
    'flask == 0.10.1',
    'sqlalchemy == 1.0.11',
    'alembic == 0.7.4',
    'flake8 == 2.5.1',
]


tests_require = [
    'pytest >= 2.7.0',
    'pytest-sugar',
]


def readme():
    with open('README.md') as f:
        try:
            return f.read()
        except (IOError, OSError):
            return None


setup(
    name="timetable",
    version=0.1,
    packages=find_packages(),
    url='https://github.com/jihyun00/timetable',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
    },
    long_description=readme(),
)
