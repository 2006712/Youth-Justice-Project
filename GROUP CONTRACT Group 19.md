# Group CONTRACT – Group 19

## Project Title

Youth Justice Support Recommendation System

---

# Group Members and Responsibilities

| Member   | Responsibility Area                  | Main Contributions                                                                                                                         |
| -------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Anjana Weththasinghe Mudiyanselage | Authentication and Role-Based Access | Implemented login/logout functionality, dashboard, Django groups, permissions, role-based access control, and account management features. |
| Shereena Fernando | Service Layer and Business Logic     | Implemented the service layer architecture, moved recommendation logic into services.py, and improved separation of concerns.              |
| Nathan Fernando | Exception Handling and Testing       | Added exception handling, created automated tests for models/services/permissions, and verified application behaviour.                     |
| Raizul Mukim | Documentation, UI, and Integration   | Improved UI templates, updated project documentation, maintained GitHub repository, and integrated all project components.                 |

---

# Project Overview

The Youth Justice Support Recommendation System is a Django-based web application developed to assist youth justice organizations in managing youth records, offence information, and rehabilitation support recommendations.

The system allows authorized users to:

* Manage youth profiles and offence records
* Recommend suitable intervention programs
* Control access using role-based permissions
* Maintain structured rehabilitation workflows
* Improve decision-making consistency for youth support planning

The application uses a service-layer architecture to separate business logic from presentation logic and includes automated testing to improve reliability and maintainability.

---

# Technologies Used

| Technology                   | Purpose                               |
| ---------------------------- | ------------------------------------- |
| Python                       | Backend programming language          |
| Django                       | Web application framework             |
| SQLite                       | Database management                   |
| HTML/CSS                     | Frontend templates and styling        |
| Git & GitHub                 | Version control and collaboration     |
| Django Authentication System | User authentication and authorization |

---

# Features Implemented

## Phase 1 – Core Application Development

* Created Django project structure
* Developed Youth and Offence models
* Implemented support recommendation functionality
* Created admin management pages
* Added database relationships between youth and offences

## Phase 2 – Authentication and Role-Based Access

* Created Accounts app
* Added login and logout functionality
* Created dashboard page
* Implemented role-based access control
* Configured user groups:

  * Admin
  * Case Worker
  * Volunteer
* Restricted access to pages based on permissions

## Phase 3 – Advanced Permissions and UI Enhancements

* Added custom decorators for role validation
* Improved page navigation and dashboard experience
* Added responsive layouts and professional styling
* Restricted recommendation access to authorized users only

## Phase 4 – Service Layer Architecture

* Created services.py
* Moved business logic out of views.py
* Added:

  * get_all_youth_records()
  * generate_support_recommendations()
* Improved maintainability and modularity

## Phase 5 – Exception Handling and Testing

* Created custom exception handling
* Added recommendation error handling
* Implemented automated testing for:

  * Models
  * Services
  * Permissions
  * Authentication
* Verified successful execution of all tests

---

# User Roles and Access Levels

| Role        | Access Level                                        |
| ----------- | --------------------------------------------------- |
| Admin       | Full system access including Django admin panel     |
| Case Worker | Access to youth records and support recommendations |
| Volunteer   | Read-only access to youth records                   |

---

# GitHub Repository

Repository URL:

[https://github.com/2006712/Youth-Justice-Project](https://github.com/2006712/Youth-Justice-Project)

---

# Team Collaboration Agreement

All group members agree to:

* Contribute fairly to the project
* Maintain regular communication
* Use GitHub for version control
* Follow coding standards and documentation practices
* Test features before pushing updates
* Respect deadlines and assigned responsibilities

---

# Testing Summary

The application was tested using Django’s testing framework.

Test coverage includes:

* Model validation
* Role-based access permissions
* Authentication workflows
* Service-layer recommendation generation
* Youth and offence record management

Final testing result:

* 10 tests executed successfully
* No failed tests
* No system check issues identified

---

# Future Improvements

Potential future enhancements include:

* REST API integration
* Advanced analytics dashboard
* Machine-learning-based recommendations
* Email notification support
* Cloud database deployment
* Mobile-responsive optimization

---

# Conclusion

The Youth Justice Support Recommendation System successfully demonstrates the implementation of a secure, role-based Django application using layered architecture principles.

The project provides structured youth management, offence tracking, and automated support recommendations while ensuring secure access control and maintainable software design.

The final system is fully functional, tested, and version-controlled through GitHub collaboration.
