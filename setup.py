from setuptools import find_packages, setup

setup(
    name='django-formsettesthelpers',
    version='0.1',
    description="Django test helpers for generating formset data.",
    long_description="",
    classifiers=[],
    keywords=['django', 'formset', 'test', 'helpers'],
    author='Teemu Husso',
    author_email='teemu.husso@gmail.com',
    url='https://github.com/Raekkeri/django-formsettesthelpers',
    download_url = 'https://github.com/raekkeri/django-formsettesthelpers/tarball/0.1',
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
