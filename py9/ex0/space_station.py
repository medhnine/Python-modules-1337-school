from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    station_id: str = Field(min_length=3, max_length=10)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        station = SpaceStation(
            name="International Space Station",
            crew_size=6,
            station_id="ISS001",
            power_level=85,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2022-03-12"),
            is_operational=True
        )
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew : {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print("Status:", "Operational" if station.is_operational else
              "Not Operational")
        print("========================================")
        print("\nExpected validation error:")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    try:
        station = SpaceStation(
            name="mohamed",
            crew_size=67,
            station_id="id_345",
            power_level=90,
            oxygen_level=33,
            last_maintenance=datetime.fromisoformat("2022-03-12"),
            is_operational=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
