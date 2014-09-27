from setuptools import find_packages, setup


version = '0.1'

setup(
    name='formsettesthelpers',
    version=version,
    description="Django test helpers for generating formset data.",
    long_description="",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=[],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
         # -*- Extra requirements: -*-
    ]
)
