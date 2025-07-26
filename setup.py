from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
      name="mlops-02",
      version="0.2.0",
      author="Prince Kumar",
      packages=find_packages(),
      install_requires=requirements,
)