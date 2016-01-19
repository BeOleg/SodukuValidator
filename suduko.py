class SodukuValidator:
    def __init__(self, size, input):
        self.size = size
        self.outer_size = self.size * self.size
        self.solution = []
        inner_idx = 0
        for i in range(0, self.outer_size):
            self.solution.append([])
            for j in range(0, self.outer_size):
                self.solution[i].append(input[inner_idx])
                inner_idx += 1

    def validate_rows(self, index):
        return len(set(self.solution[index])) == len(self.solution[index])

    def validate_cols(self, index):
        revised_test_case = []
        for dynamic_idx in range(0, self.outer_size):
            if self.solution[dynamic_idx][index] in revised_test_case:
                return False

            revised_test_case.append(self.solution[dynamic_idx][index])

        return True

    def validate_inner(self, start_idx):
        res = []
        for row in self.solution[start_idx:start_idx+self.size]:
            for num in row[start_idx:start_idx+self.size]:
                if num in res:
                    return False
                res.append(num)

        return True

    def validate(self):

        for i in range(0, self.outer_size):
            if not self.validate_inner(i * self.size):
                return False

            if not all([self.validate_cols(i),
                        self.validate_rows(i)]):
                return False

        return True




test_input = '182543697' \
             '965178342' \
             '743962815' \
             '374896521' \
             '628451739' \
             '519237468' \
             '297684153' \
             '431725986' \
             '856319274'

validator = SodukuValidator(3, test_input)

print validator.validate()