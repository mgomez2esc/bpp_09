# Miguel Gómez Gómez-Escalonilla
# miguel.gomez.escalonilla@gmail.com
# Practica02

import unittest
from main import ingresar_persona, leer_archivo, return_file
from faker import Faker
import random
import pandas as pd

class Test_main(unittest.TestCase):

    def testcase_01(self):

        faker = Faker()

        name = faker.first_name()
        lastname = faker.last_name()
        age = random.randint(18, 85)
        email = name + lastname +'.'+ str(random.randint(0, 999999)) +'@gmail.com'

        self.assertIsInstance(name, str)
        self.assertIsInstance(lastname, str)
        self.assertIsInstance(age, int)
        self.assertIsInstance(email, str)

        ingresar_persona(name, lastname, age, email)
        
    def testcase_02(self):
        
        faker = Faker()

        name = faker.first_name()
        lastname = faker.last_name()
        age = random.randint(18, 85)
        email = name + lastname +'.'+ str(random.randint(0, 999999)) +'@gmail.com'

        ingresar_persona(name, lastname, age, email)
       
        my_list = leer_archivo(email)
                      
        self.assertEqual(my_list[0][0], name)
        self.assertEqual(my_list[0][1], lastname)
        self.assertEqual(int(my_list[0][2]), age)
        self.assertEqual(my_list[0][3], email)
     
    def testcase_03(self):

        df = return_file()
        
        self.assertFalse(df.empty)

    def testcase_04(self):

        df = return_file()

        for i in df['email']:
            self.assertTrue(i.endswith('@gmail.com'))

    def testcase_05(self):

        df = return_file()
    
        self.assertEqual(len(df.columns), 4)


unittest.main()

