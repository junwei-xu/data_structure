# 数据结构基础（python描述）

## 复杂度

* 时间复杂度O(n)
    1. 基本操作，即只有常数项，认为其时间复杂度为O(1)
    2. 顺序结构，时间复杂度按**加法**进行计算
    3. 循环结构，时间复杂度按**乘法**进行计算
    4. 分支结构，时间复杂度取最大值
* 空间复杂度S(n)  
  对一个算法在运行过程中临时占用存储空间大小的量度

## 顺序表

* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.2sv66ag87m00.png)
* 实现  
  内置的list和tuple是采用分离式技术实现的动态顺序表

## 链表

### 单链表

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.5iykzlwi3b40.png)

### 双链表

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.6kisesyehys0.png)
* 注意  
  任意位置插入的实现
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.16fe0xi00j5s.png)

### 单向循环链表

* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.1horkmeeznpc.png)
* 注意  
  判断尾结点为 --> cur.next != self.__head
* 实现

## 栈

* 形式   
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.7fh0a7awgq80.png)
* 实现

## 队列

### 基础队列

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.1mm3l279s85c.png)
* 实现

### 双端队列

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.1bvj2r6t4i1s.png)
* 注意  
  双端队列两头都可以出入，front入队和rear出队需要额外判断此时的front、rear指针位置
* 实现

### 循环队列

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.6nq6synsflg0.png)
* 注意  
  rear/front从0开始计数，相当于留一个空间 队列空： front = rear   
  队列满： (rear+1) % MaxSize = front --> 此时实际还留有一个空间，以避免与队空标志冲突   
  队列长度计算： length = (rear-front+MaxSize) % MaxSize
* 实现

## 二叉树

* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.4twul6qljwg0.png)

## 排序

### 冒泡排序

* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.2u7imhd6w1c0.png)

### 选择排序

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.3k0fd328o080.png)

### 插入排序

* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.7hywljfqqdo0.png)

### 快速排序

* 基本步骤
    1. 选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素。这个过程称之为 partition
    2. 对这两个子数组进行快速排序
    3. 合并结果
* 形式
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.75ht7ap2cu00.png)
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.8uubryfpgb4.png)

### 希尔排序

* 概念   
  把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；  
  随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.3weylhhuwgc0.png)

### 归并排序

* 分治法步骤
    1. 分解：将待排序的 n 个元素分成各包含 n/2 个元素的子序列
    2. 解决：使用归并排序递归排序两个子序列
    3. 合并：合并两个已经排序的子序列以产生已排序的答案
* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.74jn6utmyso0.png)  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.232r5qm4x8jk.png)

### 比较

![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.2j4qkm7swz60.png)

## 查找

### 二分查找

* 递归实现

### 二叉查找树

* 特征
    1. 所有key小于V的都被存储在V的左子树
    2. 所有key大于V的都存储在V的右子树
* 形式  
  ![image](https://cdn.jsdelivr.net/gh/junwei-xu/image-hosting@master/20210515/image.5pmqitdydyc0.png)

