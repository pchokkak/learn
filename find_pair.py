def find_pair(A,sum):
    for i in range(len(A)-1):
        print(i)
        for j in range(i+1, len(A)):
            if A[i]+A[j] == sum:
                print("pair found at index{0} and {1} ie".format(i,j))
                print(A[i]+A[j])
                
    print("pair not found")

if __name__ == '__main__':

    A = [5,3,9,7,1,4,6]
    sum = 10

    find_pair(A,sum)

