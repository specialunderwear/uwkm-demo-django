from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='uwkm-demo-django',
    # extract version from module.
    version=__version__,
    description="Demo project voor uwkm",
    long_description="Aliquam aliquet, est a ullamcorper condimentum, tellus nulla fringilla elit, a iaculis nulla turpis sed wisi. Fusce volutpat. Etiam sodales ante id nunc. Proin ornare dignissim lacus. Nunc porttitor nunc a sem. Sed sollicitudin velit eu magna. Aliquam erat volutpat. Vivamus ornare est non wisi. Proin vel quam. Vivamus egestas. Nunc tempor diam vehicula mauris. Nullam sapien eros, facilisis vel, eleifend non, auctor dapibus, pede.",
    classifiers=[],
    keywords='',
    author='lars',
    author_email='spam@permanentmarkers.nl',
    url='https://bitbucket.org/uwkm_deventer/uwkm-demo-django/',
    license='GPL',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # for avoiding conflict have one namespace for all apc related eggs.
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'Django',
        'django-oscar',
        'wagtail',
    ],
    # mark test target to require extras.
    extras_require = {
        'test':  ["mock"]
    },
    # generate scripts
    entry_points={
        'console_scripts':[
            'manage.py = uwkmdemo.main:main',
        ]
    },
)
