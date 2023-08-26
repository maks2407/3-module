# def str_cpunter(s):
#     for sym in set(s):
#         counter = 0 
#         for sub_sum in s:
#             if sym == sub_sum:
#                 counter += 1
#         print(sym, counter)

# str_cpunter('ка')

def str_counter(s):
    sims_counter = {}
    for sym in s:
        sims_counter[sym] = sims_counter.get(sym, 0) + 1

    for sym, count in sims_counter.items():
        print(sym, count)

str_counter('aab')