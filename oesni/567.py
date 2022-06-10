class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def to_dict(s):
            chrs = {}
            for c in s:
                try:
                    chrs[c] += 1
                except:
                    chrs[c] = 1
            return chrs

        permutation = to_dict(s1)
        # print("permutation: {0}".format(permutation))

        sub = to_dict(s2[0 : len(s1)])
        # print("[{idx}]{substr} -> {dict}".format(idx=0, substr=s2[0 : len(s1)], dict=sub))
        if sub == permutation:
            return True

        for idx in range(1, len(s2) - len(s1) + 1):
            sub[s2[idx - 1]] -= 1
            try:
                sub[s2[idx + len(s1) -1]] += 1
            except:
                sub[s2[idx + len(s1) -1]] = 1

            sub = {k: v for k, v in sub.items() if v > 0}

            # print("[{idx}]{substr} -> {dict}".format(idx=idx, substr=s2[idx: : idx + len(s1)], dict=sub))

            if sub == permutation:
                return True
        return False