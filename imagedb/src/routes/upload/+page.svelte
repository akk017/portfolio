<script lang="ts">
	import TagInput from '$lib/components/tag_input/tag_input.svelte';
	import TextInput from '$lib/components/text_input/text_input.svelte';
	import TextArea from '@/components/text_area/text_area.svelte';
	let { data } = $props();

	let name = $state();
	let url = $state();
	let source = $state();
	let desc = $state();

	let fileInput: HTMLInputElement;
	let previewUrl = $state<string | null>(null);

	const handleFileChange = (e: Event) => {
		const target = e.target as HTMLInputElement;
		const file = target.files?.[0];
		if (file && file.type.startsWith('image/')) {
			previewUrl = URL.createObjectURL(file);
		}
	};

	const handleClick = () => {
		fileInput.click();
	};

	const handleDrop = (e: DragEvent) => {
		e.preventDefault();
		const file = e.dataTransfer?.files?.[0];
		if (file && file.type.startsWith('image/')) {
			previewUrl = URL.createObjectURL(file);
		}
	};

	const handleDragOver = (e: DragEvent) => {
		e.preventDefault();
	};

	const handleRemove = () => {
		if (previewUrl) {
			URL.revokeObjectURL(previewUrl);
		}
		previewUrl = null;
		fileInput.value = '';
	};

	const handleSave = () => {
		console.log(name, url, source, desc)
	}
</script>

<main>
	<h3>ImageDb - Upload Image</h3>
	<div class="division">
		<section class="input">
			<TextInput label="Name" bind:value={name}/>
			<TagInput label="Tags"/>
			<TextInput label="Url" bind:value={url}/>
			<TextInput label="Source" bind:value={source}/>
			<TextArea label="Desc" bind:value={desc}/>
			<div class="action">
				<button class="save" onclick={() => handleSave()}>save</button>
				<button class="clear">clear</button>
			</div>
		</section>
		<section class="file-input">
			<label for="file-upload-input">Upload Image</label>
			<input
				type="file"
				accept="image/*"
				bind:this={fileInput}
				onchange={handleFileChange}
				id="file-upload-input"
				hidden
			/>
			<button
				class="upload-image"
				onclick={handleClick}
				ondrop={handleDrop}
				ondragover={handleDragOver}
			>
				{#if previewUrl}
					<img src={previewUrl} alt="Preview" />
				{:else}
					<span>Click or drag image here</span>
				{/if}
			</button>
			{#if previewUrl}
				<button class="remove-image" onclick={handleRemove}>Remove</button>
			{/if}
		</section>
	</div>
</main>

<style>
	main {
		padding-left: 100px;
		padding-top: 20px;
		padding-right: 100px;
		height: 100%;
	}
	div.division {
		display: flex;
		gap: 20px;
	}
	section.input {
		display: flex;
		flex-direction: column;
		gap: 20px;
		width: 30%;
	}

	section.file-input {
		width: 70%;
		height: 100%;
	}

	button.upload-image {
		width: 100%;
		min-height: 200px;
		border: 1px solid black;
		margin-top: 5px;
		background: transparent;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
		padding: 0;
		font-family: monospace;
	}

	button.upload-image:hover {
		border-style: dashed;
	}

	button.upload-image img {
		width: 100%;
		object-fit: cover;
	}

	button.remove-image,
	button.save,
	button.clear {
		border: 1px solid black;
		background-color: transparent;
		color: black;
		outline: none;
		margin-top: 15px;
		padding: 4px 10px;
		font-family: monospace;
		text-transform: uppercase;
		cursor: pointer;
	}

	button.remove-image:hover,
	button.save:hover,
	button.clear:hover {
		background-color: black;
		color: white;
	}

	button.remove-image:active,
	button:active,
	button.clear:active {
		background-color: white;
		color: black;
	}

	div.action {
		display: flex;
	}

	button.save {
		width: 20%;
		margin-top: 0;
	}

	button.clear {
		padding: 4px 16px;
		border-left: 0;
		margin-top: 0;
	}
</style>
