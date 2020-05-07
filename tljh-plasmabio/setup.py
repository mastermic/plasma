from setuptools import setup, find_packages

setup(
    name="tljh-plasma",
    version="0.0.1",
    entry_points={"tljh": ["tljh_plasma = tljh_plasma"]},
    packages=find_packages(),
    include_package_data=True,
    install_requires=["dockerspawner", "tljh_repo2docker"],
)
