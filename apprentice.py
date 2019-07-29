import whois

first = "secret"
last = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC",  
    "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA",  
    "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE",  
    "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC",  
    "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho",
    "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
    "Maine","Maryland","Massachusetts","Michigan","Minnesota",
    "Mississippi","Missouri","Montana","Nebraska","Nevada",
    "NewHampshire","NewJersey","NewMexico","NewYork",
    "NorthCarolina","NorthDakota","Ohio","Oklahoma",
    "Oregon","Pennsylvania","RhodeIsland","SouthCarolina",
    "SouthDakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","WestVirginia","Wisconsin","Wyoming",
    "sepa", "nepa","swpa","nwpa","npa", "wpa"
    ]

avail = []
com = []
org = []
net = []
i = 0

for place in last:
    full = "www." + first + place + ".com"
    try:
        test = whois.whois(full)
        avail.append(full)
        com.append(full)
        i+=1
    except:
        print(full + " is not available")
j = i

for place in last:
    full1 = "www." + first + place + ".org"
    try:
        test = whois.whois(full1)
        avail.append(full1)
        org.append(full1)
        i+=1
    except:
        print(full1 + " is not available")
k = i - j


for place in last:
    full2 = "www." + first + place + ".net"
    try:
        test = whois.whois(full2)
        avail.append(full2)
        net.append(full2)
        i+=1
    except:
        print(full2 + " is not available")
l = i - j - k

print("\n \n")
print(str(j)+" .com sites available")
print(str(k)+" .org sites available")
print(str(l)+" .net sites available")
print(str(i) + " websites available total")

print("\n.coms available")
for site in com:
    print(site + " is available")

print("\n.orgs available")
for site in org:
    print(site + " is available")

print("\n.nets available")
for site in net:
    print(site + " is available")


