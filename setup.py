import os

from setuptools import setup, find_packages


REPO_DIR = os.path.dirname(os.path.realpath(__file__))


def collectRequirements():
  """
  Read the requirements.txt file and parse into requirements for setup's
  install_requirements option.
  """
  requirementsPath = os.path.join(REPO_DIR, "requirements.txt")
  return [
    line.strip()
    for line in open(requirementsPath).readlines()
    if not line.startswith("#")]


if __name__ == "__main__":

  setup(
    name="wheel_marker_fail",

    version="0.0.1",

    install_requires=collectRequirements(),

    package_dir = {"": "src"},

    packages=find_packages("src"),

    zip_safe=False,

    description="Demonstrates lack of environment marker support when installing wheel",

    author="Vitaly",
  )
