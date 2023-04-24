import { createPromptModule } from 'inquirer';
import { Answers } from './src/types';
import { createDefaultFiles } from './src/defaultFiles';
import { questions } from './src/constants';
import { createSonarProjectProperties } from './src/sonarProperties';
import { createProjectDirectory } from './src/directory';
import { createEntrypoint } from 'src/entrypoint';

const prompt = createPromptModule();

prompt<Answers>(questions)
  .then(async (answers: Answers) => {
    const dirName = await createProjectDirectory(answers.projectName);

    await createDefaultFiles(dirName);
    await createSonarProjectProperties(dirName, answers.projectName);
    await createEntrypoint(answers, dirName);

  })
  .catch((error: Error) => {
    console.error(error);
  });
