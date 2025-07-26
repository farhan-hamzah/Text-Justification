from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            # Tentukan batas baris
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            # Ambil kata-kata dari i sampai j-1
            line_words = words[i:j]
            spaces_needed = maxWidth - sum(len(word) for word in line_words)
            num_slots = len(line_words) - 1

            # Jika ini baris terakhir atau hanya 1 kata → rata kiri
            if j == n or num_slots == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Hitung distribusi spasi
                space, extra = divmod(spaces_needed, num_slots)
                line = ""
                for k in range(num_slots):
                    line += line_words[k]
                    line += " " * (space + (1 if k < extra else 0))
                line += line_words[-1]  # kata terakhir tanpa spasi tambahan

            result.append(line)
            i = j

        return result
