from FindEulerNumber import TicToc,FindEulerNumber

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    euler_number_find = FindEulerNumber()
    euler_number_find.number_more_than_one(100000)
    euler_number = euler_number_find.euler_number_result()
    print("Euler Number = %12.8f | X = %d | Y= %d" %
          (euler_number, euler_number_find.x, euler_number_find.y))
    print("TIME = %.6f seconds" % (tt.toc()))