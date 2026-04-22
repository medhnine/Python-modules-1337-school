from datetime import datetime
from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
    )
    is_verified: bool = False

    @model_validator(mode="after")
    def is_valid(self):
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError('Physical contact reports must be verified')
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    try:
        station = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            timestamp=datetime.fromisoformat("2022-03-12"),
            contact_type=ContactType.radio,
            signal_strength=0.85,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'",
            is_verified=False,
        )
        print("Alien Contact Log Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station.contact_id}")
        print(f"type: {station.contact_type}")
        print(f"Location: {station.location}")
        print(f"Signal: {station.signal_strength}")
        print(f"Duration: {station.duration_minutes} minutes")
        print(f"Witnesses: {station.witness_count}")
        print(f"Message: {station.message_received}")
        print("\n========================================")
        print("Expected validation error:")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    try:
        AlienContact(
            contact_id="AC001_TEST",
            location="Area 51, Nevada",
            timestamp=datetime.fromisoformat("2022-03-12"),
            contact_type=ContactType.telepathic,
            signal_strength=9.0,
            duration_minutes=45,
            witness_count=2,
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
