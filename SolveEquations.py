import sys
import math
from typing import Union


class CalcOneEqual:
    def __init__(self) -> None:
        self.N: int = int(input("Enter count of uknowns: "))
        self.B: list[list[int]] = self.MakeMatrix()
        self.c: int = int(input("Enter c: "))

    def MakeMatrix(self) -> list[list[int]]:
        B = [
            [1 if i == j + 1 else 0 for j in range(self.N)] for i in range(self.N + 1)]
        for i in range(self.N):
            B[0][i] = int(input(f"Enter a{i}: "))
        return B

    def SearchMin(self) -> Union[bool, tuple[int]]:
        B = self.B
        N = self.N
        d_index: int = 0
        d: int = 0
        if N == 1:
            d = B[0][0]

        for index, item in enumerate(B[0][:]):
            if item != 0:
                if abs(item) < abs(B[0][d_index]):
                    d_index = index
                    d = item
                else:
                    d = B[0][d_index]

        if d == 0:
            return False
        else:
            return d, d_index

    def CalcRQ(self, a: int, b: int):
        r = a % b
        q = a // b

        if r < 0 and a * b < 0:
            q -= 1
            r = a - b * q
        if r < 0 and a * b > 0:
            q += 1
            r = a - b * q

        return r, q

    def CalcMatrix(self) -> None:
        r = q = count_not_null = 0
        N = self.N
        B = self.B

        while count_not_null != 1:

            res_searchmin = self.SearchMin()
            if not res_searchmin:
                raise ValueError("All elements are 0")
            else:
                d, d_index = res_searchmin

            self.d = d
            self.d_index = d_index
            count_not_null = 1

            for j in range(N):
                if B[0][j] != 0 and j != d_index:
                    r, q = self.CalcRQ(B[0][j], d)
                    B[0][j] = r

                    for i in range(1, N + 1):
                        B[i][j] -= q * B[i][d_index]

                if r != 0:
                    count_not_null += 1

    def WriteResult(self) -> None:
        if self.c % self.d == 0:
            for i in range(1, self.N + 1):
                t = 0
                print(f"\nx{(i-1)} = {self.B[i][self.d_index] * self.c / self.d}", end=" ")
                for j in range(self.N):
                    if j != self.d_index:
                        print(" + " + str(self.B[i][j]) + "*t" + str(t), end="")
                        t += 1
        else:
            raise ValueError("No solutions in integers")


