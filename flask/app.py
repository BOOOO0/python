import os

from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
DATABASE_URL = os.getenv('FLASK_DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URL'] = DATABASE_URL

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 베이스 클래스 생성
Base = declarative_base()


# 테이블 모델 정의
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


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/item/<int:item>', methods=['GET'])
def get_items(item):
    return f'item: {item}'


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json().get('item')
    return f'item: {data}'


if __name__ == '__main__':
    app.run(debug=True)

    # db = SessionLocal()
    #
    # # 사용자 데이터 삽입
    # user = create_user(db, name="John Doe", age=30)
    # print(f"Created User: {user.id}, {user.name}, {user.age}")
    #
    # # 모든 사용자 데이터 쿼리
    # users = get_users(db)
    # for user in users:
    #     print(f"User: {user.id}, {user.name}, {user.age}")
