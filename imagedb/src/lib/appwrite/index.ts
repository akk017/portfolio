import { Client, TablesDB } from 'appwrite';
import { PUBLIC_APPWRITE_ENDPOINT, PUBLIC_APPWRITE_PROJECT_ID } from '$env/static/public';

export const appwriteClient = new Client()
	.setEndpoint(PUBLIC_APPWRITE_ENDPOINT)
	.setProject(PUBLIC_APPWRITE_PROJECT_ID);

export const tablesDB = new TablesDB(appwriteClient);
