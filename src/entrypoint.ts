import { promisify } from 'util';
import { Answers } from './types';
import { writeFile } from 'fs';

export async function createEntrypoint(answers: Answers, dirName: string) {
  if (answers.useExpress) {
    const mainContent = `import express, { Request, Response } from 'express';
  
  const app = express();
  
  app.get('/', (req: Request, res: Response) => {
    res.send('Hello World from Express!');
  });
  
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(\`Server running on port \${PORT}\`);
  });
  `;

    await promisify(writeFile)(`${dirName}/index.ts`, mainContent);

    console.log(`main.ts file created with Express application at: ${dirName}/index.ts`);
  } else if (answers.useKoa) {
    const mainContent = `import Koa, { Context, Next } from 'koa';
  
  const app = new Koa();
  
  app.use(async (ctx: Context, next: Next) => {
    ctx.body = 'Hello World from Koa!';
    await next();
  });
  
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(\`Server running on port \${PORT}\`);
  });
  `;
    await promisify(writeFile)(`${dirName}/index.ts`, mainContent);
    console.log(`main.ts file created with Koa application at: ${dirName}/index.ts`);
  }
}
