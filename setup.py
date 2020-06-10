from setuptools import setup
import os
from glob import glob

setup(
    name='katakana',
    version='0.2',
    description='English to Katakana with sequence-to-seqeucne learning',
    license='MIT',
    url='https://github.com/Tsedevdorj/katakana',
    author='wanasit',
    install_requires=['keras', 'h5py', 'numpy', 'tensorflow'],
    packages=['katakana'],
    data_files = [ (os.path.dirname(__file__), glob('trained_models/**')) ]
)
