import setuptools

setuptools.setup(name='ext_api',
version='1.0',
description='External API Call',
url='https://github.com/salwil/testing-third-party-apis-with-mocks',
author='Salome Wildermuth',
python_requires='>=3.9',
install_requires=[
    'nose==1.3.7',
    'urllib3==2.1.0'
],
author_email='salome.wildermuth@ewz.ch',
packages=setuptools.find_packages())