1.5
什么是分组交换，为什么因特网与分组交换有关？
分组交换把数据划分成许多小的数据块（分组），并在每个分组中加进目标接受方的标识信息。遍布网络的所有交换设备都保存有分组如何抵达所有可能目的地的有关信息。当一个分组到达任一个交换设备时，该设备就会选择一条路径，分组沿着这条路径被最终传送到正确的目的地。
分组交换从根本上改变了联网方法，并奠定了线代因特网的基础————分组交换允许多个通信方通过一个共享的网络传送数据，而不是形成一条条专用的通信线路。
1.10
描述TCP/IP的分层模型，并解释改模型是如何提出的。
共分为五层，自下而上分别为：物理层、网络接口层、网络互连层、传输层和应用层。
第一层：物理层
物理层协议规定底层传输介质和相关硬件的细节。与电气特性、无线电频率和信号等有关的所有规范，都属于第一层。
第二层：网络接口层或MAC
媒体访问控制MAC层中的协议规定了单一网络间的通信以及网络硬件与第三层间的接口（通常通过软件来实现）的相关细节。有关网络地址、网络可支持的最大分组长度、用于接入底层介质的协议以及硬件寻址等方面的规范，都属于第二层。
第三层：网络互连层
网络互连层协议是因特网最重要的基础。第三层协议规定两台计算机通过因特网（即通过多个互联网络）进行通信的细节。因特网编址结构、因特网分组格式、将大分组划分成为小分组的方法以及差错报告机制等，都属于第三层。
第四层：传输层
传输层协议为一台计算机上的应用程序跟另一条计算机上的应用程序之间提供通信手段。接收端最大可接受数据速率的控制、避免网络拥塞的机制、确保所有数据以正确顺序接收的技术等规范，都属于第四层。
第五层：应用层
应用层是TCP/IP协议栈的最高层，该层协议规定一对应用进程在她们通信的时候如何交互作用。这层协议还规定有关应用进程所交换的消息含义和格式，本质上，当一个程序员开发穿越网络通信的应用程序时，就将涉及第五个协议。电子邮件交换、文件传输、Web浏览、电话服务、智能手机应用和视频会议等方面的规范，都属于第五层。
TCP/IP分层模型的提出是为了提高系统的可维护性、灵活性和互操作性并为了确保所形成的的通信系统是完整的和有效的。这个模型的思想受到OSI（Open Systems Interconnection）模型的启发，但TCP/IP模型更加简单实用。TCP/IP模型的发展是在ARPANET项目中进行的，该项目是美国国防部高级研究计划局（ARPA）在20世纪60年代末和70年代初进行的，是互联网的前身。
5.3
数据通信的概念模型包括哪些构成部分？
信息源：信息源（有时简称信源）既可以是模拟的也可以是数字的，其重要概念包括各种信号特征（如振幅、频率和相位）。可划分为周期的（有规律地出现）或非周期的（无规律地出现）。而且，信息的模拟与数字表示之间的转换是这个子课题的关注焦点。
信源编码器和解码器：一旦信息被数字化后，就可以对其数字表示进行转换或变换，其重要概念包括数据压缩和通信效果。
加密器和解密器：为了保护信息不被窃密，信息可以在传输前先加密，在接收后再解密，其重要概念包括加密技术和算法。
信道编码器和解码器：信道编码是用来检测和纠正传输错误的，其重要的概念包括检测和限制差错的方法，以及十几种可采用的技术（例如在计算机网络中使用的奇偶校验、校验以及循环冗余等）。
多路复用器和解复用器：复用指多个信源同时在共享截止上传输信息的方式，其重要概念包括多信源轮流使用介质的同步共享技术等。
调制器和解调器：调制指信息发送时把需要传输的数据转化为相应的电磁信号，其概念包括模拟和数字调制的技术方案及其设备。实施调制和解调的设备称为调制解调器(Modem)。
物理信道与传输：包括传输介质和传输模式，其重要概念包括带宽、电磁噪声、干扰和信道容量以及传输模式（如串行传输和并行传输）等。
6.7
对一个复合波进行傅里叶分析会产生什么？
会分解成一组频率、振幅、和相位不同正弦函数。如果复合信号是周期性的，其组成部分也是周期性的。
6.17
在曼彻斯特编码中使用信号的什么特征来表示码位？
使用电平的跳变来表示码位，电压从0V到一个正电压的跳变来对应于逻辑1，电压从某个电压值到0V的跳变对应于逻辑0.
6.20
如果人耳可听到的最高频率是20 000Hz，那么对麦克风产生的模拟信号进行数字化转换时，其采样率必须是多少？
由奈奎斯特定理：$采样率 = 2 \times f_{max}$,其中$f_{max}$是复合信号中的最高频率。本题中最高频率$f=20,000Hz$，那么$采样率=2 \times 20000=40000Hz$
7.3
当噪声遇到金属物体时会发生什么现象？
由于金属可以吸收辐射，所以它可起屏蔽作用。因此，如果噪声遇到金属物体会被吸收，噪声减小。
7.17
请列举三种类型的通信卫星，并分别说明每一种的特征。
低地球轨道（LEO）：
优点：低时延
缺点：从地球的观察视角，卫星在天空中不断移动
中地球轨道（MEO）：
轨道为椭圆形（而非圆形），主要用于提供南北两极的通信
地球静止轨道（GEO）：
优点：相对于地球表面某一位置，卫星保持在固定方位
缺点：距离遥远
8.4
码字是什么？在前向纠错中如何使用码字？
码字是由一组二进制位组成的序列，通常用来表示一段信息。这段信息可以是文本、图像、声音等任何形式的数据。每个二进制位被称为一个比特，而一组比特构成了一个码字。
在前向纠错中，码字被用于增强通信系统的可靠性。前向纠错的目标是在发送端引入冗余信息（通过添加纠错码）以便在接收端检测和纠正错误，而无需进行重发请求。
具体来说，在前向纠错中如何使用码字涉及到使用一定数量的冗余比特，通过某种纠错码算法将这些冗余比特添加到原始数据中，形成一个扩展的码字。这个扩展的码字包含了原始信息和冗余信息。在接收端，如果发生了一些错误，通过纠错码的算法，可以尽可能地检测和纠正这些错误，以还原原始信息。
8.15
请做出10010101010除以10101的除法计算。
$\qquad\qquad\qquad\  111000$
$\ \ 10101 \mid \overline{10010101010}$
$\qquad\qquad\ \underline{10101}$
$\qquad\qquad\ 100000$
$\qquad\qquad\ \ \ \underline{10101}$
$\qquad\qquad\ \quad 10111$
$\qquad\qquad\ \quad \underline{10101}$
$\qquad\qquad\ \ \ \qquad 10010$
由此，结果为111000余10010
9.4
异步传输的主要特征是什么？
异步传输：数据项的传输可以在任意时间开始，两组数据项之间的间隔时长也可以是任意的。异步传输的缺点是发送器和接收器之间缺少协调——当介质空闲时，接收器不知道在新的数据到来之前，介质还会空闲多长时间。
9.6
开始位是什么？其用于哪种类型的串行传输？
RS-232规定发送器在发送一个字符的比特之前要先发送一个额外的0比特，成为开始位。开始位用于异步串行传输。
9.8
当两个人进行对话时，他们是使用单工、半双工还是全双工传输？
当两个人进行对话时，通常使用全双工传输。在全双工通信中，双方都可以同时发送和接收信息，就像电话对话一样。每个人都能在同一时间既说话又听取对方的回应，实现了双向的即时通信。
相比之下，单工通信只能在一个方向上传输信息，类似于广播电台，其中信息只能从一个方向发送。而半双工通信允许双方交替地进行发送和接收，但不能同时进行。典型的半双工通信例子是对讲机，其中一方说话时另一方需要等待。
在对话中，全双工通信是最自然和常见的方式，因为它允许实现更接近面对面交流的体验。
10.1
列举模拟调制的三种基本类型。
模拟调制是一种将模拟信号转换为适合传输的信号的过程。有三种基本类型的模拟调制：

