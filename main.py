import sys
from timeit import default_timer as timer

# palindrome checks libraries
from palindrome import search_first_palindrome_prime_n_sized

def main():
    # check the arguments given
    args = sys.argv[1:]

    if len(args) > 3:
        print("Too many arguments")
        print("Usage: python main.py <n_min> <n_max> <step>")
        return 0
    elif len(args) < 3 and len(args) != 1:
        print("Too few arguments")
        print("Usage: python main.py <n_min> <n_max> <step>")
        return 0
    
    n_min = int(args[0])
    n_max = int(args[1])
    step = int(args[2])

    if n_min <= 0 or n_max <= 0 or step <= 0:
        print("The arguments must be positive and greater than 0")
        return 0
    elif n_min > n_max:
        print("The n_min must be less than n_max")
        return 0
    elif step > n_max - n_min:
        print("The step must be less than n_max - n_min")
        return 0
    elif n_max > 10e3 or n_min > 10e3:
        print("The n_max and n_min must be less than 10e3")
        return 0
    
    mean_t = 0
    iter = 0
    # iterates from n_min to n_max with step
    for i in range(n_min, n_max + 1, step):
        
        '''if i%2 == 0:
            # if n is even, it is not a palindrome
            continue
        '''

        iter += 1
        start_t = timer()
        
        palindrome_prime, palindrome_pos = search_first_palindrome_prime_n_sized(i)
        
        end_t = timer()

        # calculates the time elapsed and moving average
        elapsed_t = end_t - start_t
        mean_t += elapsed_t

        if palindrome_prime == None and palindrome_pos == None:
            print(f"Did not find {i}-digits palindrome prime in the first 1 million digits of pi. Time elapsed: " + str(elapsed_t))
            continue
        print(f"Found {i}-digits palindrome prime \"{palindrome_prime}\" at position {palindrome_pos}. Time elapsed: " + str(elapsed_t))

    # prints the mean time
    if iter > 0:
        mean_t /= iter
        print("Mean time: " + str(mean_t))
    else:
        print("No palindrome prime found")

if __name__ == '__main__':
    main()