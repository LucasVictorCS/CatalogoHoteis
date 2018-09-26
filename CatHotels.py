cat={
  'Hotel A': {'price':300,'distanceBeach':100,'star':5},
  'Hotel B': {'price':100,'distanceBeach':900,'star':3},
  'HOtel C': {'price':400,'distanceBeach':100,'star':4},
  'HOtel C': {'price':300,'distanceBeach':200,'star':5}
  }
final=cat
for key in list(cat):
  for key2 in list(cat):
    a=cat[key]
    b=cat[key2]
    count=0
  
    if key!=key2:
      if a['price']>=b['price']and a['distanceBeach']>=b['distanceBeach']and a['star']<=b['star']:
        if a['price']>b['price']or a['distanceBeach']>b['distanceBeach']or a['star']<b['star']:
          del final[key]
        break
for key in final:
  print(key)
input("")

















    
  










