# ORM

- Django는 ORM이 내장된(?) 방식이지만 FASTAPI는 각 DB에 대응되는 ORM 라이브러리를 사용할 수 있다. MySQL이면 SQLAlchemy, MongoDB면 MongoEngine을 사용할 수 있다. 모든 DB에 해당되는 라이브러리가 있는 지는 모르겠다.

- pydantic에 대해서 간략하게 언급하면 pydantic은 ORM처럼 모델을 생성하는 것은 아니고 들어오는 값이 pydantic으로 정의한 틀과 동일한지 검증하는 역할이다. 이전에 모르고 사용했어서 씀

- 실제로 클라이언트 - 서버 간 데이터로 오고 가는 건 아니지만 DAO? DTO? 라고 생각하면 되는 걸까?

# FASTAPI 라이브러리

- `pip install "fastapi[all]"`

- `pip install "fastapi[all]"`로 설치하면 필요한 다른 라이브러리도 같이 설치가 되는데 FASTAPI가 빠른 이유는 libuv를 기반으로 Cython으로 작성된 uvloop를 쓰는 uvicorn 쓰는 starlette을 쓰기 때문인데 그냥 uvicorn을 설치하면 uvloop가 같이 설치가 되지 않기 때문에 위와 같이 설치하는 것이 권장된다고 한다.

- 그냥 설치하면 uvloop가 없나? 기억이 안나네 아무튼 이유가 참 기네....

- 그리고 처음 FastAPI를 접했을 때는 Django, Flask보다 더 쉽게 거의 Express 만큼 쉽게 서버 앱을 만들길래 되게 간단하고 가벼운 아직 잘 안쓰이는 프레임워크인줄 알았는데 오히려 성능이 좋아서 큰 규모의 서버에 더 많이 쓰이고 Go만큼 빠른 속도를 가지고 있다고 한다.

- 동시성 처리, 병렬 프로그래밍에도 강점을 보인다고 한다. 이건 공부할 의지를 높여준다.

# FastAPI 앱 배포

- 파이썬 서버 어플리케이션을 배포할 때 가장 난감했던 것 중 하나가 wsgi, asgi와 같은 인터페이스인데 FastAPI는 둘 모두 사용해서 배포한다고 한다.

- 우선 wsgi(Gunicorn), asgi(Uvicorn) 같은 CGI(Common Gateway Interface)들은 웹서버와 스크립트나 파이썬 프로그램 같은 다른 프로그램을 연결하는 표준화된 프로토콜이다.

- 둘 다 사용하는 이유는 wsgi는 멀티 프로세싱이 가능한데 복수의 워커 프로세스를 사용하는 기능을 uvicorn이 사용하기 위함이라고 한다. 서버의 cpu 코어 수 등 스펙에 맞게 그리고 컨테이너를 사용한다면 그 컨테이너에 할당된 코어 수에 맞게 사용하는 것 같다.

- 근데 너는 왜 jvm 같은게 없니... 너는 왜 Node.js 엔진이 없니...

- Nginx 외에 다른 웹서버를 사용하는지 찾아봤는데 wsgi, asgi가 WAS와 같은 동적 처리를 도와주는 역할을 하기 때문에 Nginx 같은 리버스 프록시가 가능한 웹서버와 함께 사용된다고 한다. Nginx + wsgi/asgi = WAS

