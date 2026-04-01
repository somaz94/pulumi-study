# utils.py
# Canonical utility for consistent resource naming across all Pulumi projects.
# Each project has a local utils.py that imports PREFIX from its own config.py.
#
# Standard pattern:
#
#   from config import PREFIX
#
#   class Utils:
#       @staticmethod
#       def resource_name(base_name: str) -> str:
#           return f"{PREFIX}-{base_name}"
#
# All projects should follow this pattern for consistency.

from config import PREFIX


class Utils:
    @staticmethod
    def resource_name(base_name: str) -> str:
        return f"{PREFIX}-{base_name}"
