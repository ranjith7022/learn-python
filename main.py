def filter_messages(messages):
    filter_messages =[]
    count = [0]*len(messages)
    for i in range(len(messages)):
        if("dang"in messages[i].lower()):
            count[i]= messages[i].count("dang")
            filter_messages.append(" ".join([word.strip() for word in messages[i].split("dang") if word.strip()]))
            
        else:
            filter_messages.append(messages[i])


    
    return filter_messages,count

