with open('test.txt') as f:
    chunks = f.read().split("\n\n")
    rules, page_numbers = chunks[0], chunks[1]
    rules_list = rules.splitlines()
    rules_list = [rule.split("|") for rule in rules_list]
    page_numbers_list = page_numbers.splitlines()
    page_numbers_list = [page.split(",") for page in page_numbers_list]

def check_rule(rules_list, page_numbers_list):
    correct_ordered_pages = []
    for pages in page_numbers_list:
        correct = True
        for i, page in enumerate(pages):
            for rule in rules_list:
                if rule[0] == page:
                    if rule[1] in pages[:i]:
                       correct = False

        if correct:
            correct_ordered_pages.append(pages) 
    return correct_ordered_pages

def sum_middle_pages(correct_ordered_pages):
    pages_sum = 0

    for pages in correct_ordered_pages:
        middle_page = len(pages) // 2
        pages_sum += int(pages[middle_page])
    return pages_sum


print(check_rule(rules_list, page_numbers_list))

print(sum_middle_pages(check_rule(rules_list, page_numbers_list)))
