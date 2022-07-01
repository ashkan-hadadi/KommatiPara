from distutils.core import setup

setup(
    # Application name:
    name="KommatiPara",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Ashkan Hadadi",
    author_email="hadadi.ashkan@gmail.com",

    # Packages
    packages=["backend"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/KommatiPara_v010/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "fastapi",
        "starlette-exporter",
        "uvicorn[standard]",
        "pandas",
    ],
)