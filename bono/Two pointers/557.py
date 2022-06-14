class Solution:
    def reverseWords(self, s: str) -> str:
        splited_s = s.split(" ")

        results_s = ""
        for string in splited_s:
            middle_string_idx = len(string) // 2
            list_string = list(string)
            for idx in range(middle_string_idx):
                list_string[idx], list_string[-1 - idx] = (
                    list_string[-1 - idx],
                    list_string[idx],
                )
            temp_s = "".join(list_string)
            results_s += temp_s
            results_s += " "
        return results_s[:-1]
