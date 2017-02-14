from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()

setup(name="hv_uploader",
      version="1.0",
      description="Uploads content to the Heavy Cloud Service (https://enzienaudio.com).",
      long_description=readme(),
      classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 2.7",
      ],
      keywords="procedural audio uploader heavy enzien audio interactive games",
      url="http://github.com/enzienaudio/hv_uploader",
      author="Enzien Audio Ltd",
      author_email="info@enzienaudio.com",
      license="MIT",
      packages=["hv_uploader"],
      install_requires=[
          "markdown",
      ],
      # test_suite="nose.collector",
      # tests_require=["nose", "nose-cover3"],
      entry_points={
          "console_scripts": ["hv-uploader=hv-uploader.command_line:main"],
      },
      include_package_data=True,
      zip_safe=True)