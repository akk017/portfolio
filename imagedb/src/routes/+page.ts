// import type { PageLoad } from './$types';
// import { error } from '@sveltejs/kit';

// export const load: PageLoad = async ({ fetch }) => {
// 	try {
// 		const res = await fetch('http://127.0.0.1:8080/api/tags');
// 		let error = false
// 		if (!res.ok) {
// 			error = false;
// 		}
// 		const tags = await res.json();
// 		return {
// 			tags: tags,
// 			error: error
// 		}
// 	} catch (e) {
// 		console.error(e);
// 		// throw error(500, 'something went wrong while loading data');
// 	}
// };