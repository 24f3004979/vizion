from dataclasses import dataclass

@dataclass
class EditRequest:
    location:tuple[str|int, str]
    content:str|int

@dataclass
class FetchRequest:
    location:tuple[str|int, str|int]