from collections import Counter
from collections import defaultdict
import itertools
#zhkh = open('log_spb.txt')
#fias1 = open('27_1-24248.txt')
#fias2 = open('28_24249-48941')

#list_of_addresses = list()
#list_zhkh = list()
#list_fias1 = list()

def get_address_and_id_into_dict(address_file, precision, precision2):
    id_address_dict = {}
    for line in address_file:
        line = line.split("\",\"")
        if (len(line) == 11) and (line[8] == precision or line[8] == precision2):
            id_address_dict[line[0]] = line[7]
    return id_address_dict


def get_address_and_id_into_dict_with_one_precision(address_file, precision):
    id_address_dict = {}
    for line in address_file:
        line = line.split("\",\"")
        if (len(line) == 11) and (line[8] == precision):
            id_address_dict[line[0]] = line[7]
    return id_address_dict

def count_duplicates(dictionary_with_duplicates):
    counts = Counter((k[1], v) for k, v in dictionary_with_duplicates.items())
    return counts

def main():
    zhkh = open('log_spb.txt')
    fias1 = open('27_1-24248.txt')
    fias2 = open('28_24249-48941.txt')
    id_address_zhkh = get_address_and_id_into_dict(zhkh, 'exact', 'number')
    id_address_fias1 = get_address_and_id_into_dict(fias1, 'exact', 'number')
    id_address_fias2 = get_address_and_id_into_dict(fias2, 'exact', 'number')
    print (len(id_address_zhkh))
    print (len(id_address_fias1))
    print (len(id_address_fias2))
    zhkh_duplicates = count_duplicates(id_address_fias1)
    print (zhkh_duplicates)
    #counts = Counter((k[1], v) for k, v in id_address_zhkh.items())
    #print(counts)
    #print (Counter([(k, len(list(v))) for k, v in itertools.groupby(sorted(id_address_zhkh.values()))]))
    #print (id_address_zhkh)


if __name__ == "__main__":
    main()

'''
for line in zhkh:
    line = line.split("\",\"")
    #print (line[7])
    
    if (len(line) == 11) and (line[8] == 'exact' or line[8] == 'number'):
        list_zhkh.append(line[7])
    
for line in fias1:
    line = line.split("\",\"")
    if (len(line) > 7) and (line[8] == 'exact' or line[8] == 'number'):
        list_fias1.append(line[7])
count = 0
for address in list_zhkh:
    for address2 in list_fias1:
        if address == address2:
            count +=1
print (count)



    for i in fias1:
        i = i.split("\",\"")
        if i[

for i in list_of_addresses:
    for j in list_of_addresses:
        if i == j:
            print(i,j)
'''

#counter = (Counter(list_of_addresses))
#most_common = (counter.most_common())
#print (most_common)
#print (len(list_of_addresses))
#print (list_of_addresses)

