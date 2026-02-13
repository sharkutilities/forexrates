from setuptools import setup, find_packages

setup(
    name="forexrates",
    version="0.0.1.dev0",
    description="A unified codebase for fetching Foreign Exchange Rates from different API sources",
    author="sharkutilities",
    url="https://github.com/sharkutilities/forexrates",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy==1.24.4",
        "pandas==1.5.3",
        "requests==2.32.3",
        "psycopg2==2.9.10",
        "SQLAlchemy==1.4.54",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
