import statistics as st
import random as rnd

def get_statistics(numbers: list[int]) -> dict:
    stat_dict: dict = {"sum": sum(numbers), "average": st.mean(numbers), "median": st.median(numbers),
                       "max": max(numbers), "min": min(numbers), "length": len(numbers)};
    return stat_dict;

num_list: list[int] = [rnd.randint(-100,100) for _ in range (15)];
print(num_list);
print(get_statistics(num_list));