1. **幅度调制：**
   - **原理：** 在幅度调制中，载波的振幅被调制，以便传送模拟信号的信息。调制后的信号的振幅随着模拟信号的变化而变化。
   - **应用：** 幅度调制常用于广播和短波通信，其中调制后的信号可以在接收端进行解调以还原原始模拟信号。

2. **频率调制：**
   - **原理：** 在频率调制中，载波的频率被调制，以便传送模拟信号的信息。调制后的信号的频率随着模拟信号的变化而变化。
   - **应用：** 频率调制常用于广播、无线电通信和音频传输等领域。FM信号的抗干扰性相对较好，因此在某些应用中更受青睐。

3. **移动位调制：**
   - **原理：** 在相位调制中，载波的相位被调制，以便传送模拟信号的信息。调制后的信号的相位随着模拟信号的变化而变化。
   - **应用：** 相位调制通常用于通信系统和雷达等领域。它在某些情况下对于抗噪声和保持信号质量有一定的优势。

11.12
假设N个用户竞争使用统计TDM系统，并且假设下层物理传输每秒可以发送K比特，一个单独用户可以体验到的最低数据速率和最高数据速率分别是什么？
在统计时分多路复用系统中，N个用户竞争使用，每秒可以发送K比特的情况下，一个单独用户可以体验到的最低数据速率和最高数据速率可以通过统计的方法来估算。

