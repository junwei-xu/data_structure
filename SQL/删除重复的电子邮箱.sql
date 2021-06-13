# 编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。
#
# +----+------------------+
# | Id | Email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Id 是这个表的主键。
# 例如，在运行你的查询语句之后，上面的 Person 表应返回以下几行:
#
# +----+------------------+
# | Id | Email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+

delete
from Person
where Id in
      (select temp.Id # temp表防止出现《You can't specify target table 'p1' for update in FROM clause》的错误
       from (select p1.Id
             from Person p1
                      inner join Person p2
                                 on p1.Email = p2.Email
             where p1.Id > p2.Id) as temp);

# 官方解法
DELETE p1
FROM Person p1,
     Person p2
WHERE p1.Email = p2.Email
  AND p1.Id > p2.Id