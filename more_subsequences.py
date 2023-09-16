def subsets(nums):

    out = set()

    def worker(seta, subset):
        nonlocal out

        if seta == "":
            if subset == "": return
            out.add(subset)
            return

        worker(seta[1:], subset + seta[:1])
        worker(seta[1:], subset)

    worker(nums, "")

    return out

print(subsets("ab"))
print(subsets("dd"))


def moreSubsequence(n: int, m: int, a: str, b:str) -> str:

    subset_a = subsets(a)
    subset_b = subsets(b)

    if len(subset_a) > len(subset_b):
        return a

    return b

print(moreSubsequence(n=2, m=2, a="ab", b="dd") )
print(moreSubsequence(n=1, m=3, a="f", b="eeg") )
# print(moreSubsequence(n=2, m=2, a="ab", b="dd") )