假设总的传输时间周期为T秒，每个用户在这个时间周期内被分配一个时间槽进行数据传输。用户的数据速率取决于其分配到的时间槽大小。

1. **最低数据速率：**
   - 最低数据速率发生在所有用户都在同一时刻竞争使用，因此每个用户分配到的时间槽可能很小。
   - 最低数据速率可以通过以下公式估算：\[ \text{最低数据速率} = \frac{K}{N} \] 这里，\(K\)是总的传输速率，\(N\)是用户的数量。

2. **最高数据速率：**
   - 最高数据速率发生在每个用户都能独占整个传输时间周期，即每个用户都在不与其他用户竞争的情况下传输数据。
   - 最高数据速率可以通过以下公式估算：\[ \text{最高数据速率} = K \]

12.1
什么是接入技术？
因特网接入技术是指链接因特网用户（一般是私人住户和商业机构）和因特网服务提供商（例如电话公司或电缆公司）的数据通信系统。
12.2
服务提供商为什么要区分上行与下行通信？
服务提供商之所以需要区分上行（Upstream）和下行（Downstream）通信，主要是因为这两个方向的通信在网络架构和资源管理上有不同的需求和特点。区分上行和下行通信有助于更有效地设计和优化网络，提高服务质量和性能。以下是一些主要的原因：

1. **不对称的带宽需求：** 上行和下行通信往往有不同的带宽需求。在许多应用场景中，用户通常下载（下行）的数据量远远超过上传（上行）的数据量。通过区分上行和下行通信，服务提供商可以更好地分配和优化网络带宽资源，以满足用户的实际需求。

2. **不同的服务质量需求：** 一些应用可能对上行通信的延迟更为敏感，而另一些应用可能更依赖于下行通信的稳定性。通过区分上行和下行通信，服务提供商可以为不同方向的通信提供不同的服务质量（QoS），以满足各种应用的特定要求。

3. **安全性和管理：** 区分上行和下行通信有助于提高网络的安全性和管理效率。例如，防火墙和安全策略可以分别应用于上行和下行流量，以增强网络的安全性。此外，监测和管理网络性能时，可以分别考虑上行和下行的指标，更好地定位和解决问题。

4. **服务提供商的业务模型：** 一些服务提供商可能基于不同的业务模型来提供上行和下行通信服务。例如，家庭宽带服务通常更强调下行速度，而企业服务可能更关注上行带宽。

12.7 *
住在同一条街上的两个邻居，都使用ADSL服务，不过测量结果表明一个用户可用大约1.5Mb/s的速率下载，而另一个用户却可以2Mb/s的速率下载。请解释原因。
ADSL的下行速率是自适应的，具有一个有趣的性质：ADSL不保证数据速率。事实上，ADSL只能保证在线路条件允许下尽量运行良好。居住地离交换局较远或本地环路要通过干扰源附近的用户，往往体验到较低的数据速率；而居住地离交换局较近以及本地环路不经过干扰源附近的用户，则体验到较高的数据速率。因此，下行速率在32kb/s到8.8448Mb/s之间变化，也就出现了同一条街上的两个邻居的下载速率不一样的现象。
13.3
在分组交换系统中，发送方如何发送一个大的文件？

在分组交换系统中，发送一个大文件通常会涉及到将大文件切分成较小的数据包，然后逐个发送这些数据包。这个过程涉及到分割、传输、和重新组装数据包的步骤。

