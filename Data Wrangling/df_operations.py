# output file content
!cat Data/microbiome_missing.csv 

# reindexing
baseball.reindex(baseball.index[::-1])

id_range = range(baseball.index.values.min(), baseball.index.values.max())
baseball.reindex(id_range)

# reindexing and filling missing values 
baseball.reindex(id_range, method='ffill', columns=['player','year']) #fills with previous value
baseball.reindex(id_range, fill_value='charliebrown', columns=['player'])

# Selecting with booleans
 data[[name.endswith('bacteria') for name in data['phylum']] and data['value'].values>1000]

# find all values in a column (number of players that played in two teams)
baseball_newind[baseball_newind['team'].isin(['LAN', 'SFN']).values]['player'].size

# extract a series from df (homeruns in 2006)
hr2006 = baseball.loc[baseball.year==2006, 'hr']
hr2006.index = baseball.player[baseball.year==2006]

# concatenate dfs
 pandas.concat([frame_one, frame_two])

# If your DataFrames do not have an identical structure,
# but do share a common key, you can also perform a SQL-style join using the .merge() function:

left = pandas.DataFrame({’key’: [’foo’, ’bar’], ’lval’: [1, 2]})
right = pandas.DataFrame({’key’: [’foo’, ’foo’, ’bar’], ’rval’: [3, 4, 5]})
pandas.merge(left, right, on=’key’)

# load data from different folders 

def load_data(files_path, column_total, column_description, feactures_tipe, path):
    values_df, values_data = [], []
    for file_ in files_path:
        df = pd.read_csv(file_, index_col=None, header=0)
        data= df[column_total][df[column_description].isin(feactures_tipe)].values
        values_df = np.append(values_df, data.astype(np.float))
        values_data.append(re.sub(path, '', file_))
    return values_df, values_data

def create_df(values_df, values_date, path, values_column):
    return pd.DataFrame(values_df.reshape((len(values_date), 2)), 
                  index =[[path]*len(values_date), values_date], 
                  columns = values_column)

# import various files using glob 

glob.glob('./[0-9].*')
glob.glob('*.gif')
glob.glob('?.gif')

# bacteria concatenation exercise

MID1.columns = MID2.columns = MID3.columns = MID4.columns = MID5.columns = MID6.columns = MID7.columns = MID8.columns = MID9.columns = ['Taxon' , 'Count']

MID1['BARCODE'] = 'MID1'
MID2['BARCODE'] = 'MID2'
MID3['BARCODE'] = 'MID3'
MID4['BARCODE'] = 'MID4'
MID5['BARCODE'] = 'MID5'
MID6['BARCODE'] = 'MID6'
MID7['BARCODE'] = 'MID7'
MID8['BARCODE'] = 'MID8'
MID9['BARCODE'] = 'MID9'

mixed = pd.concat([MID1, MID2, MID3, MID4, MID5, MID6, MID7, MID8, MID9], axis=0)
final = pd.merge(mixed, metadata)

# groupby and iterate (iterate over every patient)

cdystonia_grouped = cdystonia.groupby(cdystonia.patient)
for patient, group in cdystonia_grouped:
    print(patient, group)

# split-apply-combine

normalize = lambda x: (x - x.mean())/x.std()
cdystonia_grouped.transform(normalize)

# 3 longest segments travelled by each ship
top3segments = segments_merged.groupby('mmsi').apply(top, column='seg_length', n=3)[['names', 'seg_length']]

# proportion of survivors 

survivorsBySexClass = dataSurvivorsSexClass.groupby(['sex', 'pclass']).sum().apply(lambda x: 100*x/float(x.sum()))
