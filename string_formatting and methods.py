name=input('enter ur name: ')
bio=f"""
 original  :{(name)}
 formatted :{(name.capitalize())}
 length    : {len(name)}
 Is alpha  :{name.isalpha()}
 Is upper  :{name.isupper()}
 count of a:{name.count('a')}"""
print(bio)