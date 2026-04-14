import { ID, Query, type Models } from 'appwrite';
import { tablesDB } from '$lib/appwrite';
import { PUBLIC_APPWRITE_DATABASE_ID } from '$env/static/public';

export const DATABASE_ID = PUBLIC_APPWRITE_DATABASE_ID;

export const TAG_COLORS = [
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

export enum Tables {
	Tags = 'tags'
}

export type TagRow = Models.Row & {
	name: string;
	color: string;
};

function getRandomColor() {
	return TAG_COLORS[Math.floor(Math.random() * TAG_COLORS.length)];
}


export async function listTags(databaseId = DATABASE_ID) {
	const pageSize = 100;
	let offset = 0;
	const rows: TagRow[] = [];

	while (true) {
		const result = await tablesDB.listRows<TagRow>({
			databaseId,
			tableId: Tables.Tags,
			queries: [Query.limit(pageSize), Query.offset(offset)]
		});

		rows.push(...result.rows);

		if (result.rows.length < pageSize) {
			break;
		}

		offset += pageSize;
	}

	return rows;
}

export async function createTag(tag_name: string) {
	return await tablesDB.createRow({
		databaseId: DATABASE_ID,
		tableId: Tables.Tags,
		rowId: ID.unique(),
		data: {
			name: tag_name,
			color: getRandomColor()
		}
	});
}

export async function deleteTag(tagId: string) {
	return await tablesDB.deleteRow({
		databaseId: DATABASE_ID,
		tableId: Tables.Tags,
		rowId: tagId
	});
}
