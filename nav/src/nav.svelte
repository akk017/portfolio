<script lang="ts">
    import Fuse from "fuse.js";
    import { navData, type NavItem, type Page } from "./data.js";
    import { buildTree, type PathNode } from "./path-node.js";

    let query = $state("");
    let current = $state<PathNode[]>([]);

    const tree = buildTree(navData);

    const fuse = new Fuse(getAllPages(), { keys: ["title"], threshold: 0.4 });

    function getAllPages(): Page[] {
        const pages: Page[] = [];
        function walk(nodes: PathNode[]) {
            for (const n of nodes) {
                if (n.isFile)
                    pages.push({
                        type: "Page" as const,
                        title: n.name,
                        href: n.path,
                        folder: false,
                        icon: n.meta.icon || "",
                    });
                if (n.isDir && n.children.length) walk(n.children);
            }
        }
        walk([tree]);
        return pages;
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
        {#if current.length}<button onclick={back}
                ><span class="material-icons">arrow_back</span></button
            >{/if}

        <input type="text" bind:value={query} placeholder="search" />
    </div>
    {#if breadcrumbs().length > 0}
        <span class="path">
            {#each breadcrumbs().slice(-2) as c, i}
                <button class="crumb" onclick={() => navigate(c.idx)}
                    >{c.name}</button
                >
                {#if i < 1}/{/if}
            {/each}
        </span>
    {/if}

    {#if query}
        <ul>
            {#each results() as p}<li><a href={p.href}>{p.title}</a></li>{/each}
        </ul>
    {:else}
        <ul>
            {#each currentItems() as n}
                <li
                    class:dir={n.isDir}
                    onclick={() => (n.isDir ? enter(n) : goto(n))}
                >
                    <span class="material-icons"
                        >{n.isDir ? "folder" : "description"}</span
                    >
                    {n.name}
                </li>
            {/each}
        </ul>
    {/if}
</div>

<style>
    #nav-container {
        font: 13px monospace;
        display: flex;
        justify-content: flex-end;
        flex-direction: column;
        height: 100%;
    }
    .path {
        padding: 8px 12px;
        background: #f5f5f5;
        display: flex;
        gap: 4px;
        align-items: center;
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
    }
    ul {
        list-style: none;
        margin: 0;
        padding: 8px 0;
        overflow-y: auto;
    }
    li {
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 4px 6px;
    }
    .material-icons {
        font-size: 18px;
    }
    li:hover {
        background: #f0f0f0;
    }
    li.dir {
        font-weight: bold;
    }
    a {
        color: inherit;
        text-decoration: none;
    }
</style>
