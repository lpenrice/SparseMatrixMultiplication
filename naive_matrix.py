class NaiveMatrix():
    def __init__(self, a):
        self.a = a
        self.rows = len(a)
        if len(a)>0:
            self.cols = len(a[0])
        else:
            self.cols = 3

    def make_empty_result_matrix(self, b):

        b_cols = b.cols

        return [[0 for col in range(b_cols)]for row in range(self.rows)]

    def __mul__(self, b):
        print("multiplying")
	    
        count = 0

        a_rows = self.rows
        a_cols = self.cols

        b_rows = b.rows
        b_cols = b.cols

        if self.cols == b.rows:
            rslt = self.make_empty_result_matrix(b)

            for i in range(0, a_rows):
                for j in range(0, b_cols):
                    for k in range(0, b_rows):
                        rslt[i][j] += self.a[i][k] * b.a[k][j]
                        count+=1
            return rslt,count
        else:
            raise Exception("Matrix dimensions are not compatible for multiplication.")
    
    def tostring(self):
        print(self.a)
            
