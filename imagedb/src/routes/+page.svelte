<script lang="ts">


	interface Item {
		title: string;
		link: string;
		tags: string[];
		desc?: string;
		image: string;
		id: string;
		color: string;
	}

	let colors = [
		'skyblue',
		'plum',
		'aqua',
		'aquamarine',
		'coral',
		'gold',
		'lightblue',
		'lightgreen',
		'lightpink',
		'lightsalmon',
		'mediumspringgreen',
		'mediumturquoise',
		'mediumorchid',
		'palevioletred',
		'paleturquoise',
		'palegreen',
		'palegoldenrod',
		'tomato',
		'turquoise',
		'violet'
	];
	const getRandomColor = () => colors[Math.floor(Math.random() * colors.length)];
	let data: Item[] = [
		{
			id: 'val-1',
			title: 'APK Protocol',
			image: '/test1.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Fonts', 'Design'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-2',
			title: 'Gen Page',
			image: '/test2.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Marketing'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-3',
			title: 'TF.AR',
			image: '/test3.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand'],
			desc: 'Lorem Ipsum is simply dummy text of the'
		},
		{
			id: 'val-4',
			title: 'Khagwal',
			image: '/test4.jpg',
			link: 'https://khagwal.com/interactions/',
			tags: ['Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand', 'UX']
		},
		{
			id: 'val-5',
			title: 'React Query Builder',
			image: '/test5.jpg',
			link: 'https://react-querybuilder.js.org',
			tags: ['Design', 'Frontend', 'Dev', 'UI', 'UX', 'SQL', 'Query']
		},
		{
			id: 'val-6',
			title: 'APK Protocol',
			image: '/test1.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Fonts', 'Design'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-7',
			title: 'Gen Page',
			image: '/test2.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Marketing'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-8',
			title: 'TF.AR',
			image: '/test3.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand'],
			desc: 'Lorem Ipsum is simply dummy text of the'
		},
		{
			id: 'val-9',
			title: 'Khagwal',
			image: '/test4.jpg',
			link: 'https://khagwal.com/interactions/',
			tags: ['Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand', 'UX']
		},
		{
			id: 'val-10',
			title: 'React Query BuilderXXXXXXXXXXXXXXXXXXXXX',
			image: '/test5.jpg',
			link: 'https://react-querybuilder.js.org',
			tags: ['Design', 'Frontend', 'Dev', 'UI', 'UX', 'SQL', 'Query']
		},
		{
			id: 'val-11',
			title: 'APK Protocol',
			image: '/test1.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Fonts', 'Design'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-12',
			title: 'Gen Page',
			image: '/test2.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Marketing'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		},
		{
			id: 'val-13',
			title: 'TF.AR',
			image: '/test3.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Landing Page', 'Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand'],
			desc: 'Lorem Ipsum is simply dummy text of the'
		},
		{
			id: 'val-14',
			title: 'Khagwal',
			image: '/test4.jpg',
			link: 'https://khagwal.com/interactions/',
			tags: ['Inspiration', 'Design', 'App Development', 'Porfolio', 'Brand', 'UX']
		},
		{
			id: 'val-15',
			title: 'React Query Builder',
			image: '/test5.jpg',
			link: 'https://react-querybuilder.js.org',
			tags: ['Design', 'Frontend', 'Dev', 'UI', 'UX', 'SQL', 'Query']
		},
		{
			id: 'val-16',
			title: 'APK Protocol',
			image: '/test1.png',
			link: 'https://apk-type.com/family/apk-protocol',
			tags: ['Fonts', 'Design'],
			desc: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived"
		}
	].map((item) => ({
		...item,
		color: getRandomColor()
	}));

	// columns
	let v1: Item[] = [];
	let v2: Item[] = [];
	let v3: Item[] = [];
	let v4: Item[] = [];

	v1 = data.filter((_, i) => i % 4 === 0);
	v2 = data.filter((_, i) => i % 4 === 1);
	v3 = data.filter((_, i) => i % 4 === 2);
	v4 = data.filter((_, i) => i % 4 === 3);

	let shortcutCount = 0;
</script>