class CalcSystemEquals:
    def __init__(self, m=None, n=None, B=None, write_res=True):
        # if m == None or n == None or B == None:
        #     self.m = int(input("Enter count of equals: "))
        #     self.n = int(input("Enter count of uknowns: "))
        #     self.B: list[list[int]] = self.MakeMatrix()
        #     self.write_res: bool = write_res
        #     return

        self.write_res: bool = write_res
        self.m: int = m
        self.n: int = n
        self.B: list[list[int]] = B

    def MakeMatrix(self):
        B = [[1 if (self.m + j) == i else 0 for j in range(self.n + 1)] for i in range(self.m + self.n)]
        for i in range(self.m):
            for j in range(self.n):
                B[i][j] = int(input(f"Enter a{i}{j}: "))
            B[i][self.n] = -1 * int(input(f"Enter c{i}: "))
        return B
    
    def SearchMin(self, index):
        _flag = False
        not_null_index = index

        try:
            for i in range(not_null_index, self.n):
                if self.B[index][not_null_index] != 0:
                    _flag = True
                    break
        except IndexError:
            raise Exception("Матрица введена неверно!")

        # Если в строке одни нули от элемента index, то возвращаем False
        if not _flag:
            return False
        
        d_index = not_null_index
        for i in range(not_null_index + 1, self.n):
            if self.B[index][i] != 0:
                if abs(self.B[index][i] < abs(self.B[index][d_index])):
                    d_index = i

        d = self.B[index][d_index]

        return d, d_index
        
    def CalcRQ(self, a: int, b: int):
        r = a % b
        q = a // b

        if r < 0 and a * b < 0:
            q -= 1
            r = a - b * q
        if r < 0 and a * b > 0:
            q += 1
            r = a - b * q

        return r, q
    
    def ReplaceRow(self, i_from, i_to):
        row = []
        for i in range(self.n + self.m):
            row.append(self.B[i][i_from])
            self.B[i][i_from] = self.B[i][i_to]
            self.B[i][i_to] = row[i]

    
    def CalcString(self, index):
        r = q = count_not_null = 0

        while count_not_null != 1:

            res_searchmin = self.SearchMin(index)
            if not res_searchmin:
                break
            
            d, d_index = res_searchmin
            self.d = d
            self.d_index = d_index
            count_not_null = 1

            for j in range(index, self.n):
                if self.B[index][j] != 0 and j != d_index:
                    r, q = self.CalcRQ(self.B[index][j], d)
                    self.B[index][j] = r

                    for i in range(index + 1, self.n + self.m):
                        self.B[i][j] -= q * self.B[i][d_index]

                if r != 0:
                    count_not_null += 1

            if d_index != index:
                self.ReplaceRow(d_index, index)

    def MakeLastRow(self, index):
        if self.B[index][index] == 0 and self.B[index][self.n] != 0:
            return False
        if self.B[index][index] != 0:
            if self.B[index][self.n] % self.B[index][index] != 0:
                return False
        if self.B[index][index] == 0 and self.B[index][self.n] == 0:
            return True
        r, q = self.CalcRQ(self.B[index][self.n], self.B[index][index])
        self.B[index][self.n] = r

        for i in range(index + 1, self.n + self.m):
            self.B[i][self.n] -= q * self.B[i][index]
        return True
    
    def CalcEquation(self):
        try:
            flag = True
            for i in range(self.m):
                self.CalcString(i)
                flag = self.MakeLastRow(i)
                if not flag:
                    break
            
            if not flag:
                raise ValueError("No solutions in integers")
            
            if self.write_res:
                self.WriteResult()

        except Exception:
            print("NO SOLUTIONS")

    
    def WriteResult(self):
        # print(self.B)

        index = 0
        while self.B[index][index] != 0 and index < self.m:
            index += 1
        
        # print(f"index = {index}")

        # left = index
        # right = self.n

        t = 0
        for j in range(index, self.n):
            if self.B[index][j] != 0:
                t += 1

        # print(f"t = {t}")
         
        print(t)

        for i in range(self.m, self.m + self.n):
            # t = 0
            # print(f"\nx{(i-self.m)} = {self.B[i][self.n]}", end=" ")
            for j in range(index, self.n + 1):
                print(f"{self.B[i][j]}", end=" ")
                # if self.B[i][j] != 0:
                #     print(" + " + str(self.B[i][j]) + "*t" + str(t), end="")
                #     t += 1
            print('')


def input_parsing():
    try:
        # Перепутаны местами m и n
        m, n = map(int, sys.stdin.readline().strip().split())
        equations = []

        if m >= 15 or n >= 15:
            raise Exception
        
        for _ in range(m):
            equation = list(map(int, sys.stdin.readline().strip().split()))
            if len(equation) == n + 1:
                equations.append(equation)
            else:
                print("Error: Неконсистентные входные данные")
                sys.exit()

        return m, n, equations
    
    except Exception:
        print("Error: Неконсистентные входные данные")
        sys.exit()


def create_b_matrix(m, n, equations):
    B = [[1 if (m + j) == i else 0 for j in range(n + 1)] for i in range(m + n)]

    for i in range(m):
        for j in range(n):
            B[i][j] = equations[i][j]
        B[i][n] = -1 * equations[i][n]
    
    return m, n, B
    

if __name__ == '__main__':
    # obj: CalcOneEqual = CalcOneEqual()
    # obj.CalcMatrix()
    # obj.WriteResult()
    in_data = input_parsing()
    m, n, B = create_b_matrix(*in_data)
    obj = CalcSystemEquals(m, n, B)
    obj.CalcEquation()
