# 查询所有分都大于80分的学生姓名
select distinct name
from student
where name not in (select distinct name from grade where score <= 80);

SELECT name
FROM student
GROUP BY name
HAVING MIN(score) > 80;

# 查询平均分大于80的学生的姓名
SELECT name
FROM (SELECT COUNT(*) AS t, SUM(score) AS num, name FROM grade GROUP BY name) AS a
WHERE a.num > 80 * t;

SELECT name, AVG(score) AS sc
FROM grade g1
GROUP BY name
HAVING AVG(score) > 80;