1. **分割文件：** 发送方首先将大文件分割成适当大小的数据包。这通常是为了确保每个数据包都可以在网络上有效地传输，而不会引起过多的数据包碎片和传输延迟。

2. **添加头部信息：** 对于每个数据包，发送方会添加一些头部信息，这些信息包括源地址、目标地址、数据包编号等。这些信息有助于确保数据包在网络中被正确地传输和重新组装。

3. **传输数据包：** 发送方将这些数据包发送到网络中。这可能涉及到使用传输层协议（如TCP或UDP）来确保可靠的传输。

4. **接收方接收数据包：** 接收方负责接收发送方发送的数据包。

5. **重新组装文件：** 接收方在接收完所有数据包后，将这些数据包按照正确的顺序重新组装成原始的大文件。

6. **检验完整性：** 为了确保传输的文件完整无缺，接收方通常会对接收到的数据进行校验，例如使用校验和或哈希值，以验证数据包的完整性。

总之，在分组交换系统中发送大文件的关键是将文件切分成适当大小的数据包，并确保这些数据包按照正确的顺序到达接收方。这样的方法有助于提高传输的效率和可靠性。
13.8
4种基本的LAN拓扑是什么？
1. **总线拓扑**
   用单根电缆将所有计算机连接起来，任何连接到总线上的计算机都能发送信号到总线上，并且所有计算机都能接收到这个信号。由于所有计算机直接连接在电缆上，因此任何一台计算机都能向其他计算机发送数据。当然，连接在总线网络上的计算机必须相互协调，以保证在任何时候只有一台计算机发送信号。某些总线网络安排计算机连接到一个小设备，且总线存在于设备内部。
2. **环形拓扑**
   把计算机连接成一个封闭的圆环————一根电缆连接第一台计算机与第二台计算机，另一根电缆连接第二台计算机与第三台，以此类推，知道一根电缆连接最后一台计算机与第一台计算机。使用环形拓扑的有些技术要求计算机连接到一个小型设备上，在设备内部构成环。这样做的有点是：计时某些计算机断开了连接，而环路本身仍然有能力继续运行。实际中，环形网络中的电缆并不形成一个圆圈，而是可以顺着过道或垂直地从大楼的一层到另一层，可以有任意的走向。
3. **网状拓扑**
   使用网状拓扑的网络在每一对计算机之间提供直接连接。网状拓扑的主要缺点在于费用问题————连接n台九三级的网状网络要求
   $网状网络中的连接数=\frac{n!}{(n-2)!2!}=\frac{n^2-n}{2}$
   最重要的是：网状网络所需的连接数的增长速度远快于计算机数目的增长速度。由于连接费用昂贵，很少有LAN会采用网状拓扑结构。
4. **星形拓扑**
   所有计算机都连接到一个中心节点（集线器），典型的集线器从发送的计算机接收数据，然后再把数据转发到合适的目标计算机。
   实际中星形网络很少会使集线器位于与所有计算机相同距离的地方而呈对称形状的。相反，集线器通常安放在于所连九三级相分离的地方，例如计算机在各自的办公室里，而集线器却安放在单位网络管理员容易接近的地方。
13.11
给定一个IEEE的MAC地址，我们如何才能判定它是不是一个单播地址？
48位IEEE的MAC地址的前3字节为机构唯一标识符（OUI），OUI中最高有效字节的2个低阶位已经分配了特殊的含义，其中的最低位是一个多播位，用来规定它是一个单播地址（0）还是一个多播地址（1）。
因此，如果给定的IEEE MAC地址的最高有效字节的最低比特位为0，则可以确定它是一个单播地址。
13.12
试定义单播、多播和广播地址，并解释它们的含义。
单播、多播和广播是用于数据传输的不同寻址方式，它们有着不同的含义和应用场景：

1. **单播地址（Unicast Address）：**
   - **定义：** 单播是指从一个主机发送数据到另一个特定的主机的通信方式。源主机将数据发送到目标主机的唯一标识符，通常是目标主机的IP地址。
   - **含义：** 单播通信是一对一的通信，只有特定目标主机能够接收并处理发送的数据。

