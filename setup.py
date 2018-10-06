import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='scoped_name_resolver',
    version='0.0.1',
    author='Davide Laezza',
    author_email='dlae@gmx.com',
    description='Name resolver with scoping',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davla/scoped-name-resolver',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
)
