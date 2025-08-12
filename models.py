from typing import Optional
from sqlmodel import SQLModel, Field

class Election(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date: str
    level: str  # federal/state/local

class Contest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    election_id: int
    office: str
    jurisdiction: str

class Candidate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contest_id: int
    name: str
    party: str | None = None
    external_refs: str | None = None  # JSON string of external IDs

class Issue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    min_val: int = 0
    max_val: int = 100

class CandidateIssue(SQLModel, table=True):
    candidate_id: int
    issue_id: int
    score: int  # 0-100