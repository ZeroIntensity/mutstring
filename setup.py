from setuptools import setup

with open("./README.md") as f:
    long_desc: str = f.read()

if __name__ == "__main__":
    setup(
        name="mutstring",
        version="1.0.0",
        author="ZeroIntensity",
        author_email="<zintensitydev@gmail.com>",
        description="please never use this",
        long_description_content_type="text/markdown",
        long_description=long_desc,
        py_modules=["mutstring"],
        install_requires=["pointers.py"],
        keywords=["python", "strings", "mutability"],
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
        license="MIT",
        urls={"Repo": "https://github.com/ZeroIntensity/mutstring"},
    )
