<script lang="ts">
	import { onDestroy } from 'svelte';

	type ButtonProps = {
		id?: string;
		text?: string;
		onclick?: (event: MouseEvent) => void;
		loading?: boolean;
		disabled?: boolean;
		loadingFillChar?: string;
		loadingHeadChar?: string;
		loadingIdleFrames?: number;
		loadingFrameMs?: number;
	};

	let {
		id,
		text = 'CREATE',
		onclick,
		loading = false,
		disabled = false,
		loadingFillChar = '·',
		loadingHeadChar = '>',
		loadingIdleFrames = 4,
		loadingFrameMs = 120
	}: ButtonProps = $props();

	let frameIndex = $state(0);
	let animationId: number | null = null;

	let loadingFrames = $derived.by(() => {
		const label = text || '';
		const len = label.length;
		const empty = loadingFillChar.repeat(len);
		const frames: string[] = Array.from({ length: loadingIdleFrames }, () => empty);

		for (let i = 0; i <= len; i += 1) {
			const chars = Array.from({ length: len }, () => loadingFillChar);
			if (i < len) chars[i] = loadingHeadChar;
			frames.push(chars.join(''));
		}

		return frames;
	});

	let buttonText = $derived.by(() => {
		if (!loading) return text;
		return loadingFrames[frameIndex % loadingFrames.length] ?? text;
	});

	function stopAnimation() {
		if (animationId !== null) {
			window.clearInterval(animationId);
			animationId = null;
		}
	}

	$effect(() => {
		stopAnimation();

		if (!loading || loadingFrames.length === 0) {
			frameIndex = 0;
			return;
		}

		frameIndex = 0;
		animationId = window.setInterval(() => {
			frameIndex = (frameIndex + 1) % loadingFrames.length;
		}, loadingFrameMs);
	});

	onDestroy(() => {
		stopAnimation();
	});
</script>

<button {id} {onclick} disabled={disabled || loading}>
	{buttonText}
</button>

<style>
	button {
		margin-block-start: 1.33em;
		margin-block-end: 1.33em;
		border: 0;
		background-color: black;
		padding: 5px 16px;
		color: white;
		font-family: monospace;
		text-transform: uppercase;
		cursor: pointer;
		min-width: 88px;
	}

	button:disabled {
		opacity: 0.9;
		cursor: default;
	}
</style>
