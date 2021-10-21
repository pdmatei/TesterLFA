import sys
import subprocess
from os import listdir
import os
from Lexer import runlexer


TESTER_DIR = "Tester/"


def run_test_group(testname):
    input_dir = TESTER_DIR+testname+"/input/"
    inputs = [os.path.splitext(f)[0] for f in listdir(input_dir)]
    for i in inputs:
        run_test(testname,i)



def run_test(testname,inputname):
    lexer = TESTER_DIR+testname+"/"+testname+".lex"
    finput = TESTER_DIR+testname+"/input/"+inputname+".in"
    foutput = TESTER_DIR+testname+"/ref/"+inputname+".out"
    freference = TESTER_DIR+testname+"/ref/"+inputname+".ref"
    
    runlexer(lexer,finput,foutput)
    val = subprocess.call(["diff","--ignore-all-space",foutput,freference])
    if val == 1:
        print(testname+" "+inputname+" failed (see .out and .ref files)")
    if val == 0:
        print(testname+" "+inputname+" passed!")


def run_all():
    testlist = ["T3.1"]

    for test in testlist:
        run_test_group(test)


#def run_all():

#run_test("T3.11.Lecture-lexer","lecture01")
#run_test("T3.1","T3.1.1")
run_test_group("T3.1")
