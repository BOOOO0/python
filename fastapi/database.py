from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://boo:qndud12!@localhost:5432/fastapi"


engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)


# 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 생성
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# 데이터 삽입 함수
def create_user(db, name: str, age: int):
    new_user = User(name=name, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 데이터 쿼리 함수
def get_users(db):
    return db.query(User).all()


# 메인 실행 코드
if __name__ == "__main__":
    # 데이터베이스 세션 생성
    db = SessionLocal()

    # 사용자 데이터 삽입
    user = create_user(db, name="John Doe", age=30)
    print(f"Created User: {user.id}, {user.name}, {user.age}")

    # 모든 사용자 데이터 쿼리
    users = get_users(db)
    for user in users:
        print(f"User: {user.id}, {user.name}, {user.age}")

    # 세션 종료
    db.close()
