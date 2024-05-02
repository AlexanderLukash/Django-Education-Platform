from dataclasses import dataclass


@dataclass(eq=False)
class ServiceException(Exception):
    @property
    def message(self) -> str:
        return 'Application exception accured'
