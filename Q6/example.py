import PGaussSolver as GS
import math
import subprocess as SP
from time import process_time as PT
import matplotlib.pyplot as plt

def func(x):
    xN = 0.5 * x + 0.5
    return (xN**3 / (xN + 1) )* math.cos(xN**2)

#list for appending time
pyt_time = []
pyt_ans = []
cpp_time = []


max = 20
for n in range(1,max+1):
    t1_pyt = PT()
    my_solver = GS.PGaussSolver(0, 1, n, func)
    my_solver.exec()
    result = my_solver.result()
    t2_pyt = PT()
    t1_cpp = PT()
    SP.call(["cpp_code.exe", str(n)])
    t2_cpp = PT()
    print("Result of Pyt code (n = {}): {:.20}".format(n, result))
    print('time in Python (for n = {}) was : {:.3}'.format(n,t2_pyt - t1_pyt))
    print('time in C++ (for n = {}) was : {:.30}'.format(n,t2_cpp - t1_cpp))
    pyt_time.append(t2_pyt - t1_pyt)
    cpp_time.append(t2_cpp - t1_cpp)
    pyt_ans.append(result)
    print('\n')

cell_numbers= []
for i in range(max):
    cell_numbers.append(list())
    cell_numbers[i].append(i+1)
    cell_numbers[i].append(pyt_time[i]*1000000)
    cell_numbers[i].append(cpp_time[i]*1000000)

fig=plt.figure()
a = fig.add_subplot(111)
a.xaxis.set_visible(False)
a.yaxis.set_visible(False)
a.axis('off')
a.autoscale(enable=True)
columns = ('Degree', 'Python(us)', 'C++(us)')
result_table = a.table(cellText=cell_numbers,
          colLabels=columns,
          loc='center', cellLoc='center')
fig.show()


list_time = list(f for f in range(max))
#Plotting the timing
fig = plt.figure()
a = fig.add_subplot(111)
plt.plot(list_time, pyt_time, '-b', label='Python')
plt.plot(list_time, cpp_time, '-r', label='C++')
plt.legend(loc='upper left')
plt.xlabel('Degree', fontsize=10)
plt.ylabel('Run Time', fontsize=10)
plt.savefig('result.pdf')
plt.show()