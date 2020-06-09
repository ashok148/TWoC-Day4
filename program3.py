def Dict(d):
    s=d.values()
    l=sorted(s)
    u=l[-2]
    print("the second largest no. is")
    print(u)
f={'eggs':92,'bread':78,'milk':55,'apple':29}
Dict(f)