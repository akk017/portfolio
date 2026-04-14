<script lang="ts">
	import './layout.css';
	import CommandCenter from '@/components/command_center/command_center.svelte';
	import MainNav from '../lib/components/main_nav/main_nav.svelte';

	let { children } = $props();
</script>

<div class="app">
	<CommandCenter />
	<MainNav />
	<main>
		{@render children()}
	</main>
</div>

<style>
	main {
		padding-top: 50px;
	}
</style>
