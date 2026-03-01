from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from typing import Optional, List, Self
from datetime import datetime

class Rank(Enum):
    cad = "cadet"
    off = "officer"
    lie = "lieutenant"
    cap = "captain"
    comm = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)
    @model_validator(mode='after')
    def another_function(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        filter = sum(1 for cr in self.crew if cr.rank == Rank.comm or cr.rank == Rank.cap)
        if filter == 0:
            raise ValueError('Must have at least one Commander or Captain')
        if self.duration_days > 365:
            experience_rate = sum(1 for cr in self.crew if cr.years_experience >= 5) / len(self.crew) if len(self.crew) > 0 else 0
            if 0.5 > experience_rate:
                raise ValueError('Long missions (> 365 days) need 50% experienced crew (5+ years)')
        for cr in self.crew:
            if not cr.is_active:
                raise ValueError('All crew members must be active')
        return self

def main():
    try:

        print("Space Mission Crew Validation")
        print("=========================================")

        commander = CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.comm,
            age=42,
            specialization="Mission Command",
            years_experience=15,
            is_active=True
        )

        lieutenant = CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.lie,
            age=35,
            specialization="Navigation",
            years_experience=8,
            is_active=True
        )

        officer = CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.off,
            age=29,
            specialization="Engineering",
            years_experience=6,
            is_active=True
        )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15),
            duration_days=900,
            crew=[commander, lieutenant, officer],
            mission_status="planned",
            budget_millions=2500.0
        )

        print(f"Valid mission created:")
        print(f"  Mission:     {mission.mission_name}")
        print(f"  ID:          {mission.mission_id}")
        print(f"  Destination: {mission.destination}")
        print(f"  Duration:    {mission.duration_days} days")
        print(f"  Budget:      ${mission.budget_millions}M")
        print(f"  Crew size:   {len(mission.crew)}")
        print(f"  Crew members:")
        for member in mission.crew:
            print(f"    - {member.name} ({member.rank.value}) - {member.specialization}")

        print("\n=========================================")

        print("Expected validation error:")
        try:
            cadet = CrewMember(
                member_id="CM004",
                name="Bob Lee",
                rank=Rank.cad,
                age=22,
                specialization="Logistics",
                years_experience=1,
                is_active=True
            )

            SpaceMission(
                mission_id="M2024_FAIL",
                mission_name="Doomed Mission",
                destination="Venus",
                launch_date=datetime(2024, 8, 1),
                duration_days=200,
                crew=[cadet],
                mission_status="planned",
                budget_millions=500.0
            )

        except ValidationError as e:
            for error in e.errors():
                print(f"{error['msg']}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")

if __name__ == "__main__":
    main()
