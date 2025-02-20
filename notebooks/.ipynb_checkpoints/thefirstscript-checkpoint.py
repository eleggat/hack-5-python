#!/usr/bin/env python

#imports
import argparse
import random
import string

#the function
def random_password(length=10):
    # Define the set of available characters to sample from
    chars = string.ascii_letters + string.digits + string.punctuation #concatenate strings of letters, numbers, punctuation

    # Generate a sample from this list
    password = random.choices(chars, k=length)

    # password is a list of characters here so `join` them together into
    # a string
    return "".join(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="Password length in characters", 
                        dest='length', type=int, default=10)
    args = parser.parse_args()

    print(random_password(length=args.length))