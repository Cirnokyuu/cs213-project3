
def if_integer(string):
    return string.isdigit() and int(string)<2030

with open('./dataset.csv', 'r', encoding='utf-8') as file: 
    lines = file.readlines() 
    lines = lines[1:]
    out = [
        'begin;\n', 
        'create table books(\n', 
        ' title varchar,\n',
        ' author varchar,\n',
        ' publisher varchar,\n',
        ' keywords varchar,\n',
        ' clc_index varchar,\n',
        ' year_of_publication integer\n',
        ');\n'
    ];



    for line in lines: 
        tmp = line.split(',')
        assert len(tmp)==7
        del tmp[4]
        pref='INSERT INTO books(title,author,publisher,keywords,clc_index,year_of_publication) VALUES ('
        for i in range(0,6):
            tmp[i] = tmp[i].replace('\n', '')
        for i in range(0,5):
            if tmp[i].count('null')>0 or len(tmp[i])==0:
                pref+='null,'
            else:
                pref+='\''+tmp[i]+'\','
        yr = tmp[5].split('.')[0]
        if if_integer(yr):
            pref+=yr
        else:
            pref+='null'
        pref+=');\n'
        out.append(pref);
    out.append('commit;')
    with open('./books.sql', 'w', encoding='utf-8') as outfile: 
        outfile.writelines(out)