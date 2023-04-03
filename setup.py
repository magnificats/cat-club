from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cat_club/__init__.py
from cat_club import __version__ as version

setup(
	name="cat_club",
	version=version,
	description="cat show and ranking software",
	author="Magnificats",
	author_email="magnificats.ro@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
