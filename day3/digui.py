#递归
#函数自己调用自己
#必须用条件让他结束
def digui_def(n):
    print(n)
    if int(n/2)>0:
        return digui_def(int(n/2))
digui_def(19)
