from setuptools import setup, find_packages

setup(
    name = "weirdbb91",
    version = "0.0.2",
    description = "it's my first pip deploy, say hi and bye",
    author = "seungho.baek",
    author_email = "weirdbb91@gmail.com",
    url = "https://github.com/weirdbb91/pypi_deploy_test",
    download_url = "https://github.com/weirdbb91/pypi_deploy_test/archive/master.zip",
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
