# 有一个courses 表 ，有: student (学生) 和 class (课程)。
#
# 请列出所有超过或等于5名学生的课。
#
# 例如，表：
#
# +---------+------------+
# | student | class      |
# +---------+------------+
# | A       | Math       |
# | B       | English    |
# | C       | Math       |
# | D       | Biology    |
# | E       | Math       |
# | F       | Computer   |
# | G       | Math       |
# | H       | Math       |
# | I       | Math       |
# +---------+------------+
# 应该输出:
#
# +---------+
# | class   |
# +---------+
# | Math    |
# +---------+
#  
#
# 提示：
#
# 学生在每个课中不应被重复计算。

select class
from courses
group by class
having count(distinct student) >= 5;
# 注意distinct -> 题目中一个学生可以选两门一样的课

# 子查询 比较复杂
SELECT class
FROM (SELECT class,
             COUNT(DISTINCT student) AS num
      FROM courses
      GROUP BY class) AS temp_table
WHERE num >= 5;
