class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for string in strs:
            length = len(string)
            encoded = ''.join((encoded, f'{length}#{string}'))
        return encoded

    def decode(self, encoded: str) -> list[str]:
        decoded_strings = []
        index = 0
        while index < len(encoded):
            # find length of string
            separator_index = index
            while encoded[separator_index] != '#':
                separator_index += 1
            length = int(encoded[index:separator_index])

            # extract string
            start_string = separator_index + 1
            end_string = start_string + length
            decoded_strings.append(encoded[start_string: end_string])

            # start new word
            index = end_string
        return decoded_strings



s = Solution()
encode = s.encode(["remember_that_a_word_length_may_have_more_than_1_digit", "consistency",":;","4#"])
print(encode)
print(s.decode(encode))