from setuptools import setup, find_packages

setup(
    name='binprint',
    version='0.1',
    description='Simple package to pretty print binary data in python',
    author='Seong Jin Kim',
    author_email='mirusu400@naver.com',
    url='https://github.com/mirusu400/binprint',
    download_url='',
    install_requires=[],
    # packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['binary', 'Pretty print', 'Python', 'Hex dump', 'Ascii dump', 'hex', 'dump'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
