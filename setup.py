#from setuptools import setup
#
#setup(name='distributions',
#      version='0.1',
#      description='Gaussian distributions',
#      packages=['distributions'],
#      zip_safe=False)

from distutils.core import setup

setup(
    name = 'binogauss_distributions',
    packages = ['binogauss_distributions'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description = 'Binomail and Gaussian distribution',
    author = 'Gbolade Kayode',
    author_email = 'gboladekayode@gmail.com',
    url = 'github package source url',
    download_url = 'download link you saved',
    keywords = ['gaussian', 'binomial','distribution'],
    classifiers = [],
    zip_safe=False
)
