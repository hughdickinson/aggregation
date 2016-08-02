from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext

from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

# From http://stackoverflow.com/a/21621689 because numpy is total garbage
class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

setup(
        name='aggregation',
        version='0.2.0',
        author='Greg Hines',
        author_email='greg@zooniverse.org',
        url='http://github.com/zooniverse/reduction',
        license='LICENSE',
        cmdclass={'build_ext':build_ext},
        setup_requires=['numpy==1.8.1'],
        packages=["engine"],
        description='Aggregation for Zooniverse projects',
        long_description=open('README.md').read(),
        test_suite='nose.collector',
        tests_require=['nose'],
        install_requires=reqs
        )
