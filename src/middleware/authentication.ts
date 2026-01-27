import * as express from "express";
import * as jwt from "jsonwebtoken";

export function expressAuthentication(
  request: express.Request,
  securityName: string,
  scopes?: string[],
): Promise<any> {
  if (securityName === "jwt") {
    const token = request.headers["authorization"];

    return new Promise((resolve, reject) => {
      if (!token) {
        reject(new Error("No token provided"));
      }
      // Bearer 제거 및 검증
      jwt.verify(
        token!.replace("Bearer ", ""),
        "YOUR_SECRET_KEY",
        function (err: any, decoded: any) {
          if (err) {
            reject(err);
          } else {
            // 스코프(권한) 체크 로직을 여기에 추가 가능
            resolve(decoded);
          }
        },
      );
    });
  }
  return Promise.reject({});
}
