import os
import json
from pydantic import BaseModel

class Controller_Config(BaseModel):
    command_name: str
    keys: list[str]
    duration: float
    cooldown: float | None
    chance: float | None

def create_config(configs: list[Controller_Config], config_name:str,  path:str) -> list[Controller_Config]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, path, f"{config_name}.json")
    with open(file_path, 'w') as f:
        serialized = ([config.model_dump_json for config in configs])
        f.write(serialized)

if __name__ == "__main__":
    configs = [
        Controller_Config(command_name="test", keys=["k"], duration=1, cooldown=30, chance=0.5),
        Controller_Config(command_name="test", keys=["e"], duration=1, cooldown=30, chance=0.5),
        Controller_Config(command_name="test", keys=["y"], duration=1, cooldown=1, chance=0.5),
    ]
    
