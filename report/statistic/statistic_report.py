def report(case_handler):
    total = 0
    through = 0
    cases = case_handler.get_cases()
    for case in cases:
        total += 1
        if case.get_through() :
            through += 1
        else:
            print(case)
    print("total", total)
    print("through", through)
