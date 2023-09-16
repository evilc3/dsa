def partation_palindrome(str):
    # print('jsadasjdajs')
    # return
    def is_palindrome(x): return x == x[::-1]

    out = []

    def worker(start, end, ans):
        nonlocal out

        if start >= end:
            out.append(ans)
            return

        # print(start, end)

        for idx in range(start, end):
            #split left: start idx
            #split right: idx n

            left = str[start:idx+1]

            # print('left : ', str)
            # if current left is palindrome only then move on.
            if is_palindrome(left):
                worker(idx+1, end, ans + [left])

    worker(0, len(str), [])

    print(out)

    ###need to find the minimum
    return min([len(i) for i in out]) - 1

print(partation_palindrome("geek"))
print(partation_palindrome("aaaa"))
print(partation_palindrome("abcde"))
print(partation_palindrome("abbac"))