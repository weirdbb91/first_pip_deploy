from setuptools import setup, find_packages

setup(
    name = "weirdbb91",
    version = "0.0.3",
    description = "it's my first pip deploy, say hi and bye",
    author = "seungho.baek",
    author_email = "weirdbb91@gmail.com",
    url = "https://github.com/weirdbb91/first_pip_deploy",
    download_url = "https://github.com/weirdbb91/first_pip_deploy/archive/master.zip",
    install_requires =  [],
    packages = find_packages(exclude = []),
    keywords = ["pypi deploy"],
    python_requires = ">=3",
    package_data = {},
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python :: 3.9",
    ],
)
