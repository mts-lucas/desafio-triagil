from dataclasses import dataclass
import requests

@dataclass
class PokemonDTO:
    name: str = None
    weight: int = None
    height: int = None