import { createOperation, deleteOperation, readAllOperation } from '../operation';

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

export type TagRow = {
	id: string;
	name: string;
	color: string;
};

function getRandomColor() {
	return TAG_COLORS[Math.floor(Math.random() * TAG_COLORS.length)];
}

export async function createTag(tag_name: string) {
	return await createOperation(TAGS_COLLECTION, {
		name: tag_name,
		color: getRandomColor()
	});
}

export async function readAllTags() {
	const response = await readAllOperation({
		collection: TAGS_COLLECTION
	});

	const rows = Array.isArray(response.documents) ? response.documents : [];

	return rows.map((doc) => ({
		id: doc.id as string,
		name: doc.name as string,
		color: (doc.color as string) || 'grey'
	}));
}

export async function deleteTag(tagId: string) {
	return await deleteOperation(TAGS_COLLECTION, tagId);
}