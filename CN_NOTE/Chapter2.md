# Physical Layer
## 理论基础
### 傅里叶分析
数字信号 -> 模拟信号
$g(t) = \frac{1}{2}c + \sum^{\infin}_{n=1}a_nsin(2\pi nft) + \sum^{\infin}_{n=1}b_ncos(2\pi nft)$
### Bandwidth-limited signals
#### 调制解调
- 调制: 把数字信号转换为模拟信号
- 解调: 把模拟信号转换为数字信号
#### 波特率
每秒钟传送波形的数量/波特率表示单位时间内传送的码元符号的个数
#### 码元
在使用时间域(时域)的波形表示数字信号时，代表不同离散数值的基本波形
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
- 磁介质
- 双绞线
- 同轴电缆
- 电力线
- 光纤

## 无线传输
- 电磁频谱
- 无线电传输
- 微波传输
- 红外传输
- 光通信
频带的概念