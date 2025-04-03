#!/usr/bin/env python
"""
Wright-Fisher simulation
"""

#imports
import argparse
import numpy as np
import random


#WF code
class Population:
    def __init__(self, N=10, f=0.2, with_np = False):
        self.N = N
        self.f = f
        self.with_np = with_np

        derived_count = round(N*f)
        self.pop = [0] * (N - derived_count) + [1] * derived_count

        if with_np:
            self.pop = np.array(self.pop) #convert to a numpy array if with_np is set to True

    def __repr__(self):
        return f"Population(N={self.N}, f={self.f})"

    def step(self, ngens=1):
        for i in range(ngens):
            if self.with_np: #if with_np is set to True
                self.pop = np.random.choice(self.pop, size=self.N)
            else:
                self.pop = random.choices(self.pop, k=self.N)

    def isMonomorphic(self, ngens = 1):
        self.step(ngens = ngens)
        if sum(self.pop)/self.N == 1:
            return print("True")
        elif sum(self.pop)/self.N == 0:
            return print("True")
        elif 0 < sum(self.pop)/self.N < 1:
            return print("False")
        else:
            return print("Something funky happened")



#executable code
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", help="Population size (int)", 
                        dest='N', type=int, default=10)
    parser.add_argument("-f", "--freq", help="Frequency of derived allele. Must be float between 0 and 1", 
                        dest='f', type=float, default=0.2)
    parser.add_argument("--np", help="Choice to run with numpy. Default False", 
                        dest='with_np', type=bool, default=False)
    parser.add_argument("-g", "--gens", help="Number of generations for step and Monomorphic functions. Must be an integer", 
                        dest='ngens', type=int)
    parser.add_argument("-v", "--verbose", help="Increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print(args)
    else:
        p = Population(N = args.N, f = args.f, with_np = args.with_np)
        print(p)
        
    if args.ngens:
        print(f"Is the population monomorphic after {args.ngens} generations?")
        p.isMonomorphic(ngens = args.ngens)






