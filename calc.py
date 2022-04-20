class Calculator:
    def __init__(self, num):
        self.num = num

    def print_res(self):
        print(self.num)

    def __add__(self, new_value):
        self.num = self.num + new_value
        return self.num

    def __sub__(self, new_value):
        if isinstance(new_value, Calculator):
            self.num -= new_value.num
        if isinstance(new_value, int):
            self.num -= new_value
        return self.num

    def __mul__(self, new_value):
        if isinstance(new_value, Calculator):
            self.num *= new_value.num
        if isinstance(new_value, int):
            self.num *= new_value
        return self.num

    def __truediv__(self, new_value):
        if isinstance(new_value, Calculator):
            self.num /= new_value.num
        if isinstance(new_value, int):
            self.num /= new_value
        return self.num

    def __floordiv__(self, new_value):
        if isinstance(new_value, Calculator):
            self.num //= new_value.num
        if isinstance(new_value, int):
            self.num //= new_value
        return self.num
    
    def __mod__(self, new_value):
        if isinstance(new_value, Calculator):
            self.num %= new_value.num
        if isinstance(new_value, int):
            self.num %= new_value
        return self.num

    def __iadd__(self, new_value):
        if isinstance(new_value, int):
            self.num += new_value
        if isinstance(new_value, Calculator):
            self.num += new_value.num
        return self

    def __radd__(self, new_value):
        if isinstance(new_value, Calculator):
            return self.num + new_value.num
        else:
            return self.num + new_value


def main():
    v1 = Calculator(2)
    v2 = Calculator(2)

    # Examples
    v1 + v2
    v1.print_res()
    v1 * 2
    v1.print_res()


if __name__ == '__main__':
    main()
