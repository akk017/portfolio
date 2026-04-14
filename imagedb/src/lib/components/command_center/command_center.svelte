<script lang="ts">
	import { onDestroy, onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { createShortcutMapper } from '$lib/shortcut';
	import Fuse from 'fuse.js';

	interface Option {
		id: string;
		title: string;
		href: string;
	}

	let options: Option[] = [
		{
			id: 'command-center-option-home',
			title: 'Home',
			href: '/'
		},
		{
			id: 'command-center-option-tags',
			title: 'Tags',
			href: '/tags'
		},
		{
			id: 'command-center-option-upload',
			title: 'Upload',
			href: '/upload'
		},
		{
			id: 'command-center-option-tracker',
			title: 'Tracker', // Track Habbits
			href: '/#todo'
		},
		{
			id: 'command-center-option-saved-view',
			title: 'Saved View',
			href: '/#todo'
		}
	];

	let dark = $state(false);
	let value = $state<string | undefined>();
	let current = $state(0);
	let fuse = $derived(
		new Fuse(options, {
			includeScore: true,
			threshold: 0.4,
			keys: ['id', 'title', 'href']
		})
	);
	let selectableOpts = $derived.by<Option[]>(() => {
		const query = value?.trim() ?? '';
		if (query.length > 0) {
			const result = fuse.search(query).map((r) => r.item);
			return result;
		}
		return options;
	});

	$effect(() => {
		if (selectableOpts.length === 0) {
			current = 0;
			return;
		}

		if (current >= selectableOpts.length) {
			current = 0;
		}
	});

	let popover: HTMLDivElement;
	let input: HTMLInputElement;

	let isPopoverOpen = $state(false);

	$effect(() => {
		document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
	});

	function onCommandPaletteShortcut() {
		popover.togglePopover();
	}

	let stopListening: (() => void) | null = null;
	let destroyShortcutMapper: (() => void) | null = null;

	onMount(() => {
		const mapper = createShortcutMapper();
		stopListening = mapper.register('cmd+shift+p', onCommandPaletteShortcut);
		destroyShortcutMapper = mapper.destroy;
	});

	const handleToggle = (e: ToggleEvent) => {
		if (e.newState === 'open') {
			input.focus();
		}
		isPopoverOpen = e.newState === 'open';
	};

	onDestroy(() => {
		stopListening?.();
		destroyShortcutMapper?.();
	});

	const onkeydown = (e: KeyboardEvent) => {
		if (e.key === 'ArrowDown') {
			current = (current + 1) % selectableOpts.length;
		} else if (e.key == 'ArrowUp') {
			current = (current - 1 + selectableOpts.length) % selectableOpts.length;
		} else if (e.key == 'Enter') {
			e.preventDefault();
			const opt = selectableOpts[current];
			if (!opt) return;

			popover.hidePopover();
			goto(opt.href);
		}
	};
</script>

<div popover bind:this={popover} id="command-center" ontoggle={handleToggle}>
	<input
		bind:this={input}
		bind:value
		id="command-center-search-input"
		type="s"
		autocomplete="off"
		autocorrect="off"
		autocapitalize="off"
		spellcheck={false}
		aria-autocomplete="none"
		role="combobox"
		aria-expanded={isPopoverOpen}
		aria-controls="command-list"
		placeholder="Command Center"
		{onkeydown}
	/>
	<div id="command-center-main">
		<div id="command-center-options">
			{#each selectableOpts as option, k}
				<span class="command-center-option" class:selected={k === current}
					>{#if k === current}&gt;{/if}
					{option.title}</span
				>
			{/each}
		</div>
		<div id="command-center-preview"></div>
	</div>
</div>

<style>
	div#command-center {
		width: 50%;
		height: 50%;
		padding: 8px 16px;
	}
	div#command-center::backdrop {
		backdrop-filter: blur(10px);
		background: rgba(0, 0, 0, 0.1);
	}
	div#command-center-main {
		display: flex;
		flex-grow: 1;
		box-sizing: border-box;
	}
	div#command-center-options {
		display: flex;
		flex-direction: column;
		width: 50%;
	}
	input#command-center-search-input {
		border: none;
		width: 100%;
		outline: none;
		padding: 0px;
		font-family: monospace;
		height: 30px;
		margin-bottom: 8px;
	}

	span.command-center-option {
		padding: 5px 0px;
	}

	span.selected {
		background-color: black;
		color: white;
		padding: 5px 12px;
	}
</style>
