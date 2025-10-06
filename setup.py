#!/usr/bin/env python

from setuptools import setup, find_packages
import os

# Read version from version.py
version_file = os.path.join(os.path.dirname(__file__), 'version.py')
with open(version_file, 'r') as f:
    exec(f.read())

# Read README for long description
readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_file, 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tridesclous-edited',
    version=version,  # From version.py
    author='C. Pouzat, S.Garcia (Original), josemal98 (Neural Analysis Modifications)',
    author_email='',
    description='Enhanced tridesclous for Real-Time Neural Analysis Interface - offline/online spike sorting with improved PyACQ integration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/josemal98/tridesclous-edited',
    project_urls={
        'Original Repository': 'https://github.com/tridesclous/tridesclous',
        'Bug Reports': 'https://github.com/josemal98/tridesclous-edited/issues',
        'Source': 'https://github.com/josemal98/tridesclous-edited',
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md', '*.rst', '*.yml', '*.yaml'],
        'gui': ['icons/*.py', 'icons/*.png', 'icons/*.svg'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.18.0',
        'scipy>=1.5.0', 
        'matplotlib>=3.1.0',
        'pandas>=1.0.0',
        'scikit-learn>=0.23.0',
        'joblib>=1.0.0',
        'numba>=0.50.0',
        'tqdm>=4.50.0',
        'neo>=0.10.0',
        'pyqtgraph>=0.12.0',
        'hdbscan>=0.8.0',
        'seaborn>=0.11.0',
        'openpyxl>=3.0.0',
        'loky>=3.0.0',
    ],
    extras_require={
        'gui': ['PyQt5>=5.12.0', 'pyqtgraph>=0.12.0'],
        'opencl': ['pyopencl>=2020.1'],
        'full': ['PyQt5>=5.12.0', 'pyqtgraph>=0.12.0', 'pyopencl>=2020.1'],
    },
    entry_points={
        'console_scripts': [
            'tdc=scripts.tdc:main',
        ],
    },
    keywords=['spike sorting', 'electrophysiology', 'neuroscience', 'real-time', 'neural analysis'],
    license='MIT',
    zip_safe=False,
)