# Physical Layer
## 理论基础
### 傅里叶分析
数字信号 -> 模拟信号
$g(t) = \frac{1}{2}c + \sum^{\infin}_{n=1}a_nsin(2\pi nft) + \sum^{\infin}_{n=1}b_ncos(2\pi nft)$
### Bandwidth-limited signals
#### 调制解调
- 调制encode: 把数字信号转换为模拟信号
- 解调decode: 把模拟信号转换为数字信号
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

#### 信道限制
即便信号传输很快，但是也会受到信道(传输介质)的制约，也可能发挥不了信号的性能
![](./ref//note2-1.png)
这里用了电话线举例，最高只能传输3000Hz
因为数据传输率bps太高的话，根据傅里叶变换，较高频率的谐波过不去，因此只有低频率的谐传输就不准确
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

![](./ref/note2-2.png)
低频段比较繁忙拥挤，因为成本比较低
高频段用于医疗、航空

- 无线电传输
- 微波传输
- 红外传输
- 光通信
频带的概念

## Communication Satellite
- Geostationary Satellites(地球同步卫星)
- Medium-Earth Orbit Satellites(中地球轨道卫星)
- Low-Earch Orbit Satellites(低地球卫星)
- Satellites Versus Fiber

同样是低频段拥挤，成本低
高频段昂贵，并且容易受到干扰(天气...)

round-trip往返旅程delay time双倍

## 数字调制和多路复用（Digital Modulation and Multiplexing）
将比特转换为联系变化的模拟信号即为数字调制

- Baseband Transmission基带传输
  - 信号传输占有传输介质上从零到最大值之间的全部频率，最大频率取决于信令速率
  - 有衔接之普遍使用
  - ![](./ref/note2-3.png)
- Passband Transmission通带传输
  - 信号战屡以载波信号频率为中心的一段频带
  - 无线和光纤信道常用
  - ![](./ref/note2-4.png)
- **Frequncy Division Multiplexing频分**
  - 将频谱分成几个频段，每个用户完全拥有其中一个频段来发送自己的信号
  - ![](./ref/note2-5.png)
- **Time Division Multiplexing时分**
  - 用户以循环的方式轮流工作，周期性地获得整个带宽非常短的一段时间
  - ![](./ref/note2-6.png)
- **Code Division Multiplexing码分**
  - 大家都在这个信道上通信，类似正交编码的方式，每个用户需要一个正交码经过一系列的数学运算提取自己要的信息

## 公共电话交换网络
上下行不对称，因为看的信息和上传的信息不一样多

路由器存储转发

电路/分组交换

某一个发生故障对整体的影响
按顺序否