2. **多播地址（Multicast Address）：**
   - **定义：** 多播是指从一个主机发送数据到一组特定的主机的通信方式。源主机将数据发送到一个多播组的标识符，多个主机可以加入该组以接收数据。
   - **含义：** 多播通信是一对多的通信，数据只被那些加入了多播组的主机接收。这种方式有效地减少了网络流量，适用于需要同时将数据发送给多个接收者的场景，比如视频流或在线会议。

3. **广播地址（Broadcast Address）：**
   - **定义：** 广播是指从一个主机发送数据到网络中的所有主机的通信方式。源主机将数据发送到广播地址，所有连接到网络的主机都能够接收并处理这个数据包。
   - **含义：** 广播通信是一对全部的通信，所有主机都能够接收发送的数据。广播通常用于一些需要将数据发送到整个网络的情况，但由于广播会导致网络中所有主机都处理这个数据包，因此使用广播应当谨慎，以免产生不必要的网络流量。

13.15
试给出术语帧的定义。

一个帧由两个概念部分组成：
- 包含元数据（如地址）的头部
- 包含发送数据的载荷

帧的头部包含一些用来处理帧的信息。特别是头部通常包含一个地址来指定期望的接收方。载荷域包含要发送的报文，并且它通常比帧头部大很多。在大多数网络技术中，网络只检查帧头部，在这个意义下，报文是不透明的。因此，载荷区可以包含任何只对发送和接收有意义的字节序列。
通常安排帧的头部在前、载荷在后传输，因为这样可以使接收方在帧头部比特到达时就开始处理帧。有一些技术通过在帧前面发送一小段前导码，在帧后面发送一小段后接码来勾画帧的完整性。
14.8
写出缩写CSMA/CD的全称，并解释每一部分的含义。
CSMA/CD的全称是“Carrier Sense Multiple Access with Collision Detection”，其中各部分的含义如下：

1. **CSMA（Carrier Sense Multiple Access）：**
   - **含义：** CSMA是一种多路访问协议，它通过监听网络上的载波（Carrier）来感知是否有其他设备正在发送数据。在CSMA中，设备在发送数据之前会先检测信道上是否有其他信号，如果信道被占用，则设备会等待一段随机的时间再次尝试发送。

2. **CD（Collision Detection）：**
   - **含义：** CD表示冲突检测。在CSMA/CD中，如果两个设备几乎同时开始发送数据，它们的信号可能会在中途相遇，造成数据碰撞。为了检测到这种碰撞，发送数据的设备会继续发送一个短的冲突检测信号，以便在碰撞发生时及时发现，并采取相应的重传机制。

综合起来，CSMA/CD是一种在共享传输介质（如以太网）上使用的协议，它允许多个设备共享同一个通信通道，但同时要求设备在发送数据之前先监听信道，以避免碰撞，并在发生碰撞时能够及时检测到并进行处理。
14.11
为什么在无线网络上需要采用CSMA/CA?

在无线网络中，采用了CSMA/CA（Carrier Sense Multiple Access with Collision Avoidance）协议，而不是CSMA/CD协议，原因如下：

1. **无线信道特性：** 无线信道是共享的，不像有线传输介质那样可以简单地检测碰撞。当一个设备发送信号时，其他设备可能会在同一时间尝试发送数据，导致碰撞。由于无线信道上的碰撞检测复杂且不可靠，CSMA/CA引入了“避免（Collision Avoidance）”的概念，以降低碰撞的发生概率。

2. **<h5>隐藏终端问题：** 无线网络中存在"隐藏终端"问题，即在传输范围内的两个设备可能无法感知彼此的存在。如果两个设备同时尝试发送数据到同一个接收设备，而彼此之间无法感知，可能导致碰撞。CSMA/CA通过引入网络协调机制，如RTS/CTS（请求发送/清除发送），来避免隐藏终端问题。

3. **冲突避免：** CSMA/CA通过在发送数据前进行随机等待的方式，以及使用退避算法，来减少碰撞的概率。在有线网络中，碰撞可以被可靠地检测和处理，但在无线网络中，避免碰撞更为重要。

4. **信道质量不稳定：** 无线信道的质量可能随时间和环境变化，因此在数据传输前进行先导信号、等待和清理过程，有助于适应不断变化的信道条件，提高网络性能。

