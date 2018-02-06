import pyexcel

a_list_of_dictionaries = [
    {
        'title': "SU25",
        'link': 'http://google.com.vn'
    },
    {
        'title': "SU23-2",
        'link': 'http://google-2.com.vn'
    },

]

pyexcel.save_as(records=a_list_of_dictionaries,
dest_file_name='excel.xlxs')
