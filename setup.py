from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in semis_theme/__init__.py
from semis_theme import __version__ as version

setup(
	name="semis_theme",
	version=version,
	description="SEMIS Theme for Frappe",
	author="Micromerger",
	author_email="m.haroon@pk.micromerger.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
