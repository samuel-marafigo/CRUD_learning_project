1. Introduction

   
This project is part of the Raciocínio Computacional (Computational Reasoning) course in the Systems Analysis and Development program I am taking. The main objective of the course is to instill basic programming principles and culminate in the development of a CRUD (Create, Retrieve, Update, Delete) system following the course guidelines.
Since I am Brazilian, and the course guidelines are written in Portuguese, the naming and commenting in the code, as well as the interface, will be in Brazilian Portuguese. However, other documentation, including this ReadMe and commit messages, will be in English.
The purpose of this repository is to showcase my learning process through different versions and to mature my skills in a Git environment.


2. Getting started

   
As this project focus on learning experience, I plan to keep it simple. The course guidelines expect the application to be built using Python and the data to be manipulated with JSON.
The project is being developed using Python 3.9 and in it's current state no dependencies are needed.


3. Features and documentation

   
The application features a command-line interface where the user may navigate through to add, list, update or remove data on students, professors, subjects, classes and enrollments.
To use the application, simply run the main.py script. The program will display a main menu with numbers as options, requesting input as needed. 


4. License

   
This project is licensed under the MIT License


5. Contact information

    
All kinds of feedback, comments or requests are always welcome!
You may reach me through the following:
Email: swmarafigo@gmail.com // Linkedin: https://www.linkedin.com/in/swmarafigo/


6. Changelog

    
Version 0.1.0 - Initial release with the basic menu layout. No functions implemented yet.

Version 0.1.1 - Added a try-except block around all user input sections in the main.py file. This follows the EAFP (Easier to Ask for Forgiveness than Permission) principle, ensuring that the program will not crash if a user enters anything other than an integer when selecting options in the CRUD menu.

Version 0.2.0 - "Include" and "list" functions added at the student's menu in main.py according to course schedule. Created placeholder message for functions that are still being implemented. Removed redundant menu options. Now, any option that still hasn't been implemented will display a placeholder message telling the user it is still under development.

Version 0.2.1 - Refactored the menu functions, making it modular, separating layout and logic functions. Introduced a reusable user input handling. Improved syntax in the listar() function.

Version 0.2.2 - Refactored the Create (incluir_dados, formerly incluir) and Read (listar_dados, formerly listar) functions, making them reusable in the code through the use of arguments to select a database. Made the function names more descriptive.
   
