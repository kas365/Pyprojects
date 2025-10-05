import numpy as np

def menu():
    print("""
        ================MATRIX CALCULATOR===============
        Choose the following options:
        1) Matrix Addition ---> 1
        2) Matrix Subtraction ---> 2
        3) Scalar Multiplication ---> 3
        4) Matrix Multiplication ---> 4
        5) Transpose ---> 5
        6) To Creat Identity ---> 6
        7) To Exist ---> 0
        =================================================
        """)

def get_rows():
    row_input = int(input("enter rows: "))
    return row_input
def get_col():
    col_input = int(input("enter columns: "))
    return col_input  

def matx(rows1,col1):
        # creating an empty list
        mat = []
        print("enter the elements: ",'\n')
        # taking input from user for list
        for i in range(rows1*col1):
            num = int(input())
            mat.append(num)
        # coverting list to array 
        a = np.array(mat).reshape(rows1,col1)
        return a   

def matx_add():
    # calling fuction
        rows = get_rows()
        col = get_col()
        a1 = matx(rows,col)
        a2 = matx(rows,col)
        print(a1)
        print(a2)
        print("RESULT:")
        print(a1+a2)

def matx_sub():
        rows = get_rows()
        col = get_col()
        a1 = matx(rows,col)
        print(a1)
        a2 = matx(rows,col)
        print(a2)
        print(f"{a1-a2}")
    
def matx_scaler():
        rows = get_rows()
        col = get_col()
        a1 = matx(rows,col)
        print(a1)
        s = int(input("enter the scalar : "))
        print(s)
        print(a1*s)

def matx_multi():
        rows = get_rows()
        col = get_col()
        # input of matrix 1:
        a1 = matx(rows,col)
        print(a1.shape)
        print(a1)

        # input of matrix 2:
        rows = get_rows() 
        col = get_col()
        a2 = matx(rows,col)
        print(a2.shape)
        print(a2)

        # vector multiplication :
        if a1.shape[1] == a2.shape[0]:
            print("the multiplied answer:")
            print(np.dot(a1,a2))
        else:
            print("ERROR : number of cols. of a1 = number of rows of a2")

def transpose_():
        rows = get_rows()
        col = get_col()
        a1 = matx(rows,col)
        print(a1)
        print(a1.T)
    
def matx_id():
        e = int(input("Enter the number of elements : "))
        a1 = np.identity(e)
        print(a1)

def main():

    menu()
    
    op = input("ENTER YOUR CHOICE : ")
    
    while op != '0':
    
        if op == '1':
            matx_add()
    
        elif op == '2':
            matx_sub()
            
        elif op == '3':
            matx_scaler()
            
        elif op == '4':
            matx_multi()
    
        elif op == '5':
            transpose_()
    
        elif op == '6':
            matx_id()
    
        menu()
        op = input("ENTER YOUR CHOICE : ") 
    
    else:
        print("have a wonderful day ahead!!! :) ")

if __name__ == "__main__":
    main()
    
    
