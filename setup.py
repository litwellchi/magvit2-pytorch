from setuptools import setup, find_packages

setup(
  name = 'magvit2-pytorch',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'MagViT2 - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/magvit2-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformer',
    'attention mechanisms',
    'generative video model'
  ],
  install_requires=[
    'beartype',
    'einops>=0.7.0',
    'vector-quantize-pytorch>=1.9.7',
    'torch'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)