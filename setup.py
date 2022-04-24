from setuptools import setup
import re


with open('README.md') as fp:
    long_description = fp.read()


def find_version():
    with open('atf/__init__.py') as fp:
        for line in fp:
            # __version__ = '0.1.0'
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    assert False, 'cannot find version'


setup(
    name='atf',
    version=find_version(),
    packages=['atf'],
    description='Algorithmic Trading Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    maintainer='streetyoga.capital',
    maintainer_email='miron@street.yoga',
    url='https://github.com/streetyoga/atf',
)