综上所述，CSMA/CA在无线网络中是为了应对无线信道的特殊性而设计的，通过避免碰撞、解决隐藏终端问题和适应信道质量的不稳定性，提高了无线网络的性能和可靠性。
15.4
接收方如何知道一个以太网帧使用的是802.3标准？
如果以太网帧中的第13~14字节包含的数值小于1500，那么这个域可以解释为分组的长度并适用802.3标准；否则，改域被解释为一个类型域并适用原始以太网标准。
15.6
一台计算机如何连接到粗缆以太网？
粗缆以太网也称粗网，它适用的硬件分成两个主要的部分：**网络接口卡NIC**处理通信的数字方面，以及一种称为**收发器**的独立电子设备连接在以太网电缆上，处理载波信号检测、把位串转换成适合传输的相应的电平、把传入的信号转换成位串。
并且一种称为**附属单元接口（AUI）**的物理电缆把收发器链接到计算机的NIC上
16.1
举出三种无线PAN技术的名称，并简要描述每种技术。

1. **蓝牙：** 小型外围设备（诸如耳机或鼠标）与系统（诸如手机或计算机）之间的短距离通信
2. **红外：** 小型设备（经常为手持控制器）与邻近系统（诸如计算机或娱乐中心）之间的视线通信
1. **ZigBee：** 能覆盖约一个住宅范围的通信，使得家里电器考科一连接到智能电网

16.4
给出用于Wi-Fi网络的IEEE标准的数值前缀。

IEEE标准中用于Wi-Fi网络的数值前缀主要涉及到802.11系列标准。以下是几个常见的IEEE标准及其数值前缀：

1. **802.11a**：Wi-Fi的第一个标准，支持5 GHz频段，并提供最高54 Mbps的数据传输速率。
2. **802.11b**：支持2.4 GHz频段，并提供最高11 Mbps的数据传输速率。
3. **802.11g**：支持2.4 GHz频段，并提供最高54 Mbps的数据传输速率。
4. **802.11n**：支持2.4 GHz和5 GHz频段，并提供最高600 Mbps的数据传输速率。
5. **802.11ac**：支持5 GHz频段，并提供最高1 Gbps的数据传输速率。
6. **802.11ax**：也称为Wi-Fi 6，支持2.4 GHz和5 GHz频段，并提供更高的数据传输速率和更好的性能。

16.8
为什么大部分无线LAN采用基础结构型方案而不采用Ad hoc方案？
大部分无线局域网络（WLAN）采用基础结构型方案而不是 Ad hoc 方案的主要原因有几点：

1. **中央控制和管理：** 基础结构型方案使用无线接入点（AP）作为中央控制节点，负责管理网络中的设备。这种集中管理的方法使得网络配置、维护和安全性更加容易。管理员可以通过配置和管理单个接入点来控制整个网络，而不需要在每个设备上进行独立配置。

2. **更好的网络组织：** 在基础结构型网络中，无线设备连接到接入点，形成一个有序的网络拓扑结构。这有助于更好地组织和优化数据流量，提高网络的性能和稳定性。Ad hoc 网络没有中心化的管理，设备之间直接通信，可能导致网络拓扑不稳定和性能下降。

3. **安全性：** 基础结构型网络通常提供更高级别的安全性，因为管理员可以通过配置接入点来实施各种安全协议和机制。这使得更容易实施访问控制、加密和其他安全策略。相比之下，Ad hoc 网络可能更容易受到各种安全威胁，因为它们通常缺乏集中的安全管理机制。

4. **易于扩展：** 基础结构型网络更容易扩展和升级。通过添加更多的接入点或升级现有的接入点，可以改善网络容量和覆盖范围。Ad hoc 网络在设备数量增加时可能更难管理，因为每个设备都需要直接与其他设备通信，导致复杂度增加。

虽然 Ad hoc 网络在某些场景下可能很有用，例如在没有基础设施支持的情况下快速建立网络连接，但在大多数企业和家庭 WLAN 的情况下，基础结构型网络更为常见和可靠。
17.3
如果两台计算机连接在一个桥接网络上，地址或应用需要改变吗？请解释。

当两台计算机连接在一个桥接网络上时，通常情况下它们的地址和应用不需要改变。以下是解释：

1. **地址不需要改变：** 桥接网络是在数据链路层（第二层）操作的，它通过学习和转发数据帧来连接多个局域网。在桥接网络中，每台计算机仍然保留其原有的网络地址（如IP地址），因为桥接设备只负责将数据帧从一个局域网转发到另一个局域网，而不修改数据帧的源或目的地址。

