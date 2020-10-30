import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video-razor",
    version="0.0.1",
    author="David Alford",
    author_email="firstlast678@gmail.com",
    description="A package for slicing a video into N sections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/5starkarma/video-razor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
