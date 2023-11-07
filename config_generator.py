import os
import json
from pydantic import BaseModel
from pydantic.json import pydantic_encoder
class Controller_Config(BaseModel):
    command_name: str
    keys: list[str]
    duration: float
    cooldown: float | None
    chance: float | None


def create_config(configs: list[Controller_Config], filename:str,  folder:str | None) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, folder, f"{filename}.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w+') as f:
        serialized = json.dumps(configs, default=pydantic_encoder)
        f.write(serialized)

if __name__ == "__main__":
    configs = [
        Controller_Config(command_name="kill", keys=["k"], duration=1, cooldown=30, chance=0.5),
        Controller_Config(command_name="everyone", keys=["e"], duration=1, cooldown=30, chance=0.5),
        Controller_Config(command_name="you", keys=["y"], duration=1, cooldown=1, chance=0.5),
        Controller_Config(command_name="see", keys=["s"], duration=1, cooldown=1, chance=0.5),

    ]
    create_config(configs, "test", "config")
