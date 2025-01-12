class OffsetTester:
    def __init__(self, buffer_size):
        """
        Initialize the tester with a buffer size.
        """
        self.buffer = bytearray(buffer_size)
        self.size = buffer_size

    def write_at_offset(self, offset, data):
        """
        Write data at a specific offset.
        """
        if offset < 0 or offset >= self.size:
            raise OffsetOutOfBoundsError(f"Offset {offset} is out of bounds.")
        
        if len(data) + offset > self.size:
            raise OffsetOutOfBoundsError("Data exceeds buffer size.")

        self.buffer[offset:offset + len(data)] = data

    def read_at_offset(self, offset, length):
        """
        Read data at a specific offset.
        """
        if offset < 0 or offset + length > self.size:
            raise OffsetOutOfBoundsError(f"Offset {offset} or length {length} is invalid.")
        
        return self.buffer[offset:offset + length]

    def dump_buffer(self):
        """
        Print the buffer for debugging purposes.
        """
        print(self.buffer)
