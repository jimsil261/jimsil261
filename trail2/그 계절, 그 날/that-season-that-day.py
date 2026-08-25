Y, M, D = map(int, input().split())

# Please write your code here.
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
months_yoon=[0,31,29,31,30,31,30,31,31,30,31,30,31]

def season_check(y,m,d):
    yoon_check=False
    if y%400==0:
        yoon_check=True
    elif y%100==0:
        yoon_check=False
    elif y%4==0:
        yoon_check=True
    
    if m>=13:
        print(-1)
    else:
        if yoon_check==True and months_yoon[m]>=d:
            if m==12 or m<=2:
                print("Winter")
            elif m<=5:
                print("Spring")
            elif m<=8:
                print("Summer")
            else:
                print("Fall")
        elif yoon_check==False and months[m]>=d:
            if m==12 or m<=2:
                print("Winter")
            elif m<=5:
                print("Spring")
            elif m<=8:
                print("Summer")
            else:
                print("Fall")
        else:
            print(-1)
season_check(Y,M,D)