import * as dotenv from 'dotenv';
import { createPromptModule } from 'inquirer';
import slugify from 'slugify';
import select from '@inquirer/select';
import { Answers } from './src/types';
import { createDefaultFiles } from './src/defaultFiles';
import { defaultAnswers, questions } from './src/constants';
import { createSonarProjectProperties } from './src/sonarProperties';
import { createProjectDirectory } from './src/directory';
import { BackendFramework, createEntrypoint } from './src/entrypoint';

dotenv.config();

const build = async (answers: Answers, dirName: string) => {
  await createProjectDirectory(answers.projectName);

  await Promise.all([
    createDefaultFiles(dirName),
    createSonarProjectProperties(dirName, answers.projectName),
  ])
}

const ask = async () => {
  if (process.env.DEFAULT_PARAMS === 'true') {
    build(defaultAnswers, 'users');
  } else {
    const prompt = createPromptModule();
    const answers =  await prompt<Answers>(questions)
    const dirName = slugify(answers.projectName, { lower: true });

    const backendFramework = await select({
      message: 'Select a backend framework',
      choices: [
        {
          name: 'Express',
          value: 'express',
          description: 'Use ExpressJS',
        },
        {
          name: 'Koa',
          value: 'koa',
          description: 'Use KoaJS',
        },
      ],
    })

    await build(answers, dirName)
    await createEntrypoint(dirName, BackendFramework[backendFramework])

  }
}

(async () => {
  await ask();
})();
