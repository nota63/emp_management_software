# Employee Management System

![Project Logo](static/my.png)

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Installation Instructions](#installation-instructions)
4. [Usage](#usage)
5. [Screenshots](#screenshots)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact Information](#contact-information)

## Project Description
The **Employee Management System** is a comprehensive solution for managing employee data within an organization. It includes functionalities for handling employee attendance, salaries, leave applications, notices, and generating employee ID cards. The system is designed to streamline HR processes and improve overall efficiency.

## Features
- **Owner Login:** Secure login for the owner.
- **Employee Attendance:** Manage and track attendance based on employee roles.
- **Employee Salaries:** View and manage employee salary details.
- **Notice Board:** Display and manage organizational notices.
- **Leave Applications:** Submit and manage leave applications.
- **ID Card Generation:** Create and view employee ID cards.
- **HR Management:** Special HR page for managing HR-specific tasks.

## Installation Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/employee-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd employee-management-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Access the application at `http://localhost:8000`.
2. Use the following credentials for the owner login:
    - **ID:** 1111
3. Navigate through the system to manage employee data, attendance, salaries, leave applications, and more.

## Screenshots
### Home Page
![Home Page](static/homepage.png)

### Owner Dashboard
![Owner Dashboard](static/owner_dashboard.png)

### Employee Attendance
![Employee Attendance](static/check_attendance.png)

### Notice Board
![Notice Board](static/notice_board.png)

### Leave Applications
![Leave Applications](static/leave_applications.png)

### ID Card Generation
![ID Card Generation](static/emp_id.png)

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite (default)
- **Libraries:** Pillow (for image processing), Django Messages Framework
- pyttsx3 for voice notifications

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact Information
For any queries or feedback, please contact:
- **Name:** Harshad dudhabarve
- **Email:** vishaldudhabarve105@gmail.com
- **GitHub:** [nota63](https://github.com/nota63)
