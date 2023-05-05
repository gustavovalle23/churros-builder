import { promisify } from 'util';
import { writeFile } from 'fs';

export enum BackendFramework {
  EXPRESS = 'express',
  KOA = 'KOA'
}


export async function createEntrypoint(dirName: string, framework: BackendFramework) {
  if (framework === BackendFramework.EXPRESS) {
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
  } else if (framework === BackendFramework.KOA) {
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
