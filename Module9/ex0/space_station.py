from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200)


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        ss = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="3077-12-31",
            is_operational=True,
            notes=None,
        )
        op = 'Operational' if ss.is_operational else 'Not Operational'
        print("Valid station created:")
        print(f"ID: {ss.station_id}")
        print(f"Name: {ss.name}")
        print(f"Crew: {ss.crew_size} people")
        print(f"Power: {ss.power_level}%")
        print(f"Oxygen: {ss.oxygen_level}%")
        print(
            f"Status: {op}"
        )
        print("========================================")
        print("Expected validation error:")
        try:
            SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=1000,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance="3077-12-31",
                is_operational=True,
                notes=None,
            )
        except ValidationError as e:
            for error in e.errors():
                print(f"{error['msg']}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
