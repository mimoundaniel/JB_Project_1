from pydantic import BaseModel, field_validator
import logging



logging.basicConfig(level=logging.INFO, filename='infra_automation/logs/provisioning.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
        return self.dict()

    def __init__(self, **data):
        super().__init__(**data)
        logging.info(f"Machine created: {self.to_dict()}")
