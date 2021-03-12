import folium

def namer(name):
    """takes in a name as a string and returns folium formatted name"""
    named = "<i>" + name +"</i>"
    return named

def basin_mapper():
    
    """Takes no argument and plots all 8 basins on folium map"""
    
    b_map = folium.Map(location=[-6.1630, 35.7516], zoom_start=6, tiles="Stamen Terrain")
    #plots initial space for general area, using tanzania's coordinates
    
    basins = ['Pangani', 'Lake Victoria', 'Lake Nyasa', 'Lake Rukwa', 'Lake Tanganyika',
              'Rufiji', 'Wami / Ruvu', 'Ruvuma / Southern Coast']
    
    long_lat = [[-5.436390, 38.978951], [-0.755775, 33.438354], [-11.6707, 34.6857], [-7.029620, 31.343060], 
                [-6.2556, 29.5108], [-7.773888, 39.363889], [-6.11667, 38.81667], [-10.474445, 34.8888]]
    
    for i in range(0, len(basins)):
        folium.Marker(long_lat[i], namer(basins[i]), icon=folium.Icon(color="purple"), tooltip=tooltip).add_to(b_map)
        #plots a purple marker for each basin
    
    return b_map

def basin_split(bname, df):
    """takes the name of a basin as a string and the cleaned df. 
    Returns pair as a list iwth basin name and basin coords.
    Returns coords_target as a nested list of waterpoint coords and their functionality tag
    """
    tooltip = "Click me!"
    basins = ['Pangani', 'Lake Victoria', 'Lake Nyasa', 'Lake Rukwa', 'Lake Tanganyika',
          'Rufiji', 'Wami / Ruvu', 'Ruvuma / Southern Coast']
    
    long_lat = [[-5.436390, 38.978951], [-0.755775, 33.438354], [-11.6707, 34.6857], [-7.029620, 31.343060], 
                [-6.2556, 29.5108], [-7.773888, 39.363889], [-6.11667, 38.81667], [-10.474445, 34.8888]]
    
    for name in range(0, len(basins)):
        if basins[name] == bname:
            pair = [bname, long_lat[name]]
            #gets the coordinates for the specifed basin only
    
    basin_df = df[['latitude', 'longitude', 'basin', 'bi_target']]

    df_basin = basin_df.loc[basin_df['basin'] == bname]
    
    target = df_basin.bi_target.head(200).tolist()
    long = df_basin.longitude.head(200).tolist()
    lat = df_basin.latitude.head(200).tolist()
    
    coords = [[la,lo] for la,lo in zip(lat, long)]
    #list comp to create lists of water point coordinates, [latitude, longitude]
    coords_target = [[t,c] for t,c in zip(target, coords)]
    #nested list containing [functionality, [latitude, longitude]]
    
    #print(coords[:5])

    return pair, coords_target

def map_build(basin):
    """takes in one parameter that consists of a list with a basin name and its coordinates
    and the coordinates of every water point connected to that basin. Creates a map with a
    marker for the basin and marlers for x amount water points. Builds maps ofindividual basins."""
    
    basin_name = basin[0][0]
    basin_coords = basin[0][1]
    coords = basin[1]
    
    b = folium.Map(location= basin_coords, zoom_start=8, tiles="Stamen Terrain")
    #plots initial space for general area, using specified basin's coordinates
    
    tooltip = "Click me!"
    
    for coord in coords:
        if coord[0] == 'functional':
            folium.Marker(coord[1], "<i>str(i)</i>", icon=folium.Icon(color="green"), tooltip=tooltip).add_to(b)
        else:
            folium.Marker(coord[1], "<i>str(i)</i>", icon=folium.Icon(color="red"), tooltip=tooltip).add_to(b)
            #plots green markers for functional basin and red markers for non functional basins
    
    folium.Marker(basin_coords, namer(basin_name), tooltip=tooltip, icon=folium.Icon(color="purple")).add_to(b)
    #plots purple ,markers for specified basin
        
    return b


def Full_map(df):
    """Takes in the cleaned data frame and plots all eight basins and however many water points are specified"""
    
    basins = ['Pangani', 'Lake Victoria', 'Lake Nyasa', 'Lake Rukwa', 'Lake Tanganyika',
          'Rufiji', 'Wami / Ruvu', 'Ruvuma / Southern Coast']
    
    long_lat = [[-5.436390, 38.978951], [-0.755775, 33.438354], [-11.6707, 34.6857], [-7.029620, 31.343060], 
                [-6.2556, 29.5108], [-7.773888, 39.363889], [-6.11667, 38.81667], [-10.474445, 34.8888]]
    
    b = folium.Map(location= [-6.1630, 35.7516], zoom_start=6, tiles="Stamen Terrain")
    #plots initial space for general area, using tanzania's coordinates
    
    tooltip = "Click me!"
    
    for i in range(0, len(basins)):
        folium.Marker(long_lat[i], namer(basins[i]), tooltip=tooltip, icon=folium.Icon(color="purple")).add_to(b)
        #plots all 8 basins as purple markers

        
    basin_df = df[['latitude', 'longitude', 'basin', 'bi_target']]
    
    for index, row in basin_df.head(400).iterrows():
        if row['bi_target'] =='functional':
            folium.Marker([row['latitude'],row['longitude']], "<i>str(i)</i>", icon=folium.Icon(color="green"), tooltip=tooltip).add_to(b)
        else:
            folium.Marker([row['latitude'],row['longitude']], "<i>str(i)</i>", icon=folium.Icon(color="red"), tooltip=tooltip).add_to(b)
            #plots green markers for functional basin and red markers for non functional basins
        
    return b