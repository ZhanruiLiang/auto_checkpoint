import setuptools

setuptools.setup(
    name="auto_checkpoint",
    version="1.0",
    author="Zhanrui Liang",
    author_email="ray040123@gmail.com",
    description="automatically makes checkpoints using git to reduce the risk of losing progress of your work",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZhanruiLiang/auto_checkpoint",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=["gitpython"],
)