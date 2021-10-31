import sys
import os
import subprocess
import argparse
from os import listdir
from Lexer import runlexer


TESTER_DIR = "Tester/"


def run_test(testname,inputname):
    lexer = TESTER_DIR+testname+"/"+testname+".lex"
    finput = TESTER_DIR+testname+"/input/"+inputname+".in"
    foutput = TESTER_DIR+testname+"/out/"+inputname+".out"
    freference = TESTER_DIR+testname+"/ref/"+inputname+".ref"
    
    runlexer(lexer,finput,foutput)
    val = subprocess.call(["diff","--ignore-all-space",foutput,freference])

    no_dots = 20
    set_no = int(testname.split('.')[1])
    if set_no == 10:
        no_dots -= 1
    if inputname == 10:
        no_dots -= 1
    dots = '.' * no_dots

    if val == 1:
        points = 0
        # print(testname+" "+inputname+" failed (see .out and .ref files)")
        print(testname + " " + inputname + dots + "failed [0p]")
    elif val == 0:
        if set_no == 1:
            points = 5
        else:
            points = 1
        # print(testname+" "+inputname+" passed!")
        print(testname + " " + inputname + dots + "passed [{}p]".format(points))

    return points

def run_test_group(testname):
    input_dir = TESTER_DIR+testname+"/input/"
    inputs = [os.path.splitext(f)[0] for f in listdir(input_dir)]

    print("Testset", testname)
    set_total = 0
    for i in inputs:
        set_total += run_test(testname,i)
    print("Set total" + '.' * 17 + "[{}p]".format(set_total))

    return set_total

def run_all():
    test_sets = ["T{}.".format(stage) + str(i) for i in range(1,11)]
    total = 0
    for test_set in test_sets:
        total += run_test_group(test_set)
        if test_set != test_sets[-1]:
            print()
    print("\nTotal" + '.' * 21 + "[{}p]".format(total))


# run_test("T3.11.Lecture-lexer","lecture01")
# run_test("T3.1","T3.1.1")
# run_test_group("T3.1")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FLA project checker')
    parser.add_argument('--stage', default='1',
                        help='Project stage')
    parser.add_argument('--set',
                        help='Name of test set directory')
    parser.add_argument('--test',
                        help='Test number')
    args = parser.parse_args()

    stage = int(args.stage)

    if args.test and not args.set:
        sys.exit("Test set must be specified if you want to run a specific test")

    if args.set:
        if args.test:
            run_test(args.set, args.test)
        else:
            run_test_group(args.set)
    else:
        run_all()

