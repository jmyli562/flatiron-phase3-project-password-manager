# Password Manager Lite

![Password Management Application](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/a46670b9-ccf3-4595-9878-521f90a913d1)

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Demo Video](#demo)
- [Contributing](#contributing)
- [License](#license)

## Description

The Password Management Application is a secure and user-friendly tool built using Python and SQLAlchemy that allows users to store and manage their online account information securely. My application provides features for adding, updating, and deleting account entries, categorizing entries, adding tags for better organization, and analyzing aggregated data insights.

## Features

- **User Authentication:** Register and log in securely to manage your passwords.
- **Account Entries:** Add, update, and delete account information.
- **Categories:** Organize entries into different categories for better organization.
- **Tags:** Add tags to your entries for easy searching and filtering.
- **Data Insights:** Explore aggregated information about your account entries.
- **Command-line Interface (CLI):** User-friendly CLI to interact with the application.

## Installation

### Pre-requisites
To successfully install my application please follow the instructions below. Note that there are a couple of pre-requisites that are required to be installed which are Python, pyenv, and pipenv.


1. To install pyenv, you can use the pyenv installer found here: https://github.com/pyenv/pyenv-installer

2. Once pyenv is installed, please install python version 3.8.13 using the following command:
   ```bash
   pyenv install 3.8.13

3. Finally, install pipenv using the following command:
   ```bash
   pip install pipenv

After installing everything above, please follow the instructions below to install my application.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-management-app.git
   
2. Navigate into the project directory:
   ```bash
   cd flatiron-phase3-project-password-manager

3. Install dependencies
   ```bash
   pipenv install
   
4. Enter into the virtual environment
   ```bash
   pipenv shell
5. cd into lib directory
   ```bash
   cd lib
6. Initialize alembic
   ```bash
   alembic init alembic
7. Create Initial Migration
   ```bash
   alembic revision --autogenerate -m "Initial migration"
8. Apply migration
   ```bash
   alembic upgrade head
9. Seed the database
   ```bash
   python seed.py
10. Run the application
    ```bash
    python cli.py

## Usage
### Registration and Login
Upon running the application, you'll be prompted to register or log in.
To register, provide a unique username, a strong password, and a valid email address.
To log in, enter your username and password.

![Registration Page](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/0be1a213-7d5d-4491-a6b5-cbddc356ed3b)

### Main Menu
After logging in, you'll be presented with the main menu. The main menu options include:

![Screenshot 2023-08-27 180524](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/75b04beb-e9b9-4409-8cfa-35da7324eccb)

### Manage Passwords
Picking this option will take you to a submenu where you can manage your passwords.
Options include viewing your password, updating your password, and viewing your average password length.

![Screenshot 2023-08-27 181059](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/655038c7-db63-4d7b-8d5d-9b692acc16ad)

### Manage Entries
Picking this option will take you to a submenu where you can view and manage your account entries.
Options include adding new entries, deleting an entry, and viewing all of your entries.

![Screenshot 2023-08-27 181344](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/bf0587c6-3652-4b36-b73b-877d164c4d93)

### Manage Categories
Organize your entries by creating, viewing, and deleting your categories.
Options include viewing your categories and creating new categories

![Screenshot 2023-08-27 181454](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/5196fbb7-847b-4772-a6e0-c9af6d9be504)

### Manage tags
This option will enable you to categorize your entries further using tags.
In this menu, you can add and remove tags to/from entries, as well as search and count entries by tag for better organization.

![Screenshot 2023-08-27 181933](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/99681f0b-1af4-4beb-9307-7ec7390f819a)

## Logging Out
To log out, simply choose the "Log Out" option from the main menu.
You'll be taken back to the registration/login screen.

![Screenshot 2023-08-27 182037](https://github.com/jmyli562/flatiron-phase3-project-password-manager/assets/60550632/4688e5a2-2c7c-48be-bfae-edb9c154bd42)

## Demo
[![Watch the video](https://img.youtube.com/vi/O8YjhyESclM/hqdefault.jpg)](https://www.youtube.com/embed/O8YjhyESclM)

## Contributing

Pull requests are welcome. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project Create your Feature Branch (git checkout -b feature/NewFeature) Commit your Changes (git commit -m 'Add some NewFeature') Push to the Branch (git push origin feature/NewFeature) Open a Pull Request For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2023 Jimmy Li

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
