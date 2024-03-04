while True:
    resp=[]
    num = int(input('digita:\n>>> '))

    while num>=1:
        bin = num % 2
        num = int(num /2)
        resp.append(bin)
    resp.reverse()

    print(resp)