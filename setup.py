from setuptools import setup, find_packages

setup(
    name='log2html',
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'numpy >= 1.11.1',
        'plotly >= 1.12.9',
        'click >= 6.6',
        'pytest >= 3.0.2',
    ],
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
