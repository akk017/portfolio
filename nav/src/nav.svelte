<script lang="ts">
    import Fuse from "fuse.js";
    import { navData, type NavItem, type Page } from "./data.js";
    import { buildTree, PathNode as PathNodeClass, type PathNode } from "./path-node.js";

    let query = $state("");
    let current = $state<PathNode[]>([]);

    const tree = buildTree(navData);

    function loadFromStorage(): PathNode[] {
        const saved = localStorage.getItem("nav-path");
        if (!saved) return [];
        try {
            const parts = JSON.parse(saved) as string[];
            const findNode = (nodes: PathNode[], name: string): PathNode | undefined => {
                for (const n of nodes) {
                    if (n.name === name) return n;
                    if (n.isDir) {
                        const found = findNode(n.children, name);
                        if (found) return found;
                    }
                }
                return undefined;
            };
            const path: PathNode[] = [];
            for (const name of parts) {
                const currentNodes = path.length ? path[path.length - 1].children : tree.children;
                const node = findNode(currentNodes, name);
                if (node) path.push(node);
                else return [];
            }
            return path;
        } catch {
            return [];
        }
    }

    $effect(() => {
        const path = current.map(n => n.name);
        localStorage.setItem("nav-path", JSON.stringify(path));
    });

    current = loadFromStorage();

    const fuse = new Fuse(getAllItems(), { keys: ["title"], threshold: 0.4 });

    function getAllItems(): (Page | { type: "folder"; title: string; href: string; folder: boolean; icon: string })[] {
        const items: (Page | { type: "folder"; title: string; href: string; folder: boolean; icon: string })[] = [];
        function walk(nodes: PathNode[]) {
            for (const n of nodes) {
                if (n.isFile)
                    items.push({
                        type: "Page" as const,
                        title: n.name,
                        href: n.path,
                        folder: false,
                        icon: n.meta.icon || "",
                    });
                if (n.isDir) {
                    items.push({
                        type: "folder" as const,
                        title: n.name,
                        href: n.path,
                        folder: true,
                        icon: "folder",
                    });
                    if (n.children.length) walk(n.children);
                }
            }
        }
        walk([tree]);
        return items;
    }

    function currentItems(): PathNode[] {
        const items = current.length
            ? current[current.length - 1].children
            : tree.children;
        const dirs = items
            .filter((n) => n.isDir)
            .sort((a, b) => a.name.localeCompare(b.name));
        const files = items
            .filter((n) => n.isFile)
            .sort((a, b) => a.name.localeCompare(b.name));
        return [...dirs, ...files];
    }

    function enter(n: PathNode) {
        if (n.isDir) current = [...current, n];
    }

    function goto(n: PathNode) {
        window.location.href = n.path;
    }

    function back() {
        if (current.length) current = current.slice(0, -1);
    }

    function breadcrumbs(): { name: string; idx: number }[] {
        if (!current.length) return [];
        return current.map((n, i) => ({ name: n.name, idx: i }));
    }

    function crumbPath(crumbs: { idx: number }[]): string {
        if (!crumbs.length) return "/";
        const last = crumbs[crumbs.length - 1];
        const start = Math.max(0, last.idx - 1);
        return current
            .slice(start, last.idx + 1)
            .map((n) => n.name)
            .join("/");
    }

    function navigate(idx: number) {
        current = current.slice(0, idx + 1);
    }

    function results() {
        return query ? fuse.search(query).map((r) => r.item) : [];
    }
</script>

<div id="nav-container">
    <div id="bar">
        <button onclick={() => (current = [])}
            ><span class="material-icons">bolt</span></button
        >
        <input type="text" bind:value={query} placeholder="search" />
    </div>
    {#if breadcrumbs().length > 0}
        <span class="path">
            {#each breadcrumbs() as c, i}
                <button class="crumb" onclick={() => navigate(c.idx)}
                    >{c.name}</button
                >
                {#if i < breadcrumbs().length - 1}/{/if}
            {/each}
        </span>
    {/if}

    {#if query}
        <ul>
            {#each results() as p}
                <li>
                    <a href={p.href} class="item" class:dir={p.folder} onclick={(e) => {
                        if (p.folder) {
                            e.preventDefault();
                            const findNode = (nodes: PathNode[], name: string, href: string): PathNode | undefined => {
                                for (const n of nodes) {
                                    if (n.name === name && n.path === href) return n;
                                    if (n.isDir) {
                                        const found = findNode(n.children, name, href);
                                        if (found) return found;
                                    }
                                }
                                return undefined;
                            };
                            const node = findNode(tree.children, p.title, p.href);
                            if (node) current = [...current, node];
                            query = "";
                        }
                    }}>
                        <span class="material-icons">{p.folder ? "folder" : "description"}</span>
                        {p.title}
                    </a>
                </li>
            {/each}
        </ul>
    {:else}
        <ul>
            {#each currentItems() as n}
                <button
                    type="button"
                    class="item"
                    class:dir={n.isDir}
                    onclick={() => (n.isDir ? enter(n) : goto(n))}
                >
                    <span class="material-icons"
                        >{n.isDir ? "folder" : "description"}</span
                    >
                    {n.name}
                </button>
            {/each}
        </ul>
    {/if}
</div>

<style>
    #nav-container {
        min-width: 300px;
        font: 13px monospace;
        display: flex;
        justify-content: flex-start;
        flex-direction: column;
        height: 100%;
        opacity: 0.2;
    }
    #nav-container:hover {
        opacity: 1;
    }
    .path {
        padding: 8px 12px;
        background: #f5f5f5;
        display: flex;
        gap: 4px;
        align-items: center;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        text-align: left;
    }
    .crumb {
        background: none;
        border: none;
        cursor: pointer;
        font: inherit;
    }
    .crumb:hover {
        text-decoration: underline;
    }
    #bar {
        display: flex;
        gap: 4px;
        border: 1px solid lightgray;
        height: 20px;
        padding: 4px 6px;

        display: flex;
        justify-content: start;
        align-items: center;
    }
    #bar button {
        background: none;
        border: none;
        cursor: pointer;
        aspect-ratio: 1 / 1;
        padding: 0;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #bar button:hover {
        background: #eee;
    }
    input {
        flex: 1;
        font: inherit;
        border: none;
        width: 100%;
        box-sizing: border-box;
        outline: none;
        border-left: 0px;
        border-right: 0px;
    }
    ul {
        list-style: none;
        margin: 0;
        padding: 8px 0;
        overflow-y: auto;
    }
    li {
        list-style: none;
        margin: 0;
    }
    .item {
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 4px 6px;
        background: none;
        border: none;
        font: inherit;
        width: 100%;
        text-align: left;
        box-sizing: border-box;
    }
    .material-icons {
        font-size: 18px;
    }
    .item:hover {
        background-color: black;
        color: white;
    }
    .item.dir {
        font-weight: bold;
    }
    a.item {
        color: inherit;
        text-decoration: none;
    }
</style>