2. **应用不需要改变：** 应用程序通常运行在网络协议栈的更高层，如传输层（第四层）或应用层。桥接网络在数据链路层工作，对上层的应用程序没有直接的影响。因此，连接在桥接网络上的计算机可以继续运行其原有的应用程序，并使用相同的网络应用协议（如HTTP、FTP等）进行通信。

需要注意的是，如果两个局域网之间存在不同的网络地址空间，例如使用不同的IP地址段，那么在桥接网络中进行通信时，可能需要进行一些配置调整，例如设置适当的子网掩码或路由规则，以确保跨越桥接网络的通信能够正确地路由和转发。但这并不涉及修改计算机的地址或应用，而是对网络设备的配置进行调整。
17.7
在网上搜索生成树算法的描述，然后编写一个模拟网桥形成生成树的计算机程序。
生成树算法通常用于网络中的桥接设备，例如在以太网中形成生成树协议（STP，Spanning Tree Protocol）的生成树。这个协议确保在网络中没有循环，同时保持冗余路径，以提高网络的可用性。下面是一个简单的Python代码示例，演示了生成树算法的一部分，假设存在一组连接在网络上的交换机：

```python
class Switch:
    def __init__(self, name):
        self.name = name
        self.connected_switches = {}  # 连接的交换机及其链路的字典

    def add_connection(self, switch, cost):
        self.connected_switches[switch] = cost
        switch.connected_switches[self] = cost

def generate_spanning_tree(root_switch, parent=None, visited=None):
    if visited is None:
        visited = set()

    print(f"Switch {root_switch.name} is in the spanning tree.")

    visited.add(root_switch)

    for neighbor, cost in root_switch.connected_switches.items():
        if neighbor not in visited and (parent is None or neighbor != parent):
            generate_spanning_tree(neighbor, root_switch, visited)

# 创建一组交换机
switch_a = Switch("A")
switch_b = Switch("B")
switch_c = Switch("C")
switch_d = Switch("D")
switch_e = Switch("E")

# 连接这些交换机
switch_a.add_connection(switch_b, 1)
switch_a.add_connection(switch_c, 2)
switch_b.add_connection(switch_d, 3)
switch_c.add_connection(switch_d, 1)
switch_c.add_connection(switch_e, 2)
switch_d.add_connection(switch_e, 1)

# 以交换机A为根节点生成生成树
generate_spanning_tree(switch_a)
```

这个简单的模拟演示了生成树算法的核心思想。在实际的网络中，生成树协议通常使用更复杂的算法来确保冗余路径的可用性，同时避免网络环路。在实际应用中，你可能会使用网络模拟器或者实际的网络设备来测试和运行这样的算法。
17.11
根据下图，链接到一个交换式LAN中的两台计算机是否能同时传输分组？请解释。
![](17.11.png)
**可以同时传输分组。**

交换式LAN使用交换机来连接多个设备，每个设备都有自己的端口。交换机具有转发和过滤数据包的能力。当一台计算机发送数据包时，交换机会根据目标MAC地址将数据包定向转发到相应的端口，只有目标计算机的端口会接收到该数据包。

由于交换机具有并行转发数据包的能力，它可以同时处理多个数据包，使得连接到交换式LAN的多台计算机能够同时传输数据包。如果一台交换机有N个端口连接N台计算机，同一时间可以进行N/2个传输。这意味着两台计算机可以通过交换式LAN同时进行通信，而不会相互干扰。
18.10
动态路由有什么好处？

动态路由是一种网络路由的方式，其中路由表的更新和维护是自动进行的，而不需要手动配置。相比于静态路由，动态路由具有一些明显的好处：

1. **自动适应网络变化：** 动态路由协议能够自动感知网络拓扑的变化。当网络发生变化时，如链路故障或新的路由器加入，动态路由协议能够及时更新路由表，确保数据流量可以根据最新的网络状态进行正确的转发。

2. **减少人工配置：** 在大规模网络中，手动配置每个路由器的路由表是非常繁琐且容易出错的。使用动态路由可以减少人工配置的工作量，提高网络的可维护性。

3. **提高网络的可扩展性：** 动态路由协议能够适应网络规模的增长，而无需对每个路由器进行手动配置。这使得网络更容易扩展，而不会导致过多的人工管理和配置。

