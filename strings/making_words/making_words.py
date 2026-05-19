def can_make_word(word, arr):
    memo = {}

    def helper(subword):
        if subword == "":
            return True

        if subword in memo:
            return memo[subword]

        for piece in arr:
            if subword.startswith(piece):
                if helper(subword[len(piece):]):
                    memo[subword] = True
                    return True

        memo[subword] = False
        return False

    return helper(word)


# Example usage
arr = ["hello", "world", "po", "pu", "lar"]

print(can_make_word("helloworld", arr))                           # True
# print(can_make_word("worldhello", arr))                           # True
# print(can_make_word("helloworldlar", arr))                        # True
# print(can_make_word("popopopopopopopopolarlarworldlarhello", arr)) # True
#
# print(can_make_word("hello world", arr))  # False
# print(can_make_word("helloworld!", arr)) # False