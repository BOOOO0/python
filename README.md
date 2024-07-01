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

# asyncio

- 파이썬에서 비동기 함수, 코루틴을 사용할 수 있게 해주는 라이브러리

- `async def [함수명]()`으로 비동기 함수를 선언할 수 있다.

- `asyncio.create_task([비동기 함수])`로 코루틴을 생성한다.

- main 스레드에서 `await`로 생성한 코루틴을 실행한다.

- 코루틴 내에서 다른 코루틴을 호출한다면 await를 사용해서 그 코루틴의 종료를 기다린다. 

- 코루틴은 병렬 프로그래밍이 아니고 동시성 처리이다. 멀티 프로세싱, 스레딩처럼 오고 가는 방식으로 순차 실행되지만 스레드 보다 가볍고 자원 사용이 적고 그 속도가 더 빨라 동시에 처리되는 것 처럼 보인다. 

# GIL (Global Interpreter Lock)

- GIL은 뮤텍스와 같은 경쟁 상태를 막기 위해 한번에 하나의 스레드만 실행될 수 있도록 하는 Lock이다.

- GIL에 의해서 병렬 프로그래밍이 불가능 했다. 코드 구현이 불가능한 것은 아니지만 병렬 프로그래밍을 통한 성능 향상을 기대할 수 없다.

- GIL의 등장 배경은 메모리 관련 문제의 예방으로 파이썬 GC는 이전에 본 것과 같이 레퍼런스 카운팅을 기준으로 메모리를 해제하는데 여기서 경쟁 상태가 생겨서 여러 스레드가 한 변수의 참조를 동시에 늘려서 0이 되지 않거나(?_이건 불확실) 0을 만들어 해제되게 만들거나 하는 문제를 방지하고자 나온게 GIL이다.

- GIL에 의해 두 스레드가 한 변수에 접근해 숫자를 같이 줄이는 코드가 실행 시간이 오히려 더 긴 것을 확인할 수 있다.

# 문자열 합치기

- 문자를 복사하지 않고 합치는 방법에 대해 찾아봤는데 그냥 `+` 연산자가 더 빠른데 뭐지...? 찾아보니까 더 빠른게 맞다고 한다. 기묘한 파이썬...

- 적은 수의 문자열을 빠르게 출력 등의 표현에 사용하려면 그냥 f스트링으로 출력하는게 나을 수도 있다. 그리고 join이 더 빠른 경우가 많다는데...? 잘 모르겠다. 연산 횟수가 많아도 느리다.

- join이 성능이 더 좋은 경우는 조금 더 길고 복잡한 문자열의 연산을 수행할 때 라고 한다. 그렇지 않은 단순한 문자를 반복 연산하는 경우는 +의 성능이 더 좋다고 한다. 이게 결론인 것 같다.

# zfill

- 회사 코드에서 zfill이 많이 보이는데 아마 바이트 크기의 특정 코드를 표현해야 하기 때문에 zfill을 사용하는 것 같다.

- [문자열].zfill(N)으로 N만큼의 크기를 가지고 문자열 앞부분을 0으로 채운다.

- 사용되진 않지만 비슷한 방식으로 사용할 수 있는 메소드로 rjust가 있다고 한다. [문자열].rjust(N, [채울 문자])로 채울 0이 아닌 채울 문자로 문자열의 앞부분을 길이 만큼 채우는 메소드이다.

- 우선 지금은 문자열을 다루거나 리스트, 딕셔너리 내에서 특정 데이터를 추출하거나 정렬하는 식의 알고리즘을 풀고 방향이 필요하다면 이렇게 가자.

# __new__, __init__, super()

- 파이썬 객체의 생성자에 대해 정리해보자.

- 기본적으로 init이 constructor의 역할을 하는 것으로 알고 있고 self가 this의 역할을 하는 것으로 알고 있다.

- 구체적인 동작 방식은 cosntructor와 다르다고 한다. init이 객체를 생성해서 메모리에 할당하는 과정까지 이끌지는 않기 때문이라고 한다.

- 메모리에 할당하는 역할을 하는 것은 __new__라고 한다. new가 init보다 먼저 실행되며 이때 객체가 메모리에 할당되고 그 다음 프로퍼티가 init에 의해 초기화되는 것 같다.

- new는 클래스 자기자신(cls)를 파라미터로 받으며 object 형태의 값을 반환한다.

- new와 init의 결합을 생성자라고 봐야할 것 같다.

