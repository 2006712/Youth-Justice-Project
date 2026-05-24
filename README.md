# Youth Justice Project

## Project Overview

The **Youth Justice Project** is a Django-based web application designed to support youth justice case management and intervention planning. The system allows authorised users to manage youth records, offence information, support programs, and recommendation workflows.

The application helps case workers identify suitable support programs for youth based on offence severity, school status, family support level, and background information. It also includes authentication, role-based access control, a service layer, and structured exception handling as part of the Assessment 4 requirements.

---

## Purpose of the System

The purpose of this system is to provide a structured way to:

- Record youth profile information
- Record offence details linked to each youth
- Maintain support programs such as mentoring, counselling, education, rehabilitation, and community programs
- Generate support recommendations based on youth risk and background factors
- Control access using user roles and permissions
- Improve maintainability through service-layer architecture and exception handling

---

## Main Features

### 1. User Authentication

The system supports user login, logout, and registration using Django’s built-in authentication system.

Authenticated users are redirected to a dashboard where available functions are shown based on their role.

---

### 2. Role-Based Access Control

The system uses Django groups and permissions to control access.

| Role | Youth Records | Support Recommendations | Admin Panel |
|---|---|---|---|
| Admin / Superuser | Yes | Yes | Yes |
| Case Worker | Yes | Yes | No |
| Volunteer | Yes | No | No |

### User Groups

The following groups are used:

- **Admin**
- **Case Worker**
- **Volunteer**

### Permission Design

- Admin users have full access to system data and user management.
- Case Workers can view and update youth-related records and access recommendations.
- Volunteers have limited read-only access to youth records and support program information.

---

## Application Workflow

The main workflow of the system is:

1. Admin creates support programs.
2. Admin or Case Worker creates youth records.
3. Admin or Case Worker records offences for each youth.
4. The system checks offence severity, school status, and family support level.
5. The system recommends suitable support programs.
6. Case Workers review the recommendations and use them to support intervention planning.

---

## Support Program Recommendation Logic

Support programs are recommended based on youth-related information.

Example recommendation rules:

- Serious offences may lead to counselling or rehabilitation support.
- Youth who have dropped out of school may need education reintegration support.
- Youth with low family support may benefit from mentoring or counselling.
- Low-risk youth may be recommended community-based programs.

Example support programs include:

- Community Awareness Program
- Youth Mentoring Program
- Education Reintegration Program
- Counselling Support Program
- Rehabilitation Program

---

## Project Architecture

The system follows Django’s Model-Template-View architecture with an added service layer.

```text
models.py      → Defines database models and domain data
views.py       → Handles HTTP requests, permissions, and template rendering
services.py    → Handles business logic and recommendation workflows
exceptions.py  → Defines custom application exceptions
templates/     → Contains HTML templates
tests.py       → Contains automated tests
