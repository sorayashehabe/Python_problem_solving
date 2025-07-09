def past(h, m, s):
    if 0<=h<24 and 0<=m<60 and 0<=s<60:
        hour = h*60*60*1000
        second = s*1000
        minute = m*60*1000
        res = hour + second +  minute
        return res
    else:
        print ("please entre hour less than 24 and more than zero, minute less than 60 and more than zero ,second less than 60 and more than 0")
        
print (past(0,1,1))
   