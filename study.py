import sys
import asyncio
import time
from threading import Thread

n = 1
ch = "a"
print(sys.getrefcount(ch), sys.getrefcount(n))
ls = []
ls.append(ch)
ls.append(n)
print(sys.getrefcount(ch), sys.getrefcount(ls), sys.getrefcount(n))


async def sleep():
    await asyncio.sleep(1)


async def add(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        await sleep()
        total += number
        print(f'작업중={name}, number={numbers}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린 시간={end - start}')
    return total


async def main():
    start = time.time()

    task1 = asyncio.create_task(add("A", [1, 2]))
    task2 = asyncio.create_task(add("B", [1, 2, 3]))

    await task1
    await task2

    result1 = task1.result()
    result2 = task2.result()

    end = time.time()
    print(f'총합={result1 + result2}, 총 시간={end - start}')


# A 작업과 B 작업이 동시에 일어난다.
if __name__ == '__main__':
    asyncio.run(main())

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = Thread(target=countdown, args=(COUNT // 2,))
t2 = Thread(target=countdown, args=(COUNT // 2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)


str1 = "Hello"
str2 = "World"

start = time.time()
str3 = str1 + str2
end = time.time()
print('StrSum Time taken in seconds -', end - start)

# join은 iterable한 객체의 문자열을 하나로 합친다. 앞에 오는 문자가 구분자가 된다.
list_1 = [str1, str2]
start = time.time()
str4 = "".join(list_1)
end = time.time()
print('StrJoinTime taken in seconds -', end - start)

start1 = time.time()
for x in range(10000000):
    dog1 = ' and '.join(['spam', 'eggs', 'spam', 'spam', 'eggs', 'spam','spam', 'eggs', 'spam', 'spam', 'eggs', 'spam'])

end1 = time.time()
print("Time to run Joiner = ", end1 - start1, "seconds")


start2 = time.time()
for x in range(10000000):
    dog2 = 'spam'+' and '+'eggs'+' and '+'spam'+' and '+'spam'+' and '+'eggs'+' and '+'spam'+' and '+'spam'+' and '+'eggs'+' and '+'spam'+' and '+'spam'+' and '+'eggs'+' and '+'spam'

end2 = time.time()
print("Time to run + = ", end2 - start2, "seconds")
