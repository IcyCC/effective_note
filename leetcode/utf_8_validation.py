class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        bin_data = [format(i, '#010b')[-8:] for i in data]
        n = 0
        while n < len(bin_data):
            nbyte = 1
            if bin_data[n][0] != '0':
                nbyte = 0
                for i in bin_data[n]:
                    if i != '1':
                        break
                    nbyte = nbyte + 1

                if nbyte == 1 or  nbyte > 4:
                    return False
            if len(bin_data[n + 1: n + nbyte + 1]) < nbyte-1:
                return False
            if nbyte != 1:
                for b in bin_data[n + 1: n + nbyte]:
                    if not b.startswith("10"):
                        return False
            n = n + nbyte

        return True