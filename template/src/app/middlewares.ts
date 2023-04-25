import { createUserRouter } from '@/infra/routers';

export const setupRouters = (app: any, di: any) => {
    const userRouter = createUserRouter({
      createUserUseCase: di.createUserUseCase, loginUseCase: di.loginUseCase
    })
    app.use(userRouter.routes());
    app.use(userRouter.allowedMethods());
  }
