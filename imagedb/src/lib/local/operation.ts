const MONGO_API_BASE_URL = 'http://localhost:9003/api/v1/mongo';

type ReadAllRequest = {
	collection: string;
	filter?: Record<string, unknown>;
	limit?: number;
	skip?: number;
};

async function operationRequest<T = unknown>(path: string, payload?: unknown): Promise<T> {
	const response = await fetch(`${MONGO_API_BASE_URL}${path}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: payload ? JSON.stringify(payload) : undefined
	});

	if (!response.ok) {
		const text = await response.text();
		throw new Error(text || `Operation failed with status ${response.status}`);
	}

	return (await response.json()) as T;
}

export function createOperation(collection: string, document: unknown) {
	return operationRequest<{ id: string }>('/create', {
		collection,
		document
	});
}

export function readOperation(collection: string, id: string) {
	return operationRequest<{ status: string; id: string; document: Record<string, unknown> }>(
		'/read',
		{
			collection,
			id
		}
	);

}

export function readAllOperation(payload: ReadAllRequest) {
	return operationRequest<{ status: string; documents: Record<string, unknown>[]; count: number }>(
		'/read_all',
		payload
	);
}

export function updateOperation(
	collection: string,
	id: string,
	update: Record<string, unknown>
) {
	return operationRequest<boolean>('/update', {
		collection,
		id,
		update
	});
}

export function deleteOperation(collection: string, id: string) {
	return operationRequest<boolean>('/delete', {
		collection,
		id
	});
}

export function bulkInsertOperation(collection: string, documents: Record<string, unknown>[]) {
	return operationRequest<{ ids: string[]; count: number }>('/bulk-insert', {
		collection,
		documents
	});
}
