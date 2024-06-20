# Python

## With

- `with ~ as ~` 구문은 주로 파일을 열고 닫을 때 사용한다고 한다. 

```python
with open(path+"/"+"test_data.txt", "r", encoding='utf-8') as f:
    firstline = f.readline()
    print(firstline)
```

- 위와 같이 with as 구문이 끝나면 메모리 해제가 자동으로 된다.

- 의문 - 파이썬은 GC가 없나? 메모리 해제를 직접 하는 시스템 프로그래밍 언어가 아니지 않나? 파일 여는 것 외에도 사용이 되는 것 같은데 우선 파일을 여는 데에 메모리 사용이 어떻게 되는지도 한번 알아보자.

- 우선 open() 함수 자체가 다른 언어에서 파일 여는 것과 같이 close()를 동반 해야 하는 함수라고 한다. 하긴 sys 라이브러리에서 쓰는 함수이니... 시스템 콜과 사용이 다르지 않은게 맞을 것 같다..

- url을 호출하는 경우에도 with 구문을 사용하는데... 이 예시는 fetch를 사용해서인가? fetch는 파일을 여는 데에도 사용을 하고 동작 방식이 비슷하고 다른 URL, API 호출과 fetch는 방식이 다르다면...

## Python GC

- 파이썬의 가비지 컬렉터는 레퍼런스 카운팅을 기준으로 메모리를 관리한다. 참조 횟수가 0이 된 객체를 메모리에서 해제한다.

- 참조 횟수가 0이 아니더라도 0에 도달할 수 없는 순환 참조 상황도 해결한다.

- refConut의 기본값이 문자열은 13, 리스트는 2, 정수는 189로 나오는데 이건 뭐지...?

- 일단 위 의문점은 시스템 콜 open과 같기 때문으로 결론이 났고 GC 공부는 지금 필요하지 않으니 넘어가자.