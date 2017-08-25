

def get_tens(tens):
    if tens== 9:
        tens_word= 'ninety'
    elif tens==8:
        tens_word= 'eighty'
    elif tens==7:
        tens_word= 'seventy'
    elif tens==6:
        tens_word= 'sixty'
    elif tens==5:
        tens_word= 'fifty'
    elif tens==4:
        tens_word= 'forty'
    elif tens==3:
        tens_word= 'thirty'
    elif tens==2:
        tens_word='twenty'
    elif tens== 0:
        tens_word=''
    return tens_word

def get_teens_word(num):
    if num == 11:
        teens_word = 'eleven'
    else:
        teens_word='not eleven'
    return teens_word

def get_ones(ones):
    if ones==1:
        ones_word= 'one'
    elif ones==2:
        ones_word= 'two'
    elif ones==3:
        ones_word= 'three'
    elif ones==4:
        ones_word='four'
    elif ones==5:
        ones_word='five'
    elif ones==6:
        ones_word='six'
    elif ones==7:
        ones_word='seven'
    elif ones== 8:
        ones_word='eigth'
    elif ones==9:
        ones_word='nine'
    return ones_word

def main():
    num=int(input('a number between 1 and 99. For example 22, 02, or 50:'))
    tens=num//10
    ones=num%10
    if num == 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        teens_word=get_teens_word(num)
        output = teens_word
    else:
        tens_word=get_tens(tens)
        ones_word=get_ones(ones)
        output = tens_word + ones_word
    # print(tens_word + tens2_word + ones_word)
    print(output)
main()
