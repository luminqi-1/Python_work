#3-4嘉宾名单
guests = ['小红','小华','小明']
print (guests[0] + '您好，欢迎来我家做客')
print (guests[1] + '您好，欢迎来我家做客')
print (guests[2] + '您好，欢迎来我家做客')

#3-5修改嘉宾名单
print (guests[0] + ',很遗憾，您不能来做客')		
guests[0] = '小强'
print (guests[0] + '您好，欢迎来我家做客')
print (guests[1] + '您好，欢迎来我家做客')
print (guests[2] + '您好，欢迎来我家做客')

#更大的餐桌
print ('我找到更大的餐桌了')
guests.insert(0,'李华')
guests.insert(2,'王强')
guests.append('王五')
print (guests[0] + '您好，欢迎来我家做客')
print (guests[1] + '您好，欢迎来我家做客')
print (guests[2] + '您好，欢迎来我家做客')
print (guests[3] + '您好，欢迎来我家做客')
print (guests[4] + '您好，欢迎来我家做客')
print (guests[5] + '您好，欢迎来我家做客')

#缩减名单
print ('只能邀请两个人来聚餐')
popped_guests = guests.pop(-1)
print (popped_guests + '抱歉，您不能来了')
popped_guests = guests.pop(-1)
print (popped_guests + '抱歉，您不能来了')
popped_guests = guests.pop(-1)
print (popped_guests + '抱歉，您不能来了')
popped_guests = guests.pop(-1)
print (popped_guests + '抱歉，您不能来了')
print (guests[0] + '请准时赴约')
print (guests[1] + '请准时赴约')
del guests[0]                 
del guests[0] 
print(guests)

