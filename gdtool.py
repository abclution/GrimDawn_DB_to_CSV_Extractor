
# CONSTANTS
import glob
import csv
import time
#import pandas as pd
INPUT_FOLDER="D:\Python_GD\data\enchants"
OUTPUT_FILE="D:\Python_GD\output.csv"
OUTPUT_FILE_SORTED="D:\Python_GD\output_sorted.csv"
#######################################
path = r'D:\Games\Steam\SteamApps\common\Grim Dawn\settings\text_en' # use your path
all_files = glob.glob(path + "/*.txt")
tagToNameDict = {}

for filename in all_files:
        with open(filename) as import_data:
            for line in import_data :
                tag, text = line.partition("=")[::2]
                # tagToNameDict
                # myvars[name.strip()] = float(var)
                tagToNameDict[tag.strip()] = str(text)
# print(tagToNameDict[tagEnchantA01])
#print(tagToNameDict.keys())
##for i in tagToNameDict:
##   if i == "tagEnchantA01" :
##        print (i, tagToNameDict[i])
#                break
#time.sleep(30)            
# https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file/9161531
#############################################
# path = r'INPUT_FOLDER' # use your path
path = r'D:\Python_GD\data\combined' # use your path
all_files = glob.glob(path + "/*.dbr")
#all_files = glob.glob(path + "/*.test")
#headerlist = []
#datalist = []
listOfDicts = []
for filename in all_files:
    headerlist = []
    datalist = []
    #print(filename)
    with open(filename) as import_data:
        for line in import_data :
            # print(repr(line))
            import_line = line.rstrip(',\n')
            #print(repr(import_line))
            #break
            header, data = import_line.split(",")
            headerlist.append(header)
            datalist.append(data)
            
#            if header == "description" : print(tagToNameDict[data])  # This is where to get the item name from the tag_items.txt
            if header == "description" : 
                #print(data)  # This is where to get the item name from the tag_items.txt
                for i in tagToNameDict:
                    if i == data :
                        print (i, tagToNameDict[i])
                        headerlist.append("aaa_ItemName")
                        datalist.append(tagToNameDict[i])
            #break
    thisdict = dict(zip(headerlist,datalist))        
    print(filename)
    print(f"This dict: {len(thisdict)}")
    listOfDicts.append(thisdict)
    print(f"List of dicts: {len(listOfDicts)}")

# https://stackoverflow.com/questions/53191611/convert-list-of-dicts-to-csv-in-python-3
len(listOfDicts)

keys = set()        # Remove duplicated
for d in listOfDicts:
    keys.update(d.keys())

with open(OUTPUT_FILE, 'a', newline='') as output_filez:
    dict_writer = csv.DictWriter(
        output_filez, fieldnames=keys, restval='', delimiter=',')
    dict_writer.writeheader()
    dict_writer.writerows(listOfDicts)
    output_filez.close()


# Get headers from created csv, sort them.
# https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file
with open(OUTPUT_FILE, 'r') as infile:
    # output dict needs a list for new column ordering


    # fieldnames = ['A', 'C', 'D', 'E', 'B']
    reader = csv.reader(infile)
    i = next(reader)
    fieldnames = sorted(i)
    # print(fieldnames)
    infile.close()

    
# https://stackoverflow.com/questions/33001490/python-re-ordering-columns-in-a-csv/33002011
with open(OUTPUT_FILE, 'r') as infile, open(OUTPUT_FILE_SORTED, 'a', newline='') as outfile:

    # output dict needs a list for new column ordering

    
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, restval='', delimiter=',')
    # # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
    #     # writes the reordered rows to the new file
        writer.writerow(row)