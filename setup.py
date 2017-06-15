from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(name="hv-uploader",
      version="2017.06.15",
      description="Uploads content to the Heavy Cloud Service (https://enzienaudio.com).",
      long_description=readme(),
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities"
      ],
      keywords="procedural audio uploader heavy enzien audio interactive games",
      url="http://github.com/enzienaudio/hv-uploader",
      author="Enzien Audio Ltd",
      author_email="info@enzienaudio.com",
      license="MIT",
      packages=["hv_uploader"],
      install_requires=[
          "requests",
      ],
      entry_points={
          "console_scripts": ["hv-uploader=hv_uploader:main"],
      },
      include_package_data=True,
      zip_safe=True)