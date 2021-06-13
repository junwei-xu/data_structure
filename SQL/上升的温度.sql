# 编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 id 。
#
# 返回结果 不要求顺序 。
#
# 查询结果格式如下例：
#
# Weather
# +----+------------+-------------+
# | id | recordDate | Temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+
#
# Result table:
# +----+
# | id |
# +----+
# | 2  |
# | 4  |
# +----+
# 2015-01-02 的温度比前一天高（10 -> 25）
# 2015-01-04 的温度比前一天高（20 -> 30）

select w1.id as id
from Weather w1
         inner join Weather w2
                    on DateDiff(w1.recordDate, w2.recordDate) = 1  # DateDiff为mysql内置函数，返回两个日期之间的天数
where w1.Temperature > w2.Temperature