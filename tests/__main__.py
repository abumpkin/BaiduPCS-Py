import os
from .test_common import *

if __name__ == "__main__":
    import sys
    allFuncs = dir()
    allObjs = vars()
    tests = {i:allObjs[i] for i in allFuncs if callable(allObjs[i]) and i.startswith("test_")}
    argv = sys.argv
    if len(argv) > 1:
        funcName = argv[1]
        argv = argv[1:]
        if funcName == "-a":
            for n,f in tests.items():
                print("----- {} -----".format(n))
                f()
        elif funcName == "-l":
            for n,f in tests.items():
                print("----- {} -----".format(n))
                print(f.__doc__)
        else:
            for i in argv:
                if i in tests:
                    print("----- {} -----".format(i))
                    tests[i]()
                else:
                    print("没有函数: " + i)
    else:
        print(f"使用方法:\npython {os.path.basename(__package__)} 测试函数1 测试函数2 ...\n"
              "-a 执行全测试")