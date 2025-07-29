#!/usr/bin/env python3
"""
Setup script for Ипотечный калькулятор
"""

from setuptools import setup, find_packages
import os

# Читаем README файл
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Читаем requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="loan_calc",
    version="1.0.0",
    author="SENSE AI",
    author_email="contact@sense-ai.com",
    description="Ипотечный калькулятор с расчетом досрочного погашения",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/loan_calc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Framework :: Flask",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "loan_calc=loan_calc.app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "loan_calc": [
            "templates/*.html",
            "static/*",
        ],
    },
    keywords="mortgage calculator loan financial calculator flask web application",
    project_urls={
        "Bug Reports": "https://github.com/your-username/loan_calc/issues",
        "Source": "https://github.com/your-username/loan_calc",
        "Documentation": "https://github.com/your-username/loan_calc#readme",
    },
) 