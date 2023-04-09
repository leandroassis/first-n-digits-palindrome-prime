# primality checks libraries
import AKS
import PSW

from time import sleep

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue):
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

def search_first_palindrome_prime_n_sized(n, pi_path="C:\\Users\\assis\\Downloads\\pi.txt"):
    queue = Queue()
    pos = 1

    with open(pi_path, "r") as f:
        digits = f.read()

        for digit in digits:
            # reads a digit and adds it to the queue
            if digit != '':
                queue.add(digit)

            # if queue is full
            if queue.size() == n:
                if is_palindrome(queue):
                    #checks if it is prime
                    if int("".join(queue.queue)) == 0:
                        return "".join(queue.queue), pos 
                    if PSW.baillie_PSW(int("".join(queue.queue))):
                        '''if AKS.aks(int("".join(queue.queue))) == 'Prime':'''
                        # return the palindrome prime
                        return "".join(queue.queue), pos 
                # if it is not a palindrome prime or it is not prime, remove the first digit
                queue.remove()
                pos+=1
        f.close()
    return None, None

def is_palindrome(queue):
    for i in range(queue.size() // 2):
        if queue.queue[i] != queue.queue[queue.size() - 1 - i]:
            return False
    return True