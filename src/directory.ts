import { mkdir } from 'fs';
import slugify from 'slugify';
import { promisify } from 'util';

const mkdirAsync = promisify(mkdir);

export async function createProjectDirectory(projectName: string): Promise<string> {
  const projectSlug = slugify(projectName, { lower: true });
  const dirName = `${projectSlug}`;

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

  return dirName;
}
