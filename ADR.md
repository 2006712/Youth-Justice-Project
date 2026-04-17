Architecture Decision Record (ADR)

Project: Youth Diversion & Support Matching System

ADR 1: Separate Models for Core Entities
Status: Accepted  

Context  
The system must manage youth, offences, and support programs as distinct data types.

Alternatives  
- Single model → simpler implementation but leads to poor scalability and data redundancy  
- Separate models → better structure and maintainability (chosen)

Decision  
Created Youth, Offence, and SupportProgram models.

Code Reference  
justice_app/models.py: 5–80  

Consequences  
- Better structure and maintainability  
- Supports object-oriented design  
- Aligns with Django model-driven architecture  

ADR 2: One-to-Many (Youth → Offence)
Status: Accepted  

Context  
A youth can have multiple offences over time.

Alternatives  
- Store offences in Youth → no proper history tracking  
- Separate model with ForeignKey → supports multiple records (chosen)

Decision  
Used ForeignKey from Offence to Youth.

Code Reference  
justice_app/models.py: 82–110  

Consequences  
- Supports offence history  
- Enables retrieval of latest offence  
- Slightly more complex queries  

ADR 3: Many-to-Many (Youth ↔ SupportProgram)
Status: Accepted  

Context  
Youth can participate in multiple support programs.

Alternatives  
- ForeignKey → restricts to one program per youth  
- ManyToMany → flexible and scalable (chosen)

Decision  
Used ManyToManyField in Youth.

Code Reference  
justice_app/models.py: 25–35  

Consequences  
- Flexible program assignment  
- Scalable relationship design  
- Adds relational complexity  

ADR 4: Add Filtering Fields in SupportProgram
Status: Accepted  

Context  
Programs must match youth characteristics such as age and risk level.

Alternatives  
- Basic model → no meaningful filtering  
- Add filtering fields → supports dynamic matching (chosen)

Decision  
Added minage, maxage, and risk_level.

Code Reference  
justice_app/models.py: 40–70  

Consequences  
- Enables personalised recommendations  
- Improves system intelligence  
- Requires accurate data input  

ADR 5: Use QuerySets for Recommendations
Status: Accepted  

Context  
Recommendations must be dynamic and scalable.

Alternatives  
- Hardcoded logic → not maintainable  
- QuerySets → flexible and scalable (chosen)

Decision  
Used Django QuerySets to filter support programs.

Code Reference  
justice_app/views.py: 10–50  

Consequences  
- Efficient and scalable logic  
- Aligns with Django ORM practices  
- Depends on clean database data  

ADR 6: Use Latest Offence
Status: Accepted  

Context  
Youth may have multiple offences recorded.

Alternatives  
- First offence → not reliable  
- Latest offence → reflects current behaviour (chosen)

Decision  
Used latest offence as the main factor in recommendation logic.

Code Reference  
justice_app/views.py: 20–40  

Consequences  
- Simple and clear logic  
- Easy to explain  
- Does not consider full offence history  

ADR 7: Show Recommendation Explanation
Status: Accepted  

Context  
Users need to understand why recommendations are made.

Alternatives  
- Show programs only → lacks transparency  
- Show explanation → improves clarity (chosen)

Decision  
Displayed a “why recommended” section in UI.

Code Reference  
justice_app/views.py: 45–65  
justice_app/templates/recommendations.html: 15–40  

Consequences  
- Improves transparency  
- Strengthens system justification  
- Slight increase in UI complexity  

ADR 8: Separate Logic and UI
Status: Accepted  

Context  
Business logic should not be placed in templates.

Alternatives  
- Logic in templates → hard to maintain  
- Logic in views/models → clean structure (chosen)

Decision  
Used Django MVC structure.

Code Reference  
justice_app/views.py: 1–70  
justice_app/templates/: all files  

Consequences  
- Clean separation of concerns  
- Easier debugging and maintenance  

ADR 9: Follow Django Design Principles
Status: Accepted  

Context  
The system must follow proper architectural practices.

Decision  
Applied Django design principles:
- DRY (Don’t Repeat Yourself)  
- Fat Models, Thin Views  
- Separation of concerns  

Code Reference  
justice_app/models.py: 1–120  
justice_app/views.py: 1–70  

Consequences  
- Cleaner and maintainable code  
- Strong alignment with Django best practices  
- Requires careful design decisions

  
ADR 8: ManyToMany supportprogram Youth relationship.
<<<<<<< HEAD
=======

Status: Accepted

Context

Various programs may be offered and taken up by a youth, as well as the same program may be offered to several youths.

Alternatives Considered

1. One-to-many relationship

   Too restrictive

2. Many-to-many

   Flexible
   Realistic

Decision

Used ManyToManyField in Youth model.

Consequences

Supports flexible assignments
Improves data relationships
Reflects real-world scenarios

ADR 9: Use Recommendation Logic by Severity.

Status: Accepted

Context

