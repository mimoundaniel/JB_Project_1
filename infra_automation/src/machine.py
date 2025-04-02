from pydantic import BaseModel, field_validator
import logging

class Machine(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int

    @field_validator('cpu', 'ram')
    def check_positive(cls, value):
        if value <= 0:
            raise ValueError('CPU and RAM must be positive integers')
        return value

    def to_dict(self):
        return self.model_dump()

    def __init__(self, **data):
        super().__init__(**data)
        logging.info(f"Machine created: {self.to_dict()}")
