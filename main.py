# python3

def parallel_processing(n, m, data):
    output = []
    thread = [0] * n
    time = 0
    mask = False
    while True:
        for s in range(n):
            if thread[s] == 0:
                if len(data) == 0:
                    mask = True
                    break
                thread[s] = data[0]
                data.pop(0)
                output.append([s, time])
            thread[s] -= 1
        if mask == True:
            break
        time += 1

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    count = list(map(int, input().split()))
    n = count[0]
    m = count[1]

    # second line - data 
    # data - contains m integers t(s) - the times in seconds it takes any thread to process s-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for s, r in result:
        print(s, r)

if __name__ == "__main__":
    main()
