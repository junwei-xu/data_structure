# 数据结构与算法基础（python描述）
## github地址
[地址](https://github.com/junwei-xu/data_structure.git)
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
  ![image](https://img-blog.csdnimg.cn/img_convert/0d895dca5b4d62cdbeaab938355419d0.png)
* 实现  
  内置的list和tuple是采用分离式技术实现的动态顺序表  
  ![image](https://img-blog.csdnimg.cn/img_convert/1e69dffb9f9c753481a1cc1ff8264fbe.png)
## 链表

### 单链表

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/6aa934548f59c4de41935e9300500982.png)
* 实现  
![image](https://img-blog.csdnimg.cn/img_convert/5de9e04dcb9db4273c99f6a3efe33af2.png)
### 双链表

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/e259b09a5532e287eea3bcf628e533da.png)
* 注意  
  任意位置插入的实现
  ![image](https://img-blog.csdnimg.cn/img_convert/f03b9e5363f31197b3ec3c4e93ac87b2.png)
* 实现  
![image](https://img-blog.csdnimg.cn/img_convert/71a0df2fc2350bf68010025d1a9c7cc1.png)
### 单向循环链表

* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/0bc4e7c952abe96ace8ffa6bdf240b69.png)
* 注意  
  判断尾结点为 --> cur.next != self.__head
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/505356239a656d42ffe1b6ac50f9dd70.png)
## 栈

* 形式   
  ![image](https://img-blog.csdnimg.cn/img_convert/5992fee0aefd469e51acf7a177caffc1.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/338a1e821ae8fe23dbbdb1536fe0ce0d.png)
## 队列

### 基础队列

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/983da6e8ac09d7f5ebf60b566a3f6840.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/9f2c3ed1043d61cec200d38873c7723e.png)
### 双端队列

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/72ebdcd827cdbe9392dc2ee377bc7ec6.png)
* 注意  
  双端队列两头都可以出入，front入队和rear出队需要额外判断此时的front、rear指针位置
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/b3b5c869addeec0da432cba886762f82.png)
### 循环队列

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/eda156a407adb9df497403ac21f4f872.png)
* 注意  
  rear/front从0开始计数，相当于留一个空间 队列空： front = rear   
  队列满： (rear+1) % MaxSize = front --> 此时实际还留有一个空间，以避免与队空标志冲突   
  队列长度计算： length = (rear-front+MaxSize) % MaxSize
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/fd77f7f8003331724f637f26185d9497.png)
## 二叉树

* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/1586f8420362d3b541baf0c823fa381b.png)
* 实现构建
![image](https://img-blog.csdnimg.cn/img_convert/faeb6ba2e3fd49954381f73036ff0576.png)
* 实现四种遍历&反转
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210602222432495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTg5MDczNA==,size_16,color_FFFFFF,t_70)

## 排序

### 冒泡排序

* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/ccaf323ec1f80a8279aee8fe36930e1a.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/ff311b66152474283368e13460e9fa96.png)
### 选择排序

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/387d0da36b11c051dde181944f44d021.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/c578d94795925159de0e488fa6429391.png)
### 插入排序

* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/00d2819ac144db0d29ccde8795e7f990.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/957884e8f8706439504af70532b0d774.png)
### 快速排序

* 基本步骤
    1. 选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素。这个过程称之为 partition
    2. 对这两个子数组进行快速排序
    3. 合并结果
* 形式
  ![image](https://img-blog.csdnimg.cn/img_convert/bd9a883a6415f84a8ba30470453d05dc.png)
  ![image](https://img-blog.csdnimg.cn/img_convert/2898b134d255d0a81666f1634224c69e.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/a9982acbf02ffcd704c3cf0fabaf5099.png)
### 希尔排序

* 概念   
  把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；  
  随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/726a23e05049165be33e7795450b5dba.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/f803ccae97a2de3420be74d145b8d654.png)
### 归并排序

* 分治法步骤
    1. 分解：将待排序的 n 个元素分成各包含 n/2 个元素的子序列
    2. 解决：使用归并排序递归排序两个子序列
    3. 合并：合并两个已经排序的子序列以产生已排序的答案
* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/228cb1b7e51bc02c5f459fc16b7962ac.png)  
  ![image](https://img-blog.csdnimg.cn/img_convert/d6647bc174921770d0198d8d0efe7627.png)
* 实现
![image](https://img-blog.csdnimg.cn/img_convert/781d77a28fad6669a84d9b4a4c375a2e.png)
### 比较

![image](https://img-blog.csdnimg.cn/img_convert/d9cd5a9a2244b4cebea3d679734c0b05.png)

## 查找

### 二分查找

* 递归实现
![image](https://img-blog.csdnimg.cn/img_convert/7c2ff4df13ffbce2e78d4a9ea4b6d6aa.png)
### 二叉查找树

* 特征
    1. 所有key小于V的都被存储在V的左子树
    2. 所有key大于V的都存储在V的右子树
* 形式  
  ![image](https://img-blog.csdnimg.cn/img_convert/6a103d2f689247cddd9842b8855f0a95.png)