The system ought to be smart in its proposal of programs depending on the severity of the offense.

Alternatives Considered

1. Hardcoded recommendations

   Not flexible

2. Data-based dynamic logic.

   Scalable
   Maintainable

Decision

Implemented logic of recommendation in Youth model using:

offence severity ranking
filtering SupportProgram

Consequences

Enables dynamic recommendations
Improves system intelligence
Shows business logic design.

Summary

These choices will guarantee:

 Strong object-oriented design
 Appropriate data modelling and relationships.
 Well defined isolation of concerns.
 Scalable and maintainable architecture

The system is based on youth justice practice in the world but also demonstrates best practices in Django design.
---
>>>>>>> b905a980f57daac774bb526b593ea165c697a50a

Status: Accepted

Context

Various programs may be offered and taken up by a youth, as well as the same program may be offered to several youths.

Alternatives Considered

1. One-to-many relationship

   Too restrictive

2. Many-to-many

   Flexible
   Realistic

Decision

Used ManyToManyField in Youth model.

Consequences

Supports flexible assignments
Improves data relationships
Reflects real-world scenarios

<<<<<<< HEAD
ADR 9: Use Recommendation Logic by Severity.

Status: Accepted

Context

The system ought to be smart in its proposal of programs depending on the severity of the offense.

Alternatives Considered

1. Hardcoded recommendations

   Not flexible

2. Data-based dynamic logic.

   Scalable
   Maintainable

Decision

Implemented logic of recommendation in Youth model using:

offence severity ranking
filtering SupportProgram

Consequences

Enables dynamic recommendations
Improves system intelligence
Shows business logic design.

Summary

These choices will guarantee:

 Strong object-oriented design
 Appropriate data modelling and relationships.
 Well defined isolation of concerns.
 Scalable and maintainable architecture

The system is based on youth justice practice in the world but also demonstrates best practices in Django design.
=======
**Consequences:**  
Less polluted, reusable and adheres to Django best practices.
>>>>>>> b905a980f57daac774bb526b593ea165c697a50a
>>>>>>>

(ADR 1) Database design using models.

## Status

Accepted

## Context

The system needs to be properly stored in data.

## Decision

Database design with used Django models.

## Rationale

Models offer articulate structure and relationships.

## Consequences

* Efficient data handling
* Needs to be designed properly.

ADR 2: Django Admin Panel.

## Status

Accepted

## Context

Information must be handled in a convenient way.

## Decision

Used Django admin panel.

## Rationale

Offers pre-made interface in data management.

## Consequences

* Faster data entry
* Limited customization

Aim: Learn to design a webpage using HTML and CSS.

## Status

Accepted

## Context

The interface to the system must be user-friendly.

## Decision

UI was built with used simple HTML and CSS.

## Rationale

* Easy to implement
* Clear presentation

## Consequences

* Simple design
* Limited advanced features

Application: Migrations should be used to update databases.

## Status

Accepted

## Context

Development of database structure.

## Decision

Used Django migrations.

## Rationale

Allows proper and safe database updates.

## Consequences

* Easy updates
* Requires migration management

ADR 5: Development Support through AI Tools.

## Status

Accepted

## Context

There is a lot of coding and debugging in the project.

## Decision

Used AI tools such as ChatGPT.

## Rationale

* Helps generate code
* Assists debugging
* Improves productivity

## Consequences

* Faster development
* Needs to validate AI-generated code.

ADR 1: Django Framework.

## Status

Accepted

## Context

The project will need a developed web-based application to handle youth information and suggestions.

## Decision

As the key framework, we selected Django.

## Rationale

Django offers such built-in functionality as ORM, administration panel and security.

## Consequences

* Faster development
* Easier database handling
* Must have knowledge of Django architecture.

This view contains a recommendation logic that is defined in the ADR 2 recommendation logic.

## Status

Accepted

## Context

The system should propose appropriate programs on the basis of youth data.

## Decision

Django views are used to implement recommendation logic.

## Rationale

Views may be dynamically filtered and integrated with models.

## Consequences

* Flexible logic
* Easy to update
* Needs proper query processing.

ADR 3: Django Templates.

## Status

Accepted

## Context

The app should have a frontend to present data.

## Decision

Templates in HTML and CSS of Django used.

## Rationale

Allows dynamic rendering and separation of concerns.

## Consequences

* Clean structure
* Easy UI updates
X Weak advanced UI.

SQLite Database is used.

## Status

Accepted

## Context

Data on youth and programs needs a database.

## Decision

SQLite (default Django database) used.

## Rationale

* Easy setup
* No external configuration
* Suitable for small projects

## Consequences

* Simple to use
* Not suitable to large scale production.

Version control in GitHub.

## Status

Accepted

## Context

Several team members are needed to work on the project.

## Decision

Used GitHub to do version control and collaboration.

## Rationale

* Tracks changes
* Supports teamwork
* Maintains code history

## Consequences

* Better collaboration
* needs to know Git commands.
