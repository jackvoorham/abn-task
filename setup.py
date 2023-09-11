from setuptools import setup, find_packages

setup(
    name="abn_task",
    version="0.1.0",
    description="ABN AMRO data processing task",
    packages=find_packages(),
    install_requires=[
        "blinker==1.6.2",
        "click==8.1.7",
        "Flask==2.3.3",
        "iniconfig==2.0.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "numpy==1.25.2",
        "packaging==23.1",
        "pandas==2.1.0",
        "pluggy==1.3.0",
        "py4j==0.10.9.7",
        "pytest==7.4.2",
        "python-dateutil==2.8.2",
        "pytz==2023.3.post1",
        "six==1.16.0",
        "tzdata==2023.3",
        "Werkzeug==2.3.7",
    ],
    entry_points={
        "console_scripts": [
            "abn_task=src.main:main",
        ],
    },
)
