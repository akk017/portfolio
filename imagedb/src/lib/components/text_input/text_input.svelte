<script lang="ts">
	let { label, min_len = 0, max_len = 1000, value = $bindable() } = $props();

	let comp_id = $props.id();
</script>

<main>
	<label for={comp_id}>{label}</label>
	<input id={comp_id} type="text" minlength={min_len} maxlength={max_len} bind:value />
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		font-family: monospace;
	}

	input {
		outline: none;
		border: 1px solid;
		font-family: monospace;
		width: calc(100% - 12px - 5px - 2px);
		margin-top: 5px;
		padding: 5px;
		padding-left: 12px;
	}
</style>