4. **支持负载均衡：** 一些动态路由协议支持负载均衡，可以在多条路径之间分配流量，以优化网络利用率。这对于大型网络和需要高可用性的应用非常重要。

5. **故障恢复：** 动态路由协议能够快速适应网络中的故障，重新计算并选择可用路径。这提高了网络的鲁棒性和可靠性，减少了对故障的影响。

6. **适应动态网络环境：** 在某些情况下，网络拓扑可能会经常变化，例如移动设备或无线网络。动态路由能够更好地适应这种动态的网络环境。

总体而言，动态路由在大多数情况下更适用于大型、复杂或经常变化的网络环境，因为它提供了更自动化、灵活和适应性更强的路由管理方式。
18.12
分布式路由计算的两种基本方法是什么？它们各自是如何工作的？
分布式路由计算的两种基本方法是**链路状态路由（Link State Router）和距离向量路由（Distance Vector Router）**。

1. **链路状态路由（LSR）**：其工作原理是每个路由器都会向网络中广播其邻居节点信息，包括链路状态、带宽、延迟等信息。通过收集到的网络拓扑信息，每台路由器可以计算出整个网络的最短路径并生成路由表。链路状态协议通常使用Dijkstra算法来计算最短路径。

链路状态协议的优点是路由器能够快速适应网络拓扑变化，可以准确地计算最短路径。但是，链路状态协议需要在整个网络中广播邻居节点信息，因此会产生较大的开销和网络流量。

1. **距离向量路由（DVR）**：其工作原理是每个路由器通过邻居节点发送的距离向量（即距离和下一跳路由器）信息来计算到其他节点的距离。每个路由器根据收到的距离向量信息更新自己的路由表，从而逐步推算出整个网络的路由表。

距离向量协议的优点是每个路由器只需要知道邻居节点的信息，因此开销相对较小。但是，距离向量协议容易受到诸如带宽瓶颈、网络拥塞等问题的影响，可能产生路由环路和计数问题。

二、综合题
假设有一栋五层楼的办公楼，进行双绞线网络布线，楼高4米，楼面分布如下图所示：
![](综合题题目.png)
走廊3米宽，各办公室宽4米，深5米，主机房设置在底楼OFFICE5内，每层楼的左边小间可以存放网络设备(临近OFFICE1)，并通过垂直干线穿线 。
进行布线设计，满足以下要求：
1. 每个办公室设置4个信息点；
2. 在每层楼支持无线接入。
3. 网络设备采用交换机。

请画出布线示意图。
布线设计需要考虑各个办公室的信息点、无线接入以及网络设备的位置。以下是可能的设计方案，仅供参考：

### 布线设计：

1. **信息点设置：**
   - 每个办公室设置4个信息点，分别布置在不同的墙壁或角落，以覆盖整个办公室。
   - 每个信息点连接到相应楼层的交换机。

2. **交换机位置：**
   - 主机房设置在底楼 OFFICE5 内，连接整个网络。
   - 在每个楼层的左边小间（临近 OFFICE1）放置交换机，以便更好地覆盖整个楼层。

3. **垂直干线穿线：**
   - 从主机房连接到每层楼的左边小间，通过垂直干线穿线将交换机连接到各个楼层。

4. **无线接入：**
   - 在每层楼的交换机上设置无线接入点（Wi-Fi路由器）。
   - 通过无线接入点提供覆盖整个楼层的无线网络。

5. **Hub 连接：**
   - 将主机房的交换机连接到位于底楼 OFFICE5 的 Hub。
   - Hub 连接到 OFFICE1 至 OFFICE8，形成整个楼宇的网络连接。

### 拓扑示意图：

```
          [Hub]
           / | \
   -------   |  -------
   |         |         |
[SW]      [AP]       [SW]  ... （每层楼）
   |         |         |
   -------   |  -------
           \ | /
          [SW]        (主机房内)

[SW]: 交换机
[AP]: 无线接入点
```

注意事项：
- 交换机数量和端口容量应根据每层楼的信息点数和设备数进行规划。
- 无线接入点的位置应考虑覆盖范围，以确保在办公室和走廊中都有良好的信号强度。
- 确保垂直干线穿线的可靠性和各个楼层的连通性。