from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
