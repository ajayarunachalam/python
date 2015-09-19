# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 9 - semordnilap
Python 2.7

A semordnilap is a word or a phrase that spells a different word when backwards
 ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:

nametag / gateman
dog / god
live / evil
desserts / stressed

Write a recursive program, semordnilap, that takes in two words and says if 
they are semordnilap.

This recursive function is not entirely straightforward. 
There are a few things that you need to check the first 
time you look at the inputs that you should not check on 
subsequent recursive calls: you need to make sure that the
 strings are not single characters, and also you need to
 be sure that the strings are not equal. If you do this
 check every time you call your function, though, this 
 will end up interfering with the recursive base case (which we don't want!).

There's a few different ways you can perform checks on the inputs 
the first time. The first way would be to use keyword arguments. 
The second way would be to use a global variable, which you'll see 
in the next lecture video; however, using global variables is always a 
bit risky and thus not the best way to do this.

The third way to perform checks on the inputs the first time you see them, 
but not any subsequent time, is to use a wrapper function. This wrapper 
function performs some checks, then makes a call to the recursive function.

The idea of a wrapper function is really important. You'll see more 
wrapper functions later. To introduce you to the idea, we are providing 
you with the wrapper function; your job is to write the recursive function 
semordnilap that the wrapper function calls. Here is the wrapper function:

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

"""

#%%

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    
    # needs to be same length
    if len(str1) != len(str2):
        return False
    
    # base case
    elif len(str1) == 1: # only need to check one because previous check same length
        return str1 == str2
    
    # recursive case first character of first has to be equal to last character
    # of second string. Check remaining characters recursively    
    return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])

    
#%%
    
semordnilapWrapper('dog', 'god')
semordnilapWrapper('live', 'evil')