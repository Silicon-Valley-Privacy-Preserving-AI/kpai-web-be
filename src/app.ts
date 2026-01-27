import express, { Response as ExResponse, Request as ExRequest } from "express";
import bodyParser from "body-parser";
import swaggerUi from "swagger-ui-express";
import { RegisterRoutes } from "./routes/routes"; // tsoa가 자동 생성할 파일

export const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// tsoa가 생성한 라우트 등록
RegisterRoutes(app);

// Swagger UI 설정
import * as swaggerDocument from "../build/swagger.json"; // tsoa가 자동 생성할 파일
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));
