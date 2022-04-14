
# IMPORTS
import glob
import csv
import time


# CONSTANTS
INPUT_FOLDER="D:\Python_GD\data\combined"
OUTPUT_FILE="D:\Python_GD\output.csv"
OUTPUT_FILE_SORTED="D:\Python_GD\output_sorted.csv"

TRANSLATIONS_PATH="D:\Games\Steam\SteamApps\common\Grim Dawn\settings\text_en" # use your path
# Translation path is a subfolder in the Grim Dawn path, under settings folder. 
# The exact folder you wish to use will depend on the language you are trying to
# extract the database strings for.


#######################################

''' This section loads the translated strings from the Grim Dawn text translations folder
into a dict to be used later.'''
# path = r'TRANSLATIONS_PATH' # use your path
all_files = glob.glob(TRANSLATIONS_PATH + "/*.txt")

tagToNameDict = {}

for filename in all_files:
        with open(filename) as import_data:
            for line in import_data :
                tag, text = line.partition("=")[::2]
                
                # The translation text files have records that look a bit like this:
                # tagGDX2WeaponBluntB203={^L}Gannar'vakkar's Sting
                # We split on the "=" getting a tuple ex. ( tagGDX2WeaponBluntB203, =, {^L}Gannar'vakkar's Sting )
                
                tagToNameDict[tag.strip()] = str(text)

# https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file/9161531
#############################################




#############################################

all_files = glob.glob(INPUT_FOLDER + "/*.dbr")


listOfDicts = []
for filename in all_files:
    headerlist = []
    datalist = []

    with open(filename) as import_data:
        for line in import_data :
            
            import_line = line.rstrip(',\n')
            header, data = import_line.split(",")
            headerlist.append(header)
            datalist.append(data)
            
            

            if header == "description" :    #
                # .dbr files contain lines that look like this
                # description,tagEnchantA005A,
                # The description line actually is a tag that is resolved via lookup
                # in the translations text.

                for i in tagToNameDict:
                    if i == data :
                        # debug print (i, tagToNameDict[i])

                        headerlist.append("aaa_ItemName")
                        datalist.append(tagToNameDict[i])
                        
                        # We will add a new column (header) for that resolves the .dbr item to its language tag.
                        # The name of aaa_ItemName is arbitrary, but named with aaa to be one of the first columns
                        # after the sorting procedure below, as for humans, the item name is the most identifiable.

                        
            
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