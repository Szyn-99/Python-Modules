from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
from typing import Optional, Self

class ContactType(Enum):
    rad = "radio"
    vis = "visual"
    phi = "physical"
    tel = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False
    @model_validator(mode='after')
    def a_function(self) -> Self:
        if not self.contact_id.startswith('AC'):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.phi.value and not self.is_verified:
            raise ValueError('Physical contact must be verified')
        if self.contact_type == ContactType.tel and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')
        if self.message_received and self.signal_strength < 7.0:
            raise ValueError('Strong signals (> 7.0) should include received messages')
        return self


def main() -> None:
    try:
        print("Alien Contact Log Validation")
        print("======================================")
        alien_contact = AlienContact(contact_id="AC_2024_001", contact_type="radio", timestamp="3030-12-21",location="Area 51, Nevada", signal_strength=8.5, duration_minutes=45, witness_count=5, message_received='Greetings from Zeta Reticuli')
        print("Valid contact report:")
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: '{alien_contact.message_received}'")
        print("======================================\n")
        print("Expected validation error:")
        try:
            alien_contact = AlienContact(contact_id="AC_2024_001", contact_type="telepathic", timestamp="3030-12-21",location="Area 51, Nevada", signal_strength=8.5, duration_minutes=45, witness_count=1, message_received='Greetings from Zeta Reticuli')
        except ValidationError:
            for error in e.errors():
                print(f"{error['msg']}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")

if __name__ == "__main__":
    main()
            