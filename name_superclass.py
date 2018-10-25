# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:03:07 2018

@author: ssubedi
"""

class Person1(object):

    '''

    for normal inheritance

    '''

        

    def __init__(self, first, last):

        self.firstname = first

        self.lastname = last



    def Name(self):

        name = self.firstname + " " + self.lastname

        return name



class Person2(object):

    '''

    for overridden the __str__ method

    '''

    

    def __init__(self, first, last):

        self.firstname = first

        self.lastname = last



    def __str__(self):

        name = self.firstname + " " + self.lastname

        return name