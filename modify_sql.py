# 将 my_movies.sql 中的 "public.my_movies" 替换为 "my_movies" 并输出到 my_movies2.sql

print('Start modifying sql file...')
with open('my_movies.sql', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # 每输出1000行，打印一次
    with open('my_movies2.sql', 'w', encoding='utf-8') as f2:
        cnt = 0
        for line in lines:
            f2.write(line.replace('public.my_movies', 'my_movies'))
            cnt += 1
            if cnt % 1000 == 0:
                print(f'{cnt} lines have been modified.')