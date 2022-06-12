import sys
from abc import ABC, abstractmethod

input = sys.stdin.readline


class EmptyStackException(Exception):
    def __init__(self, message):
        self.message = message
        pass

    def __str__(self):
        return self.message


class Stack(ABC):

    @abstractmethod
    def __init__(self):
        '''
        빈 Stack을 생성한다.
        '''
        pass

    @abstractmethod
    def __len__(self):
        '''
        길이를 얻는다.
        :return: 길이
        '''
        pass

    @abstractmethod
    def push(self, value):
        '''
        Stack의 맨 끝에 value를 추가한다.
        :param value: 추가할 값.
        '''
        pass

    @abstractmethod
    def pop(self):
        '''
        Stack의 맨 끝에 있는 value를 꺼내온다. Stack이 비어있을 경우, EmptyStackException이 발생한다.
        :return: 꺼낸 값.
        '''
        pass

    @abstractmethod
    def peek(self):
        '''
        Stack의 맨 끝에 있는 값을 조회한다. Stack이 비어있을 경우, EmptyStackException이 발생한다.
        :return: 맨 앞의 값.
        '''
        pass

    def add(self, value):
        self.push(value)

    def pull(self):
        return self.pop()

    def remove(self):
        return self.pop()


class StackJihoon(Stack):
    interval = 16

    def __init__(self):
        self.stack = [0] * self.interval
        self.index = -1

    def __len__(self):
        return self.index + 1

    def is_empty(self):
        return self.__len__() == 0

    def push(self, value):
        self.index += 1

        if self.index == len(self.stack):
            self.stack += [0] * self.interval

        self.stack[self.index] = value

    def pop(self):
        if self.is_empty():
            raise EmptyStackException('stack is empty')

        value = self.stack[self.index]

        self.index -= 1

        if self.index <= len(self.stack) - (self.interval * 1.5):
            self.stack = self.stack[:len(self.stack) - self.interval]

        return value

    def peek(self):
        if self.is_empty():
            raise EmptyStackException('stack is empty')
        return self.stack[self.index]


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        stack = StackJihoon()

        parenthesis_string = input().strip()

        is_invalid_stack = False
        for parenthesis in parenthesis_string:
            if parenthesis == '(':
                stack.push(parenthesis)
                continue
            try:
                temp = stack.pop()
            except EmptyStackException:
                is_invalid_stack = True
                break

        if is_invalid_stack or len(stack) != 0:
            print('NO')
            continue
        print('YES')
