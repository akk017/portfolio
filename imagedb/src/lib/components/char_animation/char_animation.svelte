<script lang="ts">
	import { onDestroy, onMount } from 'svelte';

	type CharAnimationProps = {
		loading?: boolean;
		fillChar?: string;
		headChar?: string;
		frameMs?: number;
		class?: string;
	};

	let {
		loading = true,
		fillChar = '·',
		headChar = '>',
		frameMs = 120,
		class: className
	}: CharAnimationProps = $props();

	let rootEl: HTMLDivElement;
	let frameIndex = $state(0);
	let charCount = $state(0);
	let animationId: number | null = null;
	let resizeObserver: ResizeObserver | null = null;

	function stopAnimation() {
		if (animationId !== null) {
			window.clearInterval(animationId);
			animationId = null;
		}
	}

	function measureCharCount() {
		if (!rootEl) return;

		const width = rootEl.clientWidth;
		if (width <= 0) {
			charCount = 0;
			return;
		}

		const probe = document.createElement('span');
		probe.style.position = 'absolute';
		probe.style.visibility = 'hidden';
		probe.style.pointerEvents = 'none';
		probe.style.font = getComputedStyle(rootEl).font;
		probe.textContent = fillChar;
		document.body.appendChild(probe);

		const charWidth = probe.getBoundingClientRect().width || 1;
		probe.remove();

		charCount = Math.max(1, Math.floor(width / charWidth));
	}

	let lineText = $derived.by(() => {
		const len = charCount;
		if (len <= 0) return '';

		const chars = Array.from({ length: len }, () => fillChar);
		if (loading) {
			const headIndex = frameIndex % len;
			chars[headIndex] = headChar;
		}

		return chars.join('');
	});

	$effect(() => {
		stopAnimation();

		if (!loading || charCount <= 0) {
			frameIndex = 0;
			return;
		}

		frameIndex = 0;
		animationId = window.setInterval(() => {
			frameIndex = (frameIndex + 1) % charCount;
		}, frameMs);
	});

	onMount(() => {
		measureCharCount();
		resizeObserver = new ResizeObserver(() => measureCharCount());
		resizeObserver.observe(rootEl);
	});

	onDestroy(() => {
		stopAnimation();
		resizeObserver?.disconnect();
	});
</script>

<div bind:this={rootEl} class={`char-animation ${className ?? ''}`}>{lineText}</div>

<style>
	div.char-animation {
		width: 100%;
		overflow: hidden;
		white-space: nowrap;
		font-family: monospace;
		line-height: 1;
		user-select: none;
	}
</style>
