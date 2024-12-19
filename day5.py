with open('test.txt') as f:
    chunks = f.read().split("\n\n")
    rules, page_numbers = chunks[0], chunks[1]
    rules_list = rules.splitlines()
    rules_list = [rule.split("|") for rule in rules_list]
    page_numbers_list = [page.split(",") for page in page_numbers.splitlines()]

def check_rule(rules_list, pages):
    for rule in rules_list:

        if rule[0] not in pages or rule[1] not in pages:
            continue

        first = pages.index(rule[0])
        second = pages.index(rule[1])

        if first > second:
            return False
    return True

def get_middle_page(pages):
    middle_page = len(pages) // 2
    return pages[middle_page]

def reorder_pages(rules_list, pages):
    i = 0
    while i < len(rules_list):
        rule = rules_list[i]

        if rule[0] not in pages or rule[1] not in pages:
            i += 1
            continue

        first = pages.index(rule[0])
        second = pages.index(rule[1])

        if first < second:
            i += 1
            continue

        save = pages[first]
        pages[first] = pages[second]
        pages[second] = save

        i = 0

    return pages


total_sum_p1 = sum([int(get_middle_page(pages)) for pages in page_numbers_list if check_rule(rules_list, pages)])

total_sum_p2 = sum([int(get_middle_page(reorder_pages(rules_list, pages))) for pages in page_numbers_list if not check_rule(rules_list, pages)])

print(total_sum_p1, total_sum_p2)
