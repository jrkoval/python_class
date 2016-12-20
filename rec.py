def fun(x):
    if not x:
        return
    print(x)
    fun(x[1:])

fun(list(range(3)))

