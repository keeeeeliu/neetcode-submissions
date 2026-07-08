class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])
        m_l, n_l = 0, 0
        m_r, n_r = num_row - 1, num_col - 1
        entrance = 0
        while m_l <= m_r:
            m_m = (m_l + m_r) // 2
            if m_l == m_r:
                entrance = m_m
            if matrix[m_m][0] < target:
                if matrix[m_m][-1] < target:
                    m_l = m_m + 1
                else:
                    entrance = m_m
                    break

            elif matrix[m_m][0] > target:
                m_r = m_m - 1
            else:
                return True
        
        while n_l <= n_r:
            n_m = (n_l + n_r) // 2
            if matrix[entrance][n_m] < target:
                n_l = n_m + 1
            elif matrix[entrance][n_m] > target:
                n_r = n_m - 1
            else:
                return True
        return False