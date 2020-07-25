from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gaussian-binomial',
      version='1.0',
      author='Esraa Abduallah',
      author_email='esraahisham753@gmail.com',
      description='Gaussian&Binomial distributions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/esraahisham753/Gaussian_Binomial_package',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.0',
      packages=['distributions'],
      zip_safe=False)
