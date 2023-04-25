import Router from 'koa-router';
import { userController } from './controllers';

interface UseCases {
  createUserUseCase: () => void;
  loginUseCase: () => void;
}

export const createUserRouter = (useCases: UseCases) => {
  const router = new Router();

  const { createUser, login } = userController({ ...useCases });

  router.post('/users', createUser);
  router.post('/users/login', login);

  return router;
};
