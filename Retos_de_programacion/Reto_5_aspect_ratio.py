import threading
import urllib.request
from fractions import Fraction

class Challenge5:

    def aspect_ratio(self, url):
        def rational_aspect_ratio(aspect_ratio):
            precision = 1.0E-6
            x = aspect_ratio
            a = round(x)
            h1, k1, h, k = 1, 0, a, 1

            while x - a > precision * k * k:
                x = 1.0 / (x - a)
                a = round(x)
                h, k, h1, k1 = h1, k1, h1 + a * h, k1 + a * k

            return h, k

        threading.Thread(target=lambda: self._calculate_aspect_ratio(url, rational_aspect_ratio)).start()

    def _calculate_aspect_ratio(self, url, rational_aspect_ratio):
        aspect_ratio_str = None

        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                bmp = bytearray(data)
                width, height = int.from_bytes(bmp[18:22], 'little'), int.from_bytes(bmp[22:26], 'little')
                aspect_ratio = height / width
                aspect_ratio_pair = rational_aspect_ratio(aspect_ratio)
                aspect_ratio_str = f"{aspect_ratio_pair[1]}:{aspect_ratio_pair[0]}"
        except Exception as e:
            print(f"No se pudo calcular el aspect ratio: {e}")

        if aspect_ratio_str:
            print(f"El aspect ratio es {aspect_ratio_str}")

if __name__ == "__main__":
    challenge = Challenge5()
    challenge.aspect_ratio("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png")
