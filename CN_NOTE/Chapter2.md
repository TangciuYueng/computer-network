# Physical Layer
## 理论基础
### 傅里叶分析
### Bandwidth-limited signals
#### 波特率
每秒钟传送波形的数量/波特率表示单位时间内传送的码元符号的个数
#### 比特率
每秒钟传送bit的数量
#### 波特率和比特率关系
[知乎波特率和比特率](https://zhuanlan.zhihu.com/p/630588317)
码元状态数量为N，就需要$log_2N$个比特位表示
比特率 = 波特率$\times log_2N$
### Maximum data rate of a channel
#### Nyquist's Theorem
无噪声情况
任意一个信号通过了一个带宽为B的低通滤波器，只要进行每秒2B次的确切采样，就可以完全重构出被过滤的信号
如果信号包含了V个离散等级
最大数据速率 = 2B $log_2V$ (BIt/sec)
#### Shannon's formula for capacity of a noisy channel
带宽为B Hz，信噪比是S/N的有噪声信道，S为信号功率，N为噪声功率
最大比特率 = B $log_2(1 + \frac{S}{N})$
## 传输介质

## 无线传输
频带的概念