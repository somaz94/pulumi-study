# utils.py
from config import PREFIX

class ResourceNamer:
    def __init__(self, prefix: str = PREFIX):
        self.prefix = prefix

    def get_name(self, base_name: str) -> str:
        return f"{self.prefix}-{base_name}"

