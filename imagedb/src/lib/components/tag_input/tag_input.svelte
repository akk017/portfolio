<script lang="ts">
	import Fuse from 'fuse.js';

	let ref: HTMLInputElement;
	let popover: HTMLDivElement;

	let prefix = 'create tag: ';

	let comp_id = $props.id();

	let { label } = $props();
	const init_tags = ['dev', 'animation', 'hello'];

	let plain_opts = $state(init_tags);

	let value = $state<string | undefined>();
	let options = $derived.by<string[]>(() => {
		const fuse = new Fuse(plain_opts, {
			includeScore: true,
			threshold: 0.4
		});
		if (value && value.length > 0) {
			const result = fuse.search(value).map((r) => r.item);
			const create = `${prefix}${value}`;
			if (!plain_opts.includes(value)) {
				return [...result, create];
			}
			return result;
		}
		return plain_opts;
	});

	let current = $state<number>(0);
	let selected = $state<string[]>([]);
	let creating_tag = $state<boolean>(false);

	$inspect(creating_tag, options);

	$effect(() => {
		options;
		if (current >= options.length) {
			current = options.length - 1;
		}
	});

	const create_tag = async (tag: string) => {
		const response = await fetch('http://localhost:8080/api/tags', {
			method: 'POST',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({
				tag: tag
			})
		});
		const val = await response.json();
		return val;
	};

	const onfocusin = () => {
		popover.showPopover();
	};
	const onfocusout = (e: FocusEvent) => {
		const to = e.relatedTarget as HTMLElement | null;
		if (!popover.contains(to) && to !== ref) {
			popover.hidePopover();
		}
	};
	const onkeydown = async (e: KeyboardEvent) => {
		if (['ArrowDown', 'ArrowUp', 'Enter', 'Escape'].includes(e.key)) {
			e.preventDefault();
		} else {
			current = 0;
		}
		const isOpen = popover.matches(':popover-open');
		if (!isOpen) {
			popover.showPopover();
		}

		if (e.key === 'ArrowDown') {
			current = (current + 1) % options.length;
		} else if (e.key == 'ArrowUp') {
			current = (current - 1 + options.length) % options.length;
		} else if (e.key == 'Enter') {
			const opt = options[current];
			if (opt.startsWith(prefix)) {
				const tag = opt.slice(prefix.length);
				creating_tag = true;
				plain_opts = await create_tag(tag);
				creating_tag = false;
			}
			selected.push(options[current]);
			value = '';
			current = 0;
		} else if (e.key == 'Escape') {
			popover.hidePopover();
		} else if (e.key === 'Backspace' && (!value || value.length === 0) && selected.length > 0) {
			selected = selected.slice(0, -1);
		}
	};

	const remove_tag = (index: number) => {
		if (index >= 0 && index < selected.length) {
			selected = selected.filter((_, i) => i !== index);
		}
	};

	const current_tag_onclick = async (index: number) => {
		const opt = options[index];
		if (opt.startsWith(prefix)) {
			const tag = opt.slice(prefix.length);
			creating_tag = true;
			plain_opts = await create_tag(tag);
			creating_tag = false;
		}
		selected.push(options[index]);
		value = '';
		ref.focus();
		popover.hidePopover();
		popover.showPopover();
	};
</script>

<main style="--tag-input: --{comp_id}">
	<label for={comp_id}>{label}</label>

	<div class="tag-input">
		<div class="tags">
			{#each selected as item, k ('tags-' + k)}
				<div class="tag">
					<span>{item}</span><button class="tag-delete" onclick={() => remove_tag(k)}>-</button>
				</div>
			{/each}
		</div>

		<input
			bind:this={ref}
			bind:value
			type="text"
			role="combobox"
			aria-expanded={popover?.matches(':popover-open')}
			aria-activedescendant={`option-${current}`}
			aria-controls="content"
			onclick={() => popover.showPopover()}
			{onfocusin}
			{onfocusout}
			{onkeydown}
			id={comp_id}
			autocomplete={null}
		/>
	</div>

	<div popover="manual" id="content-{comp_id}" class="content" bind:this={popover}>
		{#if creating_tag}
			<button class="item selected">creating...</button>
		{:else}
			{#each options as item, k ('options-' + k)}
				<button
					id="option-{k}"
					role="option"
					aria-selected={k === current}
					class="item"
					class:selected={k === current}
					onmouseenter={(e) => (current = k)}
					onclick={() => current_tag_onclick(k)}
				>
					{#if k === current}&gt;{/if}
					{item}
				</button>
			{/each}
		{/if}
	</div>
</main>

<style>
	main {
		font-family: monospace;
	}

	div.tag-input {
		border: 1px solid;
		margin-top: 5px;
		padding: 5px;
		padding-left: 12px;
		width: calc(100% - 12px - 5px - 2px);
	}

	input {
		anchor-name: var(--tag-input);
		outline: none;
		border: none;
		font-family: monospace;
		width: calc(100% - 12px - 5px);
	}

	div.content {
		margin: 0;
		padding: 0;
		z-index: 100;

		border: 1px solid;
		position: absolute;
		position-anchor: var(--tag-input);

		top: anchor(bottom);
		left: anchor(left);
		width: 200px;
		height: 200px;
		overflow-y: scroll;
		scrollbar-width: none;
	}

	button {
		text-align: start;
		border: 0px;
		font-family: monospace;
	}

	button.item {
		width: 100%;
		background-color: transparent;
	}
	/* button.item:hover {
		cursor: poniter;
		background-color: black;
		color: white;
	} */
	button.selected {
		background-color: black;
		color: white;
	}
	button.selected:hover {
		cursor: pointer;
	}

	div.tags {
		width: 100%;
		display: flex;
		flex-wrap: wrap;
		gap: 4px;
		margin-bottom: 4px;
	}

	.tag {
		color: white;
		background-color: black;
		display: inline-flex;
		justify-content: space-between;
		align-items: center;
		border: 1px solid black;
		padding: 0px;
		padding-left: 6px;

		white-space: nowrap;
		width: max-content;
	}

	.tag > span {
		margin-right: 4px;
	}

	.tag > .tag-delete {
		padding-right: 5px;
	}

	.tag-delete {
		color: white;
		background-color: black;
	}

	.tag-delete:hover {
		background-color: white;
		color: black;
	}

	h3 {
		font: monospace;
	}
</style>
