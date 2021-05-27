class BitmapFile:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # There are 3 color channels per pixel
        # and there are width * height pixels.
        self.pixels = []
        for row in range(self.height):
            for col in range(self.width):
                self.pixels.append([0, 0, 0])

    def set_pixel(self, row, col, pixel):
        # row and col are integers
        # pixel is a sub-list of three values: [red, green, blue]
        loc = row * self.width + col
        self.pixels[loc][0] = pixel[2]
        self.pixels[loc][1] = pixel[1]
        self.pixels[loc][2] = pixel[0]

    def get_pixel(self, row, col):
        loc = row * self.width + col
        return self.pixels[loc]

    def write(self, file_name):
        # Write Bitmap File Header
        # Write Bitmap Info Header
        # Write pixels in BGR (blue, green red)
        # You can use self.get_pixel to get the
        # color values as a list.
        bmpfile = open(file_name, "wb")
        padding = 0
        if (self.width * 3) % 4 != 0:
            padding = 4 - (self.width * 3) % 4
        headers = BitmapHeaders(self.width, self.height)
        bmpfile.write(headers.make_headers())
        # Recall we count backwards for the rows
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                px = self.get_pixel(row, col)
                bmpfile.write(bytes(px))
            bmpfile.write(bytes(padding))
        bmpfile.close()

class BitmapHeaders:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def make_headers(self):
        ba = bytearray()
        # First the bitmap file header: signature (2 bytes), size (4 bytes), reserved (4 bytes), offset (4 bytes)
        # signature is always 'BM'
        ba += b'BM'
        # size is the total size of the file. We have 54 bytes in of header, followed by self.width * self.height pixels
        padding = 0
        row_bytes = (self.width * 3) % 4
        if row_bytes > 0:
            padding = 4 - row_bytes
        size = 54 + (self.width * 3 + padding) * self.height
        # We have to specify "little" byte order since BMP files require that the "little" end of
        # the four bytes go first.
        ba += size.to_bytes(length=4, byteorder='little')
        # 4 bytes of reserved. bytearray() automatically initializes these to 0, so we shouldn't have to do anything
        ba += int(0).to_bytes(length=4, byteorder='little')
        # Offset comes next. This is how far we have to jump to get to the pixel array, which means we have to
        # skip the file and info header, so we need to skip exactly 54 bytes
        offset = 54
        ba += offset.to_bytes(length=4, byteorder='little')
        # Now we get to the info header: 
        # size (4 bytes), width (4 bytes), height (4 bytes), planes (2 bytes), bits per pixel (2 bytes),
        # compression (4 bytes), bmp_size (4 bytes), horizontal resolution (4 bytes), vertical resolution (4 bytes),
        # colors (4 bytes), colors used (4 bytes)
        size = 40 # The info header is 40 bytes
        ba += size.to_bytes(length=4, byteorder='little')

        # Width
        ba += self.width.to_bytes(length=4, byteorder='little')
        # Height
        ba += self.height.to_bytes(length=4, byteorder='little')
        # Planes is 1
        ba += int(1).to_bytes(length=2, byteorder='little')
        # Bits per pixel is 24, we use 3 bytes per pixel which is 3 * 8 = 24 bits
        bpp = 3 * 8
        ba += bpp.to_bytes(length=2, byteorder='little')
        # Compression is 0
        ba += int(0).to_bytes(length=4, byteorder='little')
        # BMP size we can set to 0. This tells programs to figure it out with the width and height
        ba += int(0).to_bytes(length=4, byteorder='little')
        # horizontal and vertical resolutions can be set to 1
        hres = 96
        ba += hres.to_bytes(length=4, byteorder='little')
        vres = 96
        ba += vres.to_bytes(length=4, byteorder='little')
        # Colors and colors used can be set to 0 to signify the program should "figure it out"
        ba += int(0).to_bytes(length=4, byteorder='little')
        ba += int(0).to_bytes(length=4, byteorder='little')

        # We can only write the immutable bytes() version to a file, so we can convert the bytes
        # using the bytes() type caster.
        return bytes(ba)
import math
def main():
    width = 255
    height = 255
    bmf = BitmapFile(width, height)
    for row in range(height):
        for col in range(width):
            px = [(row + 100) % 256, (row + col) % 256, col % 256] # I changed the values here, I hope you like the abstract art :)
            bmf.set_pixel(row, col, px)

    bmf.write("test.bmp")

if __name__ == "__main__":
    main()

