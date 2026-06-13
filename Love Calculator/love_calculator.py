def calculate_love_score(name1,name2):
    
    name=name1+name2
    
    char1="t"
    char2="r"
    char3="u"
    char4="e"
    
    count1=name.lower().count(char1)
    count2=name.lower().count(char2)
    count3=name.lower().count(char3)
    count4=name.lower().count(char4)
    
    char5="l"
    char6="o"
    char7="v"
    char8="e"
    
    count5=name.lower().count(char5)
    count6=name.lower().count(char6)
    count7=name.lower().count(char7)
    count8=name.lower().count(char8)
    count8=name.lower().count(char8)
    
    total1=str(count1+count2+count3+count4)
    total2=str(count5+count6+count7+count8)
    
    
    total=total1+total2
    
    print(total)
    
calculate_love_score("Kanye West", "Kim Kardashian")