- super()는 부모 클래스의 생성자를 호출하는 것인데 파이썬은 특이하게 `super().__init__`과 `super().__new__`를 둘 다 사용할 수 있다.

# bytearray

- 바이트는 0부터 255까지 2^4 까지의 8bit 이내의 2진수인 정수를 의미한다.

- 바이트 어레이는 그 바이트들을 연속적으로 저장하는 자료형이다.

- `b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'`와 같은 형태로 `\`로 구분되어있다. 표현은 16진수로 된다.

# 비트연산자

- 비트 연산자는 두 값을 비교할 때 2진수로 된 비트 형태로 변환한 다음 각 자리를 비교한다.

- `&`연산자는 and 연산자와 동일한데 두 값의 2^3 자리수가 둘 다 1이라면 해당 자리수를 1로 결정한다. 둘 중 하나만 0이여도 0이 된다.

```
0b1100
&
0b1001
=
0b1000
```

- 위와 같이 연산의 결과가 결정되는 것이다.

- `|`연산자는 or과 동일하게 하나만 1이면 1이 된다.

- `^`연산자는 XOR 연산자라고 하는데 두 값이 서로 다를 경우 1이 된다. `0b1100 ^ 0b1001 = 0b0101`와 같은 결과를 가진다.

- 숫자를 예시로 들어보자. 7과 3을 ^ 연산자로 연산을 해보면 `0b111 ^ 0b11`인데 `0b100`이 되어서 4가 된다.

- 시프트 연산자는 `<<`라면 오른쪽 맨 끝에 0을 추가하고 `0b111 << 1`은 `0b1110`이 된다. 반대로 `>>`라면 오른쪽 맨 끝 비트를 지운다. `0b111 >> 1`은 `0b11`이 된다. `7 << 1 = 14(1110)`, `7 >> 1 = 3(11)`

# yield

- yield는 함수의 반환인데 return처럼 값을 한번에 다 반환하는 것이 아니라 하나씩 메모리에 올려서 반환한다.

- 원리는 제너레이터라는 것을 사용하는건데 제너레이터는 iterable한 객체인데 리스트처럼 메모리에 올린 상태로 가지고 있는 것이 아니라 필요한 값을 그때그때 생성(?)한다.

- 제너레이터는 iterable할 뿐 인덱스를 가지고 있는 리스트, 튜플과는 다르다.

- iterable한 객체는 내장 객체에 __iter__ 항목을 가지고 있다고 한다.

# ML 도메인에서 파이썬을 잘 쓰는 법

- https://hyperconnect.github.io/2023/05/30/Python-Performance-Tips.html

# 성능 모니터링

- 성능 모니터링을 위해 당장 유료 APM을 사용하지는 않아도 될 것 같고 엘라스틱 APM이라는 것이 있고 오픈소스로도 가능한 것 같으니 시도해보자.

- 결국 내가 원하는 방향은 대용량 트래픽을 감당하는 고성능 서버 어플리케이션, 그 서비스가 실행되기 위한 큰 크기의 기반 인프라, 큰 조직을 위한 DevOps 문화 이 3가지를 익히는 것이니 파이썬 백엔드 실습을 간단하게 진행하면서 모니터링에 대한 부분도 같이 고민해보자. 큰 어플리케이션이 아니더라도 학습을 목표로 해보자.

- https://blog.naver.com/olpaemi/221973730638

# 삼항연산자

- `[True일 때 반환될 값] if True else [False일 때 반환될 값]`으로 사용한다.

# Lambda

- 람다 함수에 대해 깊게 정리하면 내용이 너무 많을테니 JS의 함수 표현식과 비슷하다고 볼 수 있다.

- `(lambda [원소]: [함수 식], [리스트 등의 객체])`

- 순회하면서 원소에 어떤 함수를 실행시키거나 다른 활용도 가능할 것 같다. 지금은 깊게 정리할 시간이 충분치 않다.

# map, filter, reduce

- 람다 함수와 함께 사용하면 JS의 고차함수와 거의 유사하게 사용할 수 있다. 이부분도 활용도를 높이려면 파이썬에 맞게 사용하는 방법에 대해 익혀야 될 것 같고 추후 자세히 정리하자.

# 리스트 표현식

- 알고리즘에서 DFS, BFS 등의 문제를 입력을 받아 board를 만들때 주로 사용했던 것 같다.

- `[i for i in range(10)]`과 같이 사용하면 0부터 9까지의 숫자를 원소로 가지는 리스트가 된다.