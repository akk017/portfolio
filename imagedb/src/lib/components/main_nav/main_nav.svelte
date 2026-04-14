<script lang="ts">
	let dark = $state(false);
	let search: HTMLInputElement;

	$effect(() => {
		document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
	});

	const onkeydown = (e: KeyboardEvent) => {
		if (['ArrowDown', 'ArrowUp', 'Enter', 'Escape'].includes(e.key)) {
			e.preventDefault();
		}

		if (e.key === 'Escape') {
			search.blur()
		}
	};
</script>

<div class="nav">
	<div class="title">
		<h3>ImageDB</h3>
	</div>
	<div class="search">
		<input placeholder="Search" {onkeydown} bind:this={search}/>
	</div>
	<input type="checkbox" bind:checked={dark} />
</div>

<style>
	/* img {
		aspect-ratio: 16 / 9;
	} */

	.nav {
		width: 100%;
		border-bottom: 1px solid;

		border-color: light-dark(black, rgb(140, 140, 140));
		background-color: light-dark(white, black);

		position: fixed;
		height: 50px;
		display: flex;
		justify-content: start;
		align-items: center;

		z-index: 100;
	}
	.title {
		padding: 0 20px;
		border-right: 1px solid;
		border-color: light-dark(black, rgb(140, 140, 140));
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.search {
		width: 100%;
	}

	.search > input {
		box-sizing: border-box;
		border: none;
		outline: none;
		font-family: monospace;
		padding: 0 20px;
		width: 100%;
		background-color: transparent;
	}
</style>
