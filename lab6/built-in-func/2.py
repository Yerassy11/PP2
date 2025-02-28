def count_case(s):
    return sum(map(str.isupper, s)), sum(map(str.islower, s))
r=count_case("CHEtam")
print(r)