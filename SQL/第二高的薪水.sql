# 编写一个 SQL 查询，获取 Employee表中第二高的薪水（Salary）。
#
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+

select ifnull( # 判断空值
               (select distinct Salary # 记得去重
                from Employee
                order by Salary DESC
                limit 1 offset 1), null # offset跳过1
           ) as SecondHighestSalary