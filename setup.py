from setuptools import setup, find_packages
from external_urls import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    pass

setup(
    name='django-external-urls',
    version=__version__,
    description="Track external links with a signal on click.",
    long_description=long_description,
    keywords='django, external url, redirect',
    author='Rich Atkinson, Piran Digital',
    author_email='rich@piran.com.au',
    url='https://github.com/piran/django-external-urls',
    download_url='https://github.com/piran/django-external-urls/archive/0.1.zip',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', ],
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
