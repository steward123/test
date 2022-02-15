def trianglegenerate_pattern1(n):
    for i in range(1,n,1):
        print(((int(str(i)*i)) if(i<n) else "\n"))
if __name__ == '__main__':
    n = int(input("Enter a number : "))
    trianglegenerate_pattern1(n)