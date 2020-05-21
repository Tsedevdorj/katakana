from setuptools import setup
import os
from glob import glob

setup(
    name='katakana',
    version='0.1',
    description='English to Katakana with sequence-to-seqeucne learning',
    license='MIT',
    url='http://github.com/wanasit/katakana',
    author='wanasit',
    packages=['katakana'],
    install_requires=['keras', 'h5py', 'numpy'],
    data_files = [ (os.path.dirname(__file__), glob('trained_models/**')) ]
)
