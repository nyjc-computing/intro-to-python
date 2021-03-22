import requests


def search(searchterm):
    '''
    Returns search results from Open Library search API.
    
    Input:
        <str>
    
    Return:
        {'start': <int>,
         'num_found': <int>,
         'numFound': <1058>,
         'docs': [<dict>,
                  ...
                  ]
         }
    '''
    resp = requests.get(f'http://openlibrary.org/search.json?q={searchterm}')
    return resp.json()

def save_to_csv(list_of_dict, filepath):
    '''
    Writes data (with header row) to a CSV file
    
    Input:
        data (as a <list> of <dict>s)
        filepath (<str>)
    
    Return:
        None
    '''
    header = ['title', 'author_name', 'first_publish_year']
    with open(filepath, 'w') as f:
        f.write(','.join(header) + '\n')
        for entry in list_of_dict:
            data = []
            for key in header:
                try:
                    if type(entry[key]) == list:
                        element = entry[key][0].replace(',', '')
                    else:
                        element = str(entry[key]).replace(',', '')
                    data.append(element)
                except KeyError:
                    data.append('')
            f.write(','.join(data) + '\n')