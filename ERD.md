Entity Relationship Diagram (ERD)

Overview

The Youth Diversion System is set up to handle the processing of this youth profile, monitor offences and provide guidance on the support programs they need. The system involves three key entities; Youth, Obviation and Support Program.

The data monitoring and intervention strategy decision-making is aided by relationships between these entities.

ERD Diagram

```mermaid
erDiagram
    YOUTH ||--o{ OFFENCE : has
    YOUTH {o--o{ SUPPORT_PROGRAM: receives

    YOUTH {
        int id PK
        string name
        int age
        string gender
        string school_status
        string familysupportlevel
        text background_notes
        datetime created_at
    }

    OFFENCE {
        int id PK
        int youth_id FK
        string offence_type
        string severity
        text notes
        date date_reported
    }

    SUPPORT_PROGRAM {
        int id PK
        string name
        string program_type
        text description
    }