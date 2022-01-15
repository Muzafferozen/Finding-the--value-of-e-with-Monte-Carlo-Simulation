from FindEulerNumber_numba import TicToc, FindEulerNumber

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_euler = FindEulerNumber()
    finding_euler.number_more_than_one(1000000)
    euler = finding_euler.euler_number_result()
    print("EULER = %12.8f | Y = %d | X = %d" %
          (euler, finding_euler.y, finding_euler.x))
    print("TIME = %.6f seconds" % (tt.toc()))
