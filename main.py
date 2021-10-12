import random, time
import insertion_sort, selection_sort, merge_sort, shellsort


def randomize(num):
    rand_arr = []
    for i in range(num):
        rand_arr.append(random.randint(0, num))
    return rand_arr

def randommax(num):
    rand_arr = []
    for i in range(num):
        rand_arr.append(i)
    return rand_arr

def randommin(num):
    rand_arr = []
    for i in range(num):
        rand_arr.append(num-i)
    return rand_arr

def randomset(num):
    rand_arr = []
    for i in range(num):
        rand_arr.append(random.randint(1, 3))
    return rand_arr

fin_ins = []
fin_sel = []
fin_mer = []
fin_shel = []

for j in range(7, 16):
    print(j)
    num = 2**j

    insertion = [[]]
    selection = [[]]
    merge = [[]]
    shell = [[]]

    for i in range(5):
        print(i)
        rand_arr = randomize(num)

        timei = time.time()
        insertion_sort.insertion_sort(rand_arr.copy())
        timei = time.time() - timei
        insertion[0].append(timei)

        timei = time.time()
        selection_sort.selection_sort(rand_arr.copy())
        timei = time.time() - timei
        selection[0].append(timei)

        timei = time.time()
        merge_sort.merge_sort(rand_arr.copy())
        timei = time.time() - timei
        merge[0].append(timei)

        timei = time.time()
        shellsort.shellsort(rand_arr.copy())
        timei = time.time() - timei
        shell[0].append(timei)

    #___________________________max

    rand_arr = randommax(num)

    timei = time.time()
    shellsort.shellsort(rand_arr.copy())
    timei = time.time() - timei
    shell.append(timei)

    timei = time.time()
    insertion_sort.insertion_sort(rand_arr.copy())
    timei = time.time() - timei
    insertion.append(timei)

    timei = time.time()
    selection_sort.selection_sort(rand_arr.copy())
    timei = time.time() - timei
    selection.append(timei)

    timei = time.time()
    merge_sort.merge_sort(rand_arr.copy())
    timei = time.time() - timei
    merge.append(timei)

    #___________________________min

    rand_arr = randommin(num)

    timei = time.time()
    shellsort.shellsort(rand_arr.copy())
    timei = time.time() - timei
    shell.append(timei)

    timei = time.time()
    insertion_sort.insertion_sort(rand_arr.copy())
    timei = time.time() - timei
    insertion.append(timei)

    timei = time.time()
    selection_sort.selection_sort(rand_arr.copy())
    timei = time.time() - timei
    selection.append(timei)

    timei = time.time()
    merge_sort.merge_sort(rand_arr.copy())
    timei = time.time() - timei
    merge.append(timei)

    #___________________________set

    rand_arr = randomset(num)

    timei = time.time()
    shellsort.shellsort(rand_arr.copy())
    timei = time.time() - timei
    shell.append(timei)

    timei = time.time()
    insertion_sort.insertion_sort(rand_arr.copy())
    timei = time.time() - timei
    insertion.append(timei)

    timei = time.time()
    selection_sort.selection_sort(rand_arr.copy())
    timei = time.time() - timei
    selection.append(timei)

    timei = time.time()
    merge_sort.merge_sort(rand_arr.copy())
    timei = time.time() - timei
    merge.append(timei)

    fin_ins.append(insertion)
    fin_sel.append(selection)
    fin_mer.append(merge)
    fin_shel.append(shell)



print(fin_ins)
print(fin_sel)
print(fin_mer)
print(fin_shel)

