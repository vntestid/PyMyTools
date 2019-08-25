# Functions for GUI File
import os


def fileCheck(GUIValues):
    fpath = GUIValues['_INPUT_FILEPATH_']
    fname = fpath.split('/')[-1]
    fextn = fpath.split('.')[-1]

    return fname,fextn

def rowCount(GUIValues):
    filehandler = open(GUIValues['_INPUT_FILEPATH_'], 'r')
    delimiter = ','

    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    row_count = sum(1 for row in reader)

    return row_count


def fileSplit(GUIValues):
    filehandler = open(GUIValues['_INPUT_FILEPATH_'], 'r')
    delimiter = ','
    row_limit = GUIValues['_INPUT_NORMALSPLIT_']
    output_name_template='Output_%s.csv'
    output_path = GUIValues['_INPUT_CUSTSPLIT_OUTFOLDER_']
    keep_headers = GUIValues['_CHK_INCHEADER_']
    
    if GUIValues['_RB2_CS_']:
        row_limit = 50 #default row limit
    else:
        output_path = '.'
        row_limit = int(GUIValues['_INPUT_NORMALSPLIT_'])

    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


    return 'Completed'


        
