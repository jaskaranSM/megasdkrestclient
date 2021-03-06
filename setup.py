import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="megasdkrestclient",
    version="0.1.1",
    description="MegaSDK-REST python wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaskaranSM/megasdkrestclient",
    download_url="https://github.com/jaskaranSM/megasdkrestclient/releases",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "aiohttp"],
    python_requires=">=3.6",
)