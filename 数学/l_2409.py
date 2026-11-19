class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        """
        分别获取alice和bot在罗马的日子 
        1、首先获取月份 
        2、根据日期遍历
        3、添加到集合中, 取交集（集合在python里面可以直接去交接，所以这里用集合存储） 
        """
        def get_day_sets(arrive_days:str, leave_days:str):


            daily_nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            arrive_month = int(arrive_days.split('-')[0])
            arrive_day = int(arrive_days.split('-')[1])

            leave_month = int(leave_days.split('-')[0])
            leave_day = int(leave_days.split('-')[1])

            start_daily_nums = sum(daily_nums[:arrive_month]) + arrive_day
            leave_daily_nums = sum(daily_nums[:leave_month]) + leave_day

            return start_daily_nums, leave_daily_nums

        Alice_days = get_day_sets(arriveAlice, leaveAlice)
        Bob_days = get_day_sets(arriveBob, leaveBob)


        return len(range(max(Alice_days[0], Bob_days[0]), min(Alice_days[1], Bob_days[1])))