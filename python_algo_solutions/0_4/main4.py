"""
Zig zag conversion of a string
[P] [ ] [A] [ ] [H] [ ] [N]
[A] [P] [L] [S] [I] [I] [G]
[Y] [ ] [I] [ ] [R] [ ] [ ]

[P] [ ] [ ] [I] [ ] [ ] [N]
[A] [ ] [L] [S] [ ] [I] [G]
[Y] [A] [ ] [H] [R] [ ] [ ]
[P] [ ] [ ] [I] [ ] [ ] [ ]

[P] [ ] [ ] [ ] [H] [ ]
[A] [ ] [ ] [S] [I] [ ]
[Y] [ ] [I] [ ] [R] [ ]
[P] [L] [ ] [ ] [I] [G]
[A] [ ] [ ] [ ] [N] [ ]

"""
list2 = [[],
         [],
         []]

def convert(s, numRows):
    result = ""
    if numRows == 1:
        result = s
        return result
    else:
        list1 = [[] for _ in range(numRows)]
        for i in range(len(s)):
            j = i % (2 * numRows - 2)
            if j >= numRows:
                j = 2 * numRows - 2 - j
            list1[j].append(s[i])
        word = ""
        for l in list1:
            for k in l:
                word += k
        return word
    


print(convert("abcdefghijk", 2))