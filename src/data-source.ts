import { DataSource } from "typeorm";
import { User } from "./entities/User";

export const AppDataSource = new DataSource({
  type: "sqlite",
  database: "database.sqlite", // 로컬 파일 DB
  synchronize: true, // 중요: 모델 변경 시 DB 스키마 자동 업데이트
  logging: false,
  entities: [User],
  subscribers: [],
  migrations: [],
});
