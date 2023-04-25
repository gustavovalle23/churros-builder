import * as dotenv from 'dotenv';
import { createPromptModule } from 'inquirer';
import { Answers } from './src/types';
import { createDefaultFiles } from './src/defaultFiles';
import { defaultAnswers, questions } from './src/constants';
import { createSonarProjectProperties } from './src/sonarProperties';
import { createProjectDirectory } from './src/directory';
import { createEntrypoint } from './src/entrypoint';

dotenv.config();

const build = async (answers: Answers) => {
  const dirName = await createProjectDirectory(answers.projectName);

  await Promise.all([
    createDefaultFiles(dirName),
    createEntrypoint(dirName, answers),
    createSonarProjectProperties(dirName, answers.projectName),
  ])
}

if (process.env.DEFAULT_PARAMS) {
  build(defaultAnswers)
} else {
  const prompt = createPromptModule();

  prompt<Answers>(questions)
    .then(async (answers: Answers) => {
      await build(answers)
    })
    .catch((error: Error) => {
      console.error(error);
    });
}
