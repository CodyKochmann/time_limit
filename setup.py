from distutils.core import setup

setup(
  name = 'time_limit',
  packages = ['time_limit'], # this must be the same as the name above
  version = '2017.6.15',
  install_requires=[],
  description = 'decorator that limits the runtime of a function',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/time_limit',
  download_url = 'https://github.com/CodyKochmann/time_limit/tarball/2017.6.15',
  keywords = ['time_limit', 'time', 'timeout', 'default_output', 'production'],
  classifiers = [],
)
