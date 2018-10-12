

def alter_date_format(date):
    # 9/29/1926
    if '-' in date:
        date = date.replace('-', '/')
    split_dob = date.split('/')
    split_dob[0] = split_dob[0].zfill(2)
    split_dob[1] = split_dob[1].zfill(2)
    return '/'.join(split_dob)

