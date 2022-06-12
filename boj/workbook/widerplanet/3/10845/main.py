#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from abc import ABC, abstractmethod

input = sys.stdin.readline


class EmptyQueueException(Exception):
    def __init__(self, message):
        self.message = message
        pass

    def __str__(self):
        return self.message


class Queue(ABC):

    @abstractmethod
    def __init__(self):
        '''
        빈 Queue를 생성한다.
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
    def enqueue(self, value):
        '''
        Queue의 맨 끝에 value를 추가한다.
        :param value: 추가할 값.
        '''
        pass

    @abstractmethod
    def dequeue(self):
        '''
        Queue의 맨 앞에 있는 value를 꺼내온다. Queue가 비어있을 경우, EmptyQueueException이 발생한다.
        :return: 꺼낸 값.
        '''
        pass

    @abstractmethod
    def peek(self):
        '''
        Queue의 맨 앞에 있는 값을 조회한다. Queue가 비어있을 경우, EmptyQueueException이 발생한다.
        :return: 맨 앞의 값.
        '''
        pass

    def add(self, value):
        self.enqueue(value)

    def push(self, value):
        self.enqueue(value)

    def pull(self):
        return self.dequeue()

    def remove(self):
        return self.dequeue()


class QueueJihoon(Queue):
    class Node():
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.__len__() == 0

    def enqueue(self, value):
        new = self.Node(value)

        new.prev = self.tail.prev
        new.next = self.tail
        new.prev.next = new
        new.next.prev = new

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException('queue is empty')

        value = self.head.next.value

        target = self.head.next

        target.next.prev = self.head
        self.head.next = target.next

        target.next = None
        target.prev = None

        self.size -= 1

        return value

    def peek(self):
        if self.is_empty():
            raise EmptyQueueException('queue is empty')

        return self.head.next.value

    def peek_last(self):
        if self.is_empty():
            raise EmptyQueueException('queue is empty')

        return self.tail.prev.value


if __name__ == '__main__':
    n = int(input())

    queue = QueueJihoon()
    result = []

    for _ in range(n):
        commands = input().strip().split()

        command = commands[0]

        if command == 'push':
            value = int(commands[1])
            queue.push(value)
        elif command == 'pop':
            try:
                result.append(queue.dequeue())
            except EmptyQueueException:
                result.append(-1)
        elif command == 'size':
            result.append(len(queue))
        elif command == 'empty':
            result.append(int(queue.is_empty()))
        elif command == 'front':
            try:
                result.append(queue.peek())
            except EmptyQueueException:
                result.append(-1)
        elif command == 'back':
            try:
                result.append(queue.peek_last())
            except EmptyQueueException:
                result.append(-1)
        else:
            raise AssertionError(f'{command} is not supported command.')

    print('\n'.join(map(str, result)))
