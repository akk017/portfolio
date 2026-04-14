import os
from abc import ABC, abstractmethod

class BaseConfig(ABC):

    @property
    @abstractmethod
    def base_path(self) -> str:
        raise NotImplementedError("abstract class")

    @property
    @abstractmethod
    def docs_path(self):
        raise NotImplementedError("abstract class")
        
    @property
    @abstractmethod
    def build_path(self):
        raise NotImplementedError("abstract class")


class Config(BaseConfig):

    def __init__(self, base: str, docs: str, build: str, templates: str) -> None:
        super().__init__()

        self._base_path = os.path.abspath(base)
        self._docs_path = os.path.join(self._base_path, docs)
        self._build_path = os.path.join(self._base_path, build)
        self._templates_path = os.path.join(self._base_path, templates)

    @property
    def base_path(self) -> str:
        return self._base_path
        
    @base_path.setter
    def base_path(self, value):
        raise ValueError("cannot set basepath")

    @property
    def docs_path(self) -> str:
        return self._docs_path
        
    @docs_path.setter
    def docs_path(self, value: str):
        path = os.path.join(self.base_path, value)
        
        if not os.path.exists(path):
            raise IOError(f"path not found, {path=}")
        self._docs_path = path

    @property
    def build_path(self) -> str:
        return self._build_path
        
    @build_path.setter
    def build_path(self, value):
        path = os.path.join(self.base_path, value)
        
        if not os.path.exists(path):
            raise IOError(f"path not found, {path=}")
        self._build_path = path
        
    @property
    def templates_path(self) -> str:
        return self._templates_path
        
    def __repr__(self) -> str:
        vars = [
            self.__class__.__name__,
            f"docs='./{os.path.relpath(self.docs_path, self.base_path)}'",
            f"build='./{os.path.relpath(self.build_path, self.base_path)}'",
            f"templates='./{os.path.relpath(self.templates_path, self.base_path)}'"
        ]

        return "<" + " ".join(vars) + ">"
