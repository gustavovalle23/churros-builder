import { readFile, writeFile } from 'fs';
import { promisify } from 'util';

export async function createDefaultFiles(dirName: string): Promise<void> {
  const defaultFiles = [
    '.eslintignore',
    '.eslintrc.js',
    '.gitignore',
    '.npmrc',
    '.prettierignore',
    '.prettierrc',
    'commitlint.config.js',
    'tsconfig.build.json',
    'tsconfig.json',
    'package.json'
  ];

  await Promise.all(defaultFiles.map(async (file) => {
    const fileContent = await promisify(readFile)(`template/${file}`, 'utf-8')
    const filePath = `${dirName}/${file}`;

    const fileContentNormalized = fileContent.replace('churros-template', dirName)

    await promisify(writeFile)(filePath, fileContentNormalized);
    console.log(`${filePath} file created successfully!`);
  }));
}
