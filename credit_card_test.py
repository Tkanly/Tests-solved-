credit_card = input("input credit card numbers: ")
size = len(credit_card)
def my_hiden_credit_card(credit_card):
    converted_cc = credit_card.replace(credit_card[size - 4:], '****')
    print(converted_cc)

my_hiden_credit_card(credit_card)