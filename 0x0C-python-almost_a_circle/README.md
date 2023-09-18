Almost a Circle - Python Project
Python Version
PEP8
License

Table of Contents
Project Description
Installation
Usage
File Structure
Testing
Contributing
License
Project Description
The "Almost a Circle" project is part of the Higher Level Curriculum for Python programming. This project aims to provide a comprehensive understanding of various Python concepts and features, including object-oriented programming (OOP), file handling, unit testing, and more.

Learning Objectives

Upon completing this project, you will be able to:
Implement unit testing in a Python project.
Serialize and deserialize Python objects using JSON.
Work with command-line arguments using argparse.
Create classes with private attributes and use getters and setters.
Understand and apply inheritance and polymorphism.
Handle exceptions effectively.
Read and write data to/from files.
Create and manipulate Python dictionaries.
Maintain code style and readability following PEP 8 guidelines.

Requirements

Python 3.8 or higher.
Code should adhere to PEP 8 style guidelines.
All code should be well-documented with clear explanations.

Installation

Clone the repository to your local machine:

git clone https://github.com/teargas001/almost_a_circle.git


Navigate to the project directory:

cd almost_a_circle
Ensure you have Python 3.8 or higher installed. You can check your Python version with:

python3 --version

No external dependencies are required. This project uses only standard Python libraries.

Usage

Running Unit Tests
To run the unit tests, use the following command from the project's root directory:

python3 -m unittest discover tests

Example Usage
You can also interact with the classes by creating Python scripts. Here's an example of how to create a Rectangle object and calculate its area:

from models.rectangle import Rectangle

# Create a Rectangle with width 5 and height 10
r = Rectangle(5, 10)

# Calculate and print the area
print("Area:", r.area())
Command Line Interface (CLI)
To interact with the project via the command line, use the provided Python scripts in the project's root directory.

0-main.py: Example script for creating and working with Base objects.
1-main.py: Example script for creating and working with Rectangle objects.
2-main.py: Example script for validating attributes of Rectangle objects.
Run these scripts using Python, e.g., python3 0-main.py.

File Structure

The project has the following file structure:

almost_a_circle/
│
├── models/
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
│
├── tests/
│   ├── test_models/
│   │   ├── test_base.py
│   │   ├── test_rectangle.py
│   │   └── test_square.py
│   └── ...
│
├── 0-main.py
├── 1-main.py
├── 2-main.py
├── ...
│
├── README.md
└── ...

Testing

This project includes a comprehensive set of unit tests to ensure the functionality and correctness of the implemented classes and methods. You can run the tests using the following command:

python3 -m unittest discover tests

We encourage collaboration on test cases to ensure comprehensive coverage and accuracy.

Contributing

Contributions to this project are welcome. If you find a bug or have an improvement in mind, please open an issue or create a pull request with your proposed changes. For major changes, please discuss them in the issue first.

License

This project is open-source and available under the MIT License. You are free to use, modify, and distribute this software as per the terms of the license.

Thank you for using Almost a Circle! If you have any questions or need further assistance, please feel free
