def rod_cutting(n, dim_price={}):

    return rod_cutting(n-1, dim_price)



if __name__ == "__main__":
    dim_price = {0: 5, 1: 11, }
    rod_cutting(10)
