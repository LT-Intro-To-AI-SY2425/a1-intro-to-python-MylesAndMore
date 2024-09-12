# Complete your individualized AI problems here

# Fibonacci Sequence:
# Generate the first n numbers of the Fibonacci sequence.

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# Basic Password Generator:
# Write a program that generates a random password with a specified length.

import random
import string

def make_password(len: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len))

password = make_password(10)
print(f"gen pass: {password}")
assert len(password) == 10, "password length test"

# File Directory Traversal: 
# Write a program to recursively traverse a given directory and all its subdirectories, returning a list of all files with a specific extension (e.g., .txt).

import os

def find_files(directory: str, extension: str) -> list[str]:
    found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found.append(os.path.join(root, file))
    return found

files = find_files(".", ".py")
print(f"found files: {files}")
assert len(files) == 4, "file search test"

# FIFO Queue:
# Implement a FIFO queue with the following methods: enqueue, get, and size.

class FIFO:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
queue = FIFO()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert queue.size() == 3, "queue size test 1"
assert queue.get() == 1, "queue get test"
assert queue.size() == 2, "queue size test 2"
