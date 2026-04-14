<script lang="ts">
	import Fuse from 'fuse.js';
	import { onMount } from 'svelte';
	import Button from '$lib/components/button/button.svelte';
	import CharAnimation from '@/components/char_animation/char_animation.svelte';
	import {
		createOperation,
		deleteOperation,
		readAllOperation
	} from '$lib/local/operation';

	type TagRow = {
		$id: string;
		name: string;
		color: string;
	};

	const TAGS_COLLECTION = 'tags';
	const TAG_COLORS = [
		'skyblue',
		'plum',
		'aqua',
		'aquamarine',
		'coral',
		'gold',
		'lightblue',
		'lightgreen',
		'lightpink',
		'lightsalmon'
	];

	let createValue = $state('');
	let creatingState = $state(false);
	let deletingState = $state(false);
	let createError = $state('');
	let tags = $state<TagRow[]>([]);
	let tagsLoading = $state(true);
	let searchValue = $state('');
	let tagSelected = $state(0);
	let filteredTags = $derived.by<TagRow[]>(() => {
		if (!searchValue.trim()) return tags;

		const fuse = new Fuse(tags, {
			keys: ['name'],
			includeScore: true,
			threshold: 0.4
		});

		return fuse.search(searchValue).map((result) => result.item);
	});

	$effect(() => {
		filteredTags;
		if (filteredTags.length === 0) {
			tagSelected = 0;
			return;
		}
		if (tagSelected >= filteredTags.length) {
			tagSelected = filteredTags.length - 1;
		}
	});

	const normalizeTag = (item: Record<string, unknown>, index: number): TagRow | null => {
		const nestedData = typeof item.DATA === 'object' && item.DATA !== null ? item.DATA : {};
		const source = nestedData as Record<string, unknown>;
		const rawMongoId = item._id;
		const mongoId =
			typeof rawMongoId === 'string'
				? rawMongoId
				: typeof rawMongoId === 'object' && rawMongoId !== null && '$oid' in rawMongoId
					? String((rawMongoId as { $oid?: unknown }).$oid ?? '')
					: '';

		const id =
			typeof item.$id === 'string'
				? item.$id
				: mongoId
					? mongoId
					: typeof item.id === 'string'
						? item.id
						: `tag-${index}`;
		const name =
			typeof item.name === 'string'
				? item.name
				: typeof source.name === 'string'
					? source.name
					: null;
		if (!name) return null;

		const color =
			typeof item.color === 'string'
				? item.color
				: typeof source.color === 'string'
					? source.color
					: 'grey';

		return { $id: id, name, color };
	};

	async function refreshTags() {
		tagsLoading = true;
		try {
			const response = await readAllOperation({
				collection: TAGS_COLLECTION
			});
			const rows = Array.isArray(response.documents) ? response.documents : [];

			tags = rows
				.map((item, index) =>
					normalizeTag((item ?? {}) as Record<string, unknown>, index)
				)
				.filter((item): item is TagRow => item !== null);
		} catch (error) {
			createError = error instanceof Error ? error.message : 'Failed to load tags';
		} finally {
			tagsLoading = false;
		}
	}

	onMount(async () => {
		await refreshTags();
	});

	async function handleCreateTag() {
		if (creatingState) return;

		const name = createValue.trim();
		if (!name) return;

		creatingState = true;

		try {
			await createOperation(TAGS_COLLECTION, {
				name,
				color: TAG_COLORS[Math.floor(Math.random() * TAG_COLORS.length)]
			});
			createValue = '';
			await refreshTags();
		} catch (error) {
			createError = error instanceof Error ? error.message : 'Failed to create tag';
		} finally {
			creatingState = false;
		}
	}

	const onkeydown = async (e: KeyboardEvent) => {
		if (['ArrowDown', 'ArrowUp', 'Enter', 'Escape'].includes(e.key)) {
			e.preventDefault();
		}

		if (e.key == 'Enter') {
			handleCreateTag();
		}
	};

	const handleSearchKeydown = (e: KeyboardEvent) => {
		if (filteredTags.length === 0) {
			return;
		}

		if (['ArrowDown', 'ArrowUp', 'Enter', 'Escape'].includes(e.key)) {
			e.preventDefault();
		}
		if (e.key === 'ArrowDown') {
			tagSelected = (tagSelected + 1) % filteredTags.length;
		} else if (e.key == 'ArrowUp') {
			tagSelected = (tagSelected - 1 + filteredTags.length) % filteredTags.length;
		}
		if (['ArrowDown', 'ArrowUp'].includes(e.key)) {
			const selected = document.getElementById(`tag-option-${tagSelected}`);
			selected?.scrollIntoView({ block: 'nearest' });
		}
	};

	const handleSearchInput = () => {
		tagSelected = 0;
	};

	const handleDeleteTag = async (tagId: string) => {
		if (deletingState) return;

		deletingState = true;
		createError = '';

		try {
			await deleteOperation(TAGS_COLLECTION, tagId);
			await refreshTags();
		} catch (error) {
			createError = error instanceof Error ? error.message : 'Failed to delete tag';
		} finally {
			deletingState = false;
		}
	};
