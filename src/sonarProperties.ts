import { readFile, writeFile } from 'fs';
import slugify from 'slugify';
import { promisify } from 'util';

export async function createSonarProjectProperties(dirName: string, projectName: string): Promise<void> {
  const projectSlug = slugify(projectName, { lower: true });
  const filePath = `${dirName}/sonar-project.properties`;

  const data = await promisify(readFile)('template/sonar-project.properties', 'utf-8');
  const fileContent = data.replace('churros-template-microservice', projectSlug);

  await promisify(writeFile)(filePath, fileContent);
  console.log(`${filePath} file created successfully!`);
}
