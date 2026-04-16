Architecture Decision Records (ADR).

This report documents major decisions taken in the architecture of the development of Youth Diversion and Support Matching System. The systematic design thinking can be seen in each choice where the circumstances, options, resolution, and outcomes are given.

ADR 1: Youth-linked Separate Offence Model.

Status: Accepted

Context

Some of these offences may be perpetrated by the same youth with time. Having all the offence information contained in the Youth model would be redundant and would be inefficient to scale.

Alternatives Considered

1) Hit and miss offence within Youth model.

   Not scalable
   Causes data duplication

2. Develop another Offence model.

   Structured data
   Supports multiple records

Decision

Another Offence model was defined and was connected with Youth through a ForeignKey.

Consequences

 Supports one-to-many relationship
 Improves scalability and normalization
 Enables efficient querying

Code Reference: 

ADR 2: Use ForeignKey for Youth–Offence Relationship

Status: Accepted

Context

There is only one young individual associated with an offence and a youth can be associated with several offenses.

Alternatives Considered

1. ManyToMany

   Incorrect relationship representation

2. ForeignKey

   Accurately represents one-to-many

Decision

ForeignKey on Offence model to Youth that is used.

Consequences

Maintains referential integrity
Simplifies queries
Reflects real-world structure

ADR 3: Add BaseModel of Shared Fields.

Status: Accepted

Context

Every model must have such common fields as createdat and updatedat.

Alternatives Considered

Please duplicate fields in both the models.

   Repetitive
   Hard to maintain

2. Abstract BaseModel

   Reusable
   Cleaner design

Decision

Developed a BaseModel, upon which Youth and Offence are based.

Consequences

Reduces duplication
Improves maintainability
Abides by Django best practices.

ADR 4: Model business logic.

Status: Accepted

Context

Logic, including the retrieval of recent offences or programs recommended, are applied in several aspects of the system.

Alternatives Considered

Embed logics in views.

   Not reusable
   Breaks separation of concerns.

2. Put logic within models.

   Reusable
   Cleaner architecture

Decision

Introduction of approaches like:

getrecentoffences()
recommend_programs()
  within the Youth model.

Consequences

Improves encapsulation
Abides by thin views (easy views).
Encourages reuse

ADR 5: Formulate The Youth Model to Show the Real World Diversity.

Status: Accepted

Context

Young people in the justice system belong to various origins, and do not necessarily include school children.

Alternatives Considered

1. simplified model (students only)

   Unrealistic
   Limited analysis

2. Expanded attributes

   More realistic
   Better decision-making

Decision

Included fields:

school_status
familysupportlevel
background_notes

Consequences

Improves realism
Supports better recommendations
Enables future analytics

ADR 6: Implement a Diversion-based System, as an alternative to Crime Tracking.

Status: Accepted

Context

Unlike the old systems which are based on the registration of the offences, the youth justice of the day leans more on rehabilitation.

Alternatives Considered

1. Crime tracking system

   Focuses on punishment
   Limited impact

2. Support-based system

   Focuses on rehabilitation
   More meaningful

Decision

Established a Youth Diversion and Support Matching System.

Consequences

Corresponds with actual activities.
Supports early intervention
Improves ethical design

ADR 7: Present SupportProgram Model with recommendations.

Status: Accepted

Context

The system needs to prescribe support programs in accordance to the youth data and severity of offences.

Alternatives Considered

1. Name text Stores 1. Name as a text: program name.

   Not scalable
   Difficult to manage

2. Develop individual SupportProgram model.

   Structured
   Extendable

Decision

Since it is our SupportProgram model, fields are:

name
program_type
target_severity
description

Consequences

Enables structured recommendations
Improves scalability
Supports future enhancements

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

