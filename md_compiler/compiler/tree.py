import os
from .meta import Meta
from enum import StrEnum


class PathType(StrEnum):
    FILE = "file"
    DIR = "directory"
        
    
class PathNode:

    def __init__(self, name, path) -> None:
        super().__init__()
        self._name = name
        self._path = path
        self._is_dir = False
        self._children: list['PathNode'] = []
        
        self._files = []
        self._dirs = []

        self._meta = Meta()

        if not os.path.exists(path):
            raise FileNotFoundError(f"file not found, {path=}")
        self._path = os.path.abspath(path)
                
        if os.path.isdir(self._path):
            self._is_dir = True
        else:
            self._is_dir = False
            
    def __str__(self) -> str:
        return f"<node path={self._path}>"

    @property
    def name(self) -> str:
        return self._name
        
    @name.setter
    def name(self, value: str):
        self._name = value
        
    @property
    def meta(self) -> Meta:
        return self._meta
        
    @meta.setter
    def meta(self, value: Meta):
        self._meta = value
        
    @property
    def path(self) -> str:
        return self._path

    def rel_path(self, relative_path) -> str:
        return os.path.relpath(self._path, relative_path)

    @path.setter
    def path(self, path: str):
        return self.path

    @property
    def type(self) -> 'PathType':
        return PathType.DIR if self._is_dir else PathType.FILE
    
    @property
    def is_file(self):
        return not self._is_dir
    
    @property
    def is_dir(self):
        return self._is_dir
        
    @property
    def children(self) -> list['PathNode']:
        return self._children
        
    @property
    def files(self) -> list['PathNode']:
        return self._files
    
    @property
    def dirs(self) -> list['PathNode']:
        return self._dirs

    def add_child(self, node: 'PathNode'):
        if self.is_file:
            raise ValueError("cannot add child to file node")
        if node.is_dir:
            self._dirs.append(node)
        else:
            self._files.append(node)

        self._children.append(node)
        
    def remove_child(self, node: 'PathNode'):
        if self.is_file:
            raise ValueError("cannot add child to file node")
        self._children.remove(node)
    