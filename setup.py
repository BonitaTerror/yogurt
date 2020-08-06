from setuptools import setup, find_packages


setup(
    name="Yogurt",
    version="0.0.1",
    packages=find_packages(),
    author="Alexander Avery",
    author_email="alex.avery@beetbox.io",
    entry_points={
        'console_scripts': [
            'yogurt=yogurt.cli:YogurtParser'
        ]
    }
)
