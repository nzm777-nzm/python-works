
placements={"django":35,"java":67,"bigdata":40,"testing":30}

def get_value(key):
    
    return placements.get(key)

srt=sorted(placements,key=get_value,reverse=True)

print(srt)