Architecture Decision Record (ADR).

Project: Youth Diversion & Support Matching System

ADR 1: Core Entities Separated Models.
Status: Accepted  

Context  
The data types that need to be handled by the system are the youth, offences and support programs.

Alternatives  
- Single model -good performance, due to simplicity but it has poor scalability and redundancy of data.  
- Separate models → easier to maintain and structure (chosen)

Decision  
Created Youth, Offence, and SupportProgram models.

Code Reference  
justice_app/models.py: 5–80  

Consequences  
- Improved maintainability and structure.  
- Supports object-oriented design  
- Conforms to Django model-driven architecture.  

ADR 2: One-to-Many (Youth → Offence)
Status: Accepted  

Context  
More than once may a youth commit many offences.

Alternatives  
- Store crimes in Youth → no adequate history tracking.  
- Separate model with ForeignKey to has ForeignKey - multiple records (chosen).

Decision  
FK Youth to Offence.

Code Reference  
justice_app/models.py: 82–110  

Consequences  
- Supports offence history  
- Allows access to most recent offence.  
- A little more advanced queries.  

ADR 3: Youth Multiple to Multiple (Youth ↔ SupportProgram)
Status: Accepted  

Context  
There are various support programs that can be done by youth.

Alternatives  
- ForeignKey - restricts to one youth per program.  
ManyToMany 1 many to many (chosen).

Decision  
Used ManyToManyField in Youth.

Code Reference  
justice_app/models.py: 25–35  

Consequences  
- Flexible program assignment  
- Scalable relationship design  
- Adds relational complexity  

ADR 4: Append Filters in SupportProgram.
Status: Accepted  

Context  
Programs should be appropriate to the youth characteristics including age and level of risk.

Alternatives  
- Simple model - no significant filtering.  
- Add filtering fields-Dynamic matching (chosen) is possible.

Decision  
Appendix minage, maxage and risk level.

Code Reference  
justice_app/models.py: 40–70  

Consequences  
- Enables personalised recommendations  
- Improves system intelligence  
- Demands precise input of data.  

ADR 5: Use QuerySets for Recommendations
Status: Accepted  

Context  
Guidelines need to be dynamic and scalable.

Alternatives  
- Hardcoded logic → not maintainable  
- QuerySets → dynamic and scalable (chosen)

Decision  
Filtered support programs by using Django QuerySet.

Code Reference  
justice_app/views.py: 10–50  

Consequences  
- Efficient and scalable logic  
- Militates with Django ORM.  
- Relies on clean database information.  

ADR 6: Use Latest Offence
Status: Accepted  

Context  
There could be various offenders on the record of youth.

Alternatives  
- First time offence - not reliable.  
- Latest offence→ represents current behaviour (chosen)

Decision  
Recently committed crime used in the reasoning process.

Code Reference  
justice_app/views.py: 20–40  

Consequences  
- straightforward and explicit reasoning.  
- Easy to explain  
- Does not take into account entire offence history.  

ADR 7: Explanation of Show Recommendation.
Status: Accepted  

Context  
Users should have the knowledge of the reasons behind recommendations.

Alternatives  
- Show programs only → is not that transparent.  
- Show explanation => enhances clarity (chosen)

Decision  
Added a why recommended section to UI.

Code Reference  
justice_app/views.py: 45–65  
justice_app/templates/recommendations.html: 15–40  

Consequences  
- Improves transparency  
- Strengthens system justification  
- Marginal rise in the complexity of UIs.  

ADR 8: Distinguish Logic and UI.
Status: Accepted  

Context  
Templates are not supposed to put business logic.

Alternatives  
- Logic in templates → difficult to maintain.  
- Logic in views/models → clean structure (chosen)

Decision  
Sharing Django CMS framework.

Code Reference  
justice_app/views.py: 1–70  
justice_app/templates/: all files  

Consequences  
- Separation of concerns a la carte.  
Easier debugging and maintenance.  

ADR 9: Follow Django Design Principles
Status: Accepted  

Context  
The right architectural practice should be adopted in the system.

Decision  
The Django design principles that have been applied:
- DRY (Don’t Repeat Yourself)  
- Thin Views, Fat Models.  
- Separation of concerns  

Code Reference  
justice_app/models.py: 1–120  
justice_app/views.py: 1–70  

Consequences  
- Tidy and most maintainable code.  
-Good adherence to Django best practices.  
- Needs wise design choices.
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
