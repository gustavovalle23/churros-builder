interface UserController {
  createUser: (ctx: any) => Promise<void>;
  login: (ctx: any) => Promise<void>;
}

type Input = { createUserUseCase: any, loginUseCase: any }

export const userController = ({ createUserUseCase, loginUseCase }: Input): UserController => {
  const createUser = async (ctx: any) => {
    const { name, email, password, birthDate, address } = ctx.request.body;

    const user = await createUserUseCase.execute({ name, email, password, birthDate, address });

    ctx.body = user;
  };


  const login = async (ctx: any) => {
    const { email, password } = ctx.request.body;

    const { token, refreshToken } = await loginUseCase.execute({ email, password });

    ctx.body = {
      token,
      refreshToken,
    };
  };

  return {
    login,
    createUser,
  };
};
