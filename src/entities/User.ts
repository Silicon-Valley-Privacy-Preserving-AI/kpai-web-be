import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id!: number;

  @Column()
  email!: string;

  @Column()
  password!: string; // 실제로는 해싱해서 저장해야 함

  @Column({ default: "user" })
  role!: string;
}
