class Add:
    """This is a test class."""

    def add(self, x: int, y: int) -> int:
        """Add two integers and return their sum

            :param int x: first number to add
            :type int x: float
            :param y: second number to be added
            :type y: int

            :returns: Sum of x and y

            :rtype: int
        """

        return (x + y)


t = Add()
sum_ = t.add(37, 3)
print(sum_)