</script>

<main>
	<h3>Tags</h3>

	<section id="tags-main">
		<section id="tags-create-tag">
			<h4 id="tags-create-tag-title">Create Tag</h4>
			<label for="tags-create-tag-input" id="tags-create-tag-label">Name</label>
			<input
				type="text"
				id="tags-create-tag-input"
				bind:value={createValue}
				autocomplete="off"
				{onkeydown}
			/>
			<Button
				id="tags-create-tag-btn"
				text="create"
				loading={creatingState || deletingState}
				onclick={handleCreateTag}
			/>
			{#if createError}
				<p id="tags-create-tag-error">{createError}</p>
			{/if}
		</section>
		<section>
			<h4 id="tags-list-title">List of Tags</h4>

			<div id="tags-list-wrap">
				{#if tagsLoading}
					<CharAnimation loading={tagsLoading} />
				{:else if tags.length === 0}
					<p id="tags-empty-state">No tags yet</p>
				{:else}
					<label for="tags-search-tag-input" id="tags-search-tag-label">Name</label>
					<input
						type="search"
						id="tags-search-tag-input"
						bind:value={searchValue}
						placeholder="Search.."
						role="combobox"
						aria-expanded={filteredTags.length > 0}
						aria-activedescendant={filteredTags.length > 0
							? `tag-option-${tagSelected}`
							: undefined}
						aria-controls="tags-list"
						autocomplete="off"
						onkeydown={handleSearchKeydown}
						oninput={handleSearchInput}
					/>
					<div id="tags-list" role="listbox">
						{#if filteredTags.length === 0}
							<p id="tags-empty-state">No matching tags</p>
						{:else}
							{#each filteredTags as tag, k (tag.$id)}
								<div
									class="tag-row"
									class:tag-selected={tagSelected == k}
									id={`tag-option-${k}`}
									role="option"
									tabindex="-1"
									aria-selected={tagSelected == k}
									onmouseenter={() => (tagSelected = k)}
								>
									<div>
										<span class="tag-dot" style:background-color={tag.color}></span>
										<span>{tag.name}</span>
										{#if k === tagSelected}&lt;{/if}
									</div>
									<button
										type="button"
										class="tag-delete"
										onclick={() => handleDeleteTag(tag.$id)}
										disabled={deletingState}
										aria-label={`Delete tag ${tag.name}`}
									>
										x
									</button>
								</div>
							{/each}
						{/if}
					</div>
				{/if}
			</div>
		</section>
		<section></section>
	</section>
</main>

<style>
	main {
		padding-left: 100px;
		padding-top: 20px;
		padding-right: 100px;
		height: 100%;
	}

	section#tags-main {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 30px;
	}
	section#tags-create-tag {
		display: flex;
		flex-direction: column;
		justify-content: start;
		align-items: start;
		width: 100%;
	}

	h4#tags-create-tag-title {
		width: 100%;
	}
	label#tags-create-tag-label, label#tags-search-tag-label {
		margin-block-end: 0.3em;
	}
	input#tags-create-tag-input {
		width: 100%;
		box-sizing: border-box;
		font-family: monospace;
		border: 1px solid grey;
		outline: none;
		border-radius: 0;
		padding: 5px 8px;
	}
	input#tags-create-tag-input:focus {
		border: 1px solid black;
	}

	p#tags-create-tag-error {
		margin: 0;
		font-size: 12px;
		color: #dc2626;
	}

	div#tags-list-wrap {
		display: flex;
		flex-direction: column;
		justify-content: start;
		align-self: start;
		max-height: 400px;
		overflow-y: auto;
	}

	div#tags-list {
		display: flex;
		flex-direction: column;
		gap: 8px;
		overflow-y: auto;
		max-height: 320px;
	}

	p#tags-empty-state {
		margin: 0;
		font-size: 13px;
		color: #666;
	}

	input#tags-search-tag-input {
		width: 100%;
		box-sizing: border-box;
		font-family: monospace;
		border: 1px solid grey;
		outline: none;
		border-radius: 0;
		padding: 5px 8px;
		margin-block-end: 1.33em;
	}
	input#tags-search-tag-input:focus {
		border: 1px solid black;
	}

	button.tag-delete {
		background-color: transparent;
		color: inherit;
		border: 1px solid currentColor;
		font-family: monospace;
		line-height: 1;
		padding: 0 4px;
		cursor: pointer;
	}

	div.tag-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 8px;
		font-family: monospace;
		font-size: 13px;
		padding: 5px 0px;
	}

	div.tag-selected {
		background-color: black;
		color: white;
		padding: 5px 8px;
		scroll-margin: 8px;
	}

	span.tag-dot {
		width: 10px;
		height: 10px;
		display: inline-block;
	}
</style>
