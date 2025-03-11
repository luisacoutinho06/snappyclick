from setuptools import setup, find_packages

setup(
    name="snappyclick",  # Name of your package
    version="1.0.0",  # Version of your project
    description="SnapPyClick App - Dynamic Resume Generator",  # Short description of the project
    long_description=open("README.md").read(),  # Detailed description from the README file
    long_description_content_type="text/markdown",  # Specifying the content type of the README
    author="Luisa",  # Author's name
    author_email="luisacoutinho06@gmail.com",  # Author's email
    url="https://github.com/luisacoutinho06/snappyclick",  # URL of the project repository (if applicable)
    packages=find_packages(where="src"),  # Automatically find packages in the 'src' folder
    package_dir={"": "src"},  # Points to the location of the source code
    install_requires=[  # Project dependencies
        "customtkinter>=5.2.2",  # Example dependency
        "pillow",  # If you are working with images
        "requests",  # If making HTTP requests
    ],
    classifiers=[  # Metadata classifiers (important for distribution)
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Supported operating systems
    ],
    python_requires=">=3.6",  # Minimum Python version required
    entry_points={  # If you want to create a command-line entry point
        "console_scripts": [
            "snappyclick=snappyclick.app:main",  # Runs the 'main' method from the 'app.py' file
        ],
    },
)
