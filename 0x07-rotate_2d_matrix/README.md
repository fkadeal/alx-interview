# Rotate 2D Matrix 
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

<br>
ns@etbaba$ cat main_0.py<br>
#!/usr/bin/python3<br>
"""<br>
Test 0x07 - Rotate 2D Matrix<br>
"""<br>
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix<br>
<br>
if __name__ == "__main__":<br>
    matrix = [[1, 2, 3],<br>
              [4, 5, 6],<br>
              [7, 8, 9]]<br>
<br>
    rotate_2d_matrix(matrix)<br>
    print(matrix)<br>
<br>
ns@etbaba$<br>
jessevhedden$ ./main_0.py<br>
[[7, 4, 1],<br>
[8, 5, 2],<br>
[9, 6, 3]]<br>
ns@etbaba$
