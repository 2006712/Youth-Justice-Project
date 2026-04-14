Architecture Decision Records

This document is a record of key architectural decisions as the Youth Diversion and Support Matching System was developed. Such decisions provide the rationale for the design decision, other alternatives, and the consequences of the decision.

ADR 1: Use a separate Offence model linked to Youth

Status
Accepted

Context
It ought to have a lot of offences in its system of the Youth. Any youth may have various crimes in their lives.

Alternatives Considered
1. Retain all the offences in the Youth model.  
   - Not scalable  
   - Causes data duplication  

2. Involve another Offence model.  
   - More structured  
   - Supports multiple records

Decision
And we decided to develop an Offence model on its own and connect it to the Youth model with a ForeignKey.

Consequences
- Allows one Youth to have multiple offences  
- Keeps data organised  
- Improves scalability  

Code Reference
justice_app/modelling code/justice_youth_and offence models.py

ADR 2: Use ForeignKey for Youth–Offence relationship

Status
Accepted

Context
A youth may have more than a single offence, but only one Youth has a single offence.

Alternatives Considered
1. ManyToMany relationship  
   - Inappropriate since a crime is a part of a young generation.  

2. ForeignKey  
   - This obviously depicts a one-to-many relationship.  

Decision
All the offences were related to the specific Youth through foreignkey in the Offence model.

Consequences
- One to many relationship is evident.  
- Makes querying easier  
- Improves data consistency  

Code Reference
justice_app/models.py (Offence model)

ADR 3: Provide share timestamp fields with BaseModel.

Status
Accepted

Context
Createdat and updatedat are needed in all the models within the system.

Alternatives Considered
1. Include timestamp fields in each model.  
   - Generates the duplication of the code.  

2. Instantiate a BaseModel, which is an abstraction.  
   - Maximum reuse and reprocessing.  

Decision
We also created a abstract BaseModel to store universal timestamp items and also used other models to inherit.

Consequences
- Reduces code duplication  
- Improves maintainability  
- Follows Django best practices  

Code Reference
justice_app/models.py (BaseModel)

ADR 4: Retrieval logic of offence: model stay.

Status
Accepted

Context
The system should reach the latest delinquencies of each youngster. Such a type of reasoning is required in different places.

Alternatives Considered
1. bring sanity to perceptions.  
   - Not reusable  
   - Posses a violation of separation of concerns.  

2. Introduce logic within the model.  
   - Reusable  
   - Cleaner architecture  

Decision
To manage this logic, we have added a method getRecentOffences () to the Youth model.

Consequences
- Improves encapsulation  
- Keeps views simple  
- Enables reuse of logic throughout the system.  

Code Reference
justice_app/models.py (Youth model)

ADR 5: Design a system that supports the needs of many youths.

Status
Accepted

Context
School students are not the only Youth who use the justice system. They can also be composed of people who have dropped out, are unemployed, or are not well supported by their families.

Alternatives Considered
1. Design a system exclusively for students.  
   - Too limited  
   - Not realistic  

2. Design a system involving a wider population of youths.  
   - More flexible  
   - Real-world applicable  

Decision
One of the fields we featured was schoolstatus, familysupportlevel, and backgroundnotes to depict varied situations among Youth.

Consequences
- Makes the system more lifelike.  
- Helps to understand the situation with young people better.  
- Enhances recommendation logic in the future.  

Code Reference
justice_app/models.py (Youth model)

ADR 6: Use a diversion and support-based approach instead of crime tracking

Status
Accepted

Context
Conventional systems are centred on crime monitoring and punishment. But the youth justice systems are set to rehabilitate and help people.

Alternatives Considered
1. Crime tracking system  
   - Concentrates on crimes.  
   - Does not favour rehabilitation.  

2. Support the matching system  
   - Is oriented to intervention and rehabilitation.  
   - Less meaningless and unethical.  

Decision
We developed a Youth Diversion and Support Matching System, where we need advice on support programs rather than merely registering crimes.

Consequences
- Has a more correct and contemporary objection.  
- Supports early intervention  
- Conformed to real-world youth justice practice.  

Code Reference
Future Support Program model Project design.

ADR 7: Prepare system to support program equivalent.

Status
Accepted

Context
The system shall subsequently suggest support programs based on youth data and a history of offences.

Alternatives Considered
1. View code logic.  
   - Not scalable  
   - Difficult to maintain  

2. Formulate designed forms and fields to match.  
   - Scalable  
   - Easier to extend  

Decision
We modelled the data structure with fields (age, offence degree, school status, and family support level) to support future recommendation logic.

Consequences
- Makes the system extensible  
- Enables the recommendation engine in the future.  
- Enhances the design quality.  

Code Reference
justice/models.py (Youth and Offence models)

---

## ADR: Intervention-based recommendations should be done using a SupportProgram model.

**Status:** Accepted

**Context:**  
The project is modeled to be a Youth Diversion and Support Matching System. The system should not just be interested in storing offence records only but it should also suggest appropriate support opportunities like counselling, training, and community service. These support options had to be represented in a separate model.

**Alternatives considered:**  
1. Save the program names in the form of plain text in Youth model.  
2. Store program options within Recommendation model.  
3. Prepare a SupportProgram model.  

**Decision:**  
Special SupportProgram model was developed with such fields like name, category, description, minimum age, maximum age, risk level supported and active status.

**Consequences:**  
Enhances structure, scalability, and recommends logic.

---

ADR: Have an eligibility logic of support program supported by a custom manager.

**Status:** Accepted

**Context:**  
The system must have recommendations on programs according to age and risk. The repeat of filtering logic in more than one place complicates code.

**Alternatives considered:**  
1. Put logic in views  
2. Lean logic to Youth model.  
3. Custom manager.  

**Decision:**  
Used SupportProgramManager with eligibility to youth method, which is eligible_for_youth(youth).

**Consequences:**  
Less polluted, reusable and adheres to Django best practices.