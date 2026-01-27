import {
  Body,
  Controller,
  Get,
  Post,
  Route,
  Security,
  SuccessResponse,
  Tags,
} from "tsoa";
import { User } from "../entities/User";
import { AppDataSource } from "../data-source";
import * as jwt from "jsonwebtoken";

// 요청 바디용 DTO 정의
interface UserCreationParams {
  email: string;
  password: string;
}

@Route("users")
@Tags("User")
export class UsersController extends Controller {
  private userRepository = AppDataSource.getRepository(User);

  /**
   * 모든 사용자를 조회합니다. (인증 필요 없음 예시)
   */
  @Get()
  public async getUsers(): Promise<User[]> {
    return this.userRepository.find();
  }

  /**
   * 새 사용자를 생성합니다.
   */
  @SuccessResponse("201", "Created")
  @Post()
  public async createUser(
    @Body() requestBody: UserCreationParams,
  ): Promise<User> {
    const user = new User();
    user.email = requestBody.email;
    user.password = requestBody.password;

    return this.userRepository.save(user);
  }

  /**
   * 로그인을 통해 JWT 토큰을 발급받습니다.
   */
  @Post("login")
  public async login(
    @Body() requestBody: UserCreationParams,
  ): Promise<{ token: string }> {
    const user = await this.userRepository.findOneBy({
      email: requestBody.email,
      password: requestBody.password,
    });
    if (!user) throw new Error("Invalid credentials");

    const token = jwt.sign(
      { id: user.id, email: user.email },
      "YOUR_SECRET_KEY",
      { expiresIn: "1h" },
    );
    return { token };
  }

  /**
   * 인증된 사용자만 접근 가능한 엔드포인트입니다.
   */
  @Security("jwt") // tsoa.json에 정의된 인증 모듈 사용
  @Get("me")
  public async getMyProfile(): Promise<string> {
    return "This is a protected resource based on JWT";
  }
}
