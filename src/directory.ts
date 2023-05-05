import { mkdir } from 'fs';
import { promisify } from 'util';

const mkdirAsync = promisify(mkdir);

export async function createProjectDirectory(dirName: string): Promise<void> {
  try {
    await mkdirAsync(dirName);
    console.log(`Directory ${dirName} created successfully!`);
  } catch (err) {
    if (err.code !== 'EEXIST') {
      console.error(`Error creating directory ${dirName}: ${err}`);
      throw err;
    }
    console.log(`Directory ${dirName} already exists.`);
  }
}
