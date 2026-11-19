import sys

def solve():

    origin_data = sys.stdin.read().strip().split()

    t = int(origin_data[0])
    users = origin_data[1:1+t]
    resisger_user = set()

    def check(user_name:str):
    
        if len(user_name) < 6 or len(user_name) > 12:
            return "illegal length" 

        if not user_name.isalpha():
            return "illegal charactor"

        if user_name in resisger_user:
            return "acount existed"

        resisger_user.add(user_name)
        return "registration complete"

    for user in users:
        print(f"{user}-> {check(user)}")



if __name__ == "__main__":

    solve()