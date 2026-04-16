
ADR 1: Separation of Core Entities into Models.

Context
The system should be in control of various kinds of data such as youth profiles, offence records and support programs. All these depict a different thing with its own set of attributes and duties.

Decision
Each core entity had its own separate Django models:
- Youth
- Offence
- SupportProgram

This makes each entity work independently in the system.

Consequences
- Enhances maintainability and modularity.
- Facilitates clean and structured database design.
- Conforms to principles of object-oriented programming.
- Makes the system more extendible in future.

ADR 2: One-to-Many Youth, Offence Relationship.

Context
There may be several offences committed by one youth. All offences must be marked individually although associated with the appropriate youth.

Decision
ForeignKey relationship between Offence and Youth was implemented:

```python
youth = models.ForeignKey(Youth, ondelete=models.CASCADE, relatedname='offences')

Consequences
	•	Allows one-to-many (one youth to many offences) relationship.
	•	Allows access to offence history of every youth.
	•	Enables the latest offence to be identified in order to make a recommendation logic.
	•	Upholds regular database format.

⸻

ADR 3: Multiple to Multiple Relationship between Youth and Support Programs.

Context

A youth can be involved in numerous support programs, and support program can be allocated to a number of youths. The relation should be elastic, extendable.

Decision

A ManyToManyField was used in the Youth model:

support_programs = models.ManyToManyField(SupportProgram, blank=True)

Consequences
	•	Provides the flexibility of assigning programs to youngsters.
	•	Avoids duplication of data
	•	Facilitates additional improvement in the future (tracking participation).
	•	Makes managing relationships easier with Django ORM.

⸻

ADR 4: Attributes Filters in SupportProgram.

Context

The system should suggest appropriate support programs according to youth attributes like age and level of offence. This makes it necessary to filter dynamically.

Decision

The SupportProgram model was modified to include additional fields:
	•	min_age
	•	max_age
	•	risk_level

These characteristics are applied in matching programs with the profiles of youth.

Consequences
	•	Allows interactive filtering with QuerySets.
	•	Favours customised and pertinent suggestions.
	•	Eliminates hardcoding.
	•	Enhances intelligence of a system.

⸻

Given query sets, recommend logic.

Context

The system should be able to come up with the recommendations in real time using the up-to-date data on the youth (such as age, severity of offence, school status, and level of family support expected to support him/her).

Decision

Django QuerySets were used to implement the logic of recommendation in the application:

programs = SupportProgram.objects.filter(
    minage_lte=youth.age,
    maxage_gte=youth.age
)

Further screening is done according to the severity of offenses and youth status.

Consequences
	•	Scalable and efficient data filtering.
	•	Maintains logic dynamic, flexible.
	•	Does not use raw SQL, which makes it easier to read and more secure.
	•	Conforms to Django best practices.


Conclusion

The architectural choices of this system are aimed at developing a scaled, maintainable and a structured solution. The system allows it to recommend appropriate support programs to the youth according to individual situations and is therefore suitable to achieve its aim using normalized models, appropriate relationships and dynamic QuerySet filtering.

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