{#snippet item(col: Item[])}
	{#each col as data, i (data.id)}
		<div class="item" class:last={i === col.length - 1}>
			<img src={data.image} alt="test" />
			<div class="main-header">
				<div class="title">
					<span class="label">title</span>
					<h3>{data.title}</h3>
				</div>
				<div class="source">
					<span class="label">source</span>
					<a href={data.link}>LINK</a>
				</div>
			</div>
			<div class="main-tags">
				<span class="label">tags</span>
				<div class="tags" style:margin-bottom={data.desc ? '14px' : '0px'}>
					{#each data.tags as tag}
						<p class="tag" style="--color: {getRandomColor()}">{tag}</p>
					{/each}
				</div>
			</div>
			{#if data.desc}
				<div class="main-desc">
					<span class="label">note</span>
					<p>{data.desc}</p>
				</div>
			{/if}
		</div>
	{/each}
{/snippet}

<main>
	<div class="col">
		{@render item(v1)}
	</div>
	<div class="col">
		{@render item(v2)}
	</div>
	<div class="col">
		{@render item(v3)}
	</div>
	<div class="col">
		{@render item(v4)}
	</div>
</main>

<style>
	:root {
		--grid-cols: 4;
		--border-color: black;
		--border-width: 0.5px;

		--img-padding: 20px;
		--text-padding: 20px;

		--font-family: monospace;
	}

	main {
		display: flex;
		position: relative;
		/* grid-template-columns: repeat(var(--grid-cols), 1fr);
		grid-template-rows: auto;
		align-items: start; */
	}

	.shortcut-indicator {
		position: fixed;
		top: 12px;
		right: 12px;
		z-index: 50;
		padding: 8px 10px;
		font-family: var(--font-family);
		font-size: 12px;
		border: 1px solid black;
		background: white;
	}

	/* main:hover .item {
		opacity: 0;
	} */

	.col {
		width: 25%;
	}

	.main-header,
	.main-tags,
	.main-desc {
		display: flex;
		width: 100%;
		box-sizing: border-box;
		padding-left: var(--text-padding);
		padding-right: var(--text-padding);
	}

	.main-header {
		gap: var(--text-padding);
	}

	.main-header > .title {
		width: 100%;
		min-width: 50%;
	}

	.main-header > .title h3 {
		margin-bottom: 14px;

		min-width: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.main-header > .source {
		width: 50%;
		box-sizing: border-box;
		display: flex;
		flex-direction: column;

		min-width: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.main-header > .source a {
		margin-top: 4px;
		cursor: pointer;
	}

	.main-tags {
		display: flex;
		flex-direction: column;
	}

	.item {
		box-sizing: border-box;
		width: 100%;
		border: var(--border-width) solid var(--border-color);
		border-color: light-dark(black, rgb(140, 140, 140));
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: start;
		padding-bottom: var(--text-padding);
	}

	.item > img {
		padding: var(--img-padding);
		width: 100%;
		box-sizing: border-box;
	}

	.label {
		font-family: var(--font-family);
		text-transform: uppercase;

		font-size: 10px;
	}

	.main-header h3 {
		margin-top: 4px;
	}

	div.tags {
		width: calc(100% - 2 * var(--img-padding));
		display: flex;
		flex-wrap: wrap;
		gap: 4px;
		margin-top: 4px;
		margin-bottom: 14px;
	}

	.tag {
		color: white;
		background-color: var(--color, black);
		color: light-dark(
			color-mix(in srgb, var(--color, black), var(--fore-color, black) 85%),
			color-mix(in srgb, var(--color, black), var(--fore-color, black) 90%)
		);
		border-width: 1px;
		border-style: solid;
		border-color: light-dark(
			color-mix(in srgb, var(--color, black), var(--fore-color, black) 15%),
			color-mix(in srgb, var(--color, black), var(--fore-color, black) 90%)
		);

		display: inline-flex;
		justify-content: space-between;
		align-items: center;
		padding: 3px 6px;

		white-space: nowrap;
		width: max-content;
		margin: 0;
	}

	.main-desc {
		display: flex;
		flex-direction: column;
	}

	.main-desc > p {
		margin-top: 4px;
		margin-bottom: 0px;
	}

	.last {
		border-bottom: 1px solid;
		border-color: light-dark(black, rgb(140, 140, 140));
	}
</style>
