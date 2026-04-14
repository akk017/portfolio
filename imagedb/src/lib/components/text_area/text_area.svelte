<script lang="ts">
	let { label, min_len = 0, max_len = 1000, value = $bindable() } = $props();

	let comp_id = $props.id();
</script>

<main>
	<label for={comp_id}>{label}</label>
	<textarea id={comp_id} minlength={min_len} maxlength={max_len} bind:value></textarea>
</main>


<style>
    main {
        display: flex;
        flex-direction: column;
        
        font-family: monospace;
    }
    
   	textarea {
		outline: none;
        height: 80px;
		border: 1px solid;
		font-family: monospace;
		width: calc(100% - 12px - 5px - 2px);
		margin-top: 5px;
		padding: 5px;
		padding-left: 12px;
        resize: vertical;
	}
</style>