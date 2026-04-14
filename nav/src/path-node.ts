import { type NavItem, type Page, type Section } from './data.js';

export enum PathType {
  FILE = 'file',
  DIR = 'directory',
}

export interface Meta {
  title?: string;
  icon?: string;
}

export class PathNode {
  private _name: string;
  private _path: string;
  private _isDir: boolean;
  private _children: PathNode[] = [];
  private _files: PathNode[] = [];
  private _dirs: PathNode[] = [];
  private _meta: Meta = {};

  constructor(name: string, path: string, isDir: boolean = false) {
    this._name = name;
    this._path = path;
    this._isDir = isDir;
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }

  get path(): string {
    return this._path;
  }

  get isDir(): boolean {
    return this._isDir;
  }

  get isFile(): boolean {
    return !this._isDir;
  }

  get type(): PathType {
    return this._isDir ? PathType.DIR : PathType.FILE;
  }

  get children(): PathNode[] {
    return this._children;
  }

  get files(): PathNode[] {
    return this._files;
  }

  get dirs(): PathNode[] {
    return this._dirs;
  }

  get meta(): Meta {
    return this._meta;
  }

  set meta(value: Meta) {
    this._meta = value;
  }

  addChild(node: PathNode): void {
    if (this.isFile) {
      throw new Error('cannot add child to file node');
    }
    this._children.push(node);
    if (node.isDir) {
      this._dirs.push(node);
    } else {
      this._files.push(node);
    }
  }

  removeChild(node: PathNode): void {
    if (this.isFile) {
      throw new Error('cannot remove child from file node');
    }
    const idx = this._children.indexOf(node);
    if (idx !== -1) {
      this._children.splice(idx, 1);
    }
    if (node.isDir) {
      const dirIdx = this._dirs.indexOf(node);
      if (dirIdx !== -1) {
        this._dirs.splice(dirIdx, 1);
      }
    } else {
      const fileIdx = this._files.indexOf(node);
      if (fileIdx !== -1) {
        this._files.splice(fileIdx, 1);
      }
    }
  }

  toString(): string {
    return `<node path=${this._path}>`;
  }
}

export function buildTree(items: NavItem[], basePath: string = '/'): PathNode {
  const root = new PathNode('root', basePath, true);

  for (const item of items) {
    const child = navItemToNode(item);
    root.addChild(child);
  }

  return root;
}

function navItemToNode(item: NavItem, parentPath: string = '/'): PathNode {
  if (item.type === 'Page') {
    const node = new PathNode(item.title, item.href, false);
    node.meta = { title: item.title, icon: item.icon };
    return node;
  }

  const node = new PathNode(item.title, parentPath + item.title, true);
  node.meta = { title: item.title };

  for (const child of item.children || []) {
    node.addChild(navItemToNode(child, parentPath + item.title + '/'));
  }

  return node;
}