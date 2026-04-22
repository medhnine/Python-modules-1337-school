from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


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
    crew: list[CrewMember] = Field(min_length=1, max_length=10)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with M")
        ranks: list = [member.rank for member in self.crew]
        if Rank.captain not in ranks and Rank.commander not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )

        active: list = [
            member for member in self.crew if member.is_active is False
        ]
        if len(active) > 0:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        member1 = CrewMember(
            member_id="Md_78",
            name="Sarah Connor",
            rank=Rank.commander,
            age=35,
            specialization="Mission Command",
            years_experience=6,
            is_active=True,
        )
        member2 = CrewMember(
            member_id="Md_99",
            name="John Smith",
            rank=Rank.lieutenant,
            age=22,
            specialization="Navigation",
            years_experience=2,
            is_active=True,
        )
        member3 = CrewMember(
            member_id="Md_22",
            name="Alice Johnson",
            rank=Rank.commander,
            age=40,
            specialization="Engineering",
            years_experience=7,
            is_active=True,
        )
        members: list = [member1, member2, member3]

        station = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2022-03-12"),
            duration_days=900,
            crew=members,
            mission_status="Mission Command",
            budget_millions=2500.0,
        )
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station.mission_id}")
        print(f"Mission: {station.mission_name}")
        print(f"Destination: {station.destination}")
        print(f"Duration: {station.duration_days}")
        print(f"Budget ${station.budget_millions}")
        print(f"Crew size: {len(members)}")
        print("Crew members:")

        for i in members:
            print(f"- {i.name} ({i.rank}) - {i.specialization}")

        print("========================================")
        print("\nExpected validation error:")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    try:
        member = [
            CrewMember(
                member_id="Md_78",
                name="Sarah Connor",
                rank=Rank.officer,
                age=35,
                specialization="Command",
                years_experience=2,
                is_active=True,
            )]
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2022-03-12"),
            duration_days=900,
            crew=member,
            mission_status="Command",
            budget_millions=2500.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
