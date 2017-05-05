from setuptools import setup, find_packages

setup(
	name = "COSgen",
	version = "",
	author = "Aymanns Florian",
	author_email = "faymanns@student.ethz.ch",
	description = "Contrast optimized stimulus sequence generation for fMRI.",
	keywords = ["fMRI", "stimulus", "contrast", "optimization"],
	url = "https://github.com/IBT-FMI/COSgen.git",
	install_requires = [],
	provides = ["COSgen"],
	packages = ["COSgen"],
	include_package_data = True,
	entry_points = {
		'console_scripts' : ['COSgen = COSgen.cli:main']
	}
	)
