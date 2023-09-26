# utils.py
from config import PREFIX

class Utils:
    @staticmethod
    def resource_name(base_name: str) -> str:
        return f"{PREFIX}-{base_name}"

