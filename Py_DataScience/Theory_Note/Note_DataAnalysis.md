# 1. 数据分析基础

```
一、数据特性
计量层次对数据进行分类
计量层次低：字段信息无法进行计算比较 如 书本 黄瓜 番茄 树木 牛
计量层次高：数据可以进行计量比较 如 1 2 3 4 5 6

定类数据：
（1）按照类别属性进行分类，各类别之间是平等并列关系
（2）这种数据不带数量信息，并且不能在各类别间进行排序
（3）主要数值运算，计算每一类别中的项目的频数和频率
如 颜色：红黄蓝  性别：男女
定序数据
1）各数据之间可以排序和比较优劣；
2）通过对文字编码进行排序，可表示彼此的高低差异
如 教育程度：小学 初中 高中 大学     季度：春夏秋冬     等级：合格 良好 优秀
定距数据
1）具有一定单位的实际测量值；
2）精确性比定类数据和定序数据更高；
3）可计算各变量之间的实际差距（加、减）
如 温度：33 21 9    年龄：30 93 24    成绩：50 70 80 
定比数据
1）可以比较大小，进行加减乘除运算；
2）定距尺度中，0表示数值，定比尺度中，0表示“没有”；如 (定距数据)温度
3）定比数据中存在绝对零点，定距数据中不存在。
如 利润: 10万 30万    薪酬：1000 3000 4000         用户数：230 3500 3000
定性数据（定类数据、定序数据）是一组表示事物性质、规定事物类别的文字表述型数据

定量数据（定距数据、定比数据）指以数量形式存在着的属性，并因此可以对其进行测量  
数据矩阵：属性 记录 
```



```
统计指标：体现总体数量特征的概念和数值，根据数据分析的目的不同，统计指标也会变化

1.总量指标：（GDP，总人口，销售总额）特定条件下的总规模、总水平或工作总量。是一种最基本的统计指标
2.平均指标：用一个数字显示其一般水平，集中趋势指标
3.相对指标：两个有联系的现象数值相比得到的比率，描述相对关系而不是总体
4.比例=各数据/总比%比率=数据项：数据项倍数 突出上升、增长幅度
5.环比增长率=（本期数-上期数）/上期数*100% 
  同比增长率=（本期数-同期数）/同期数*100% 
```



```
1. 平均数
2. 中位数 排序后中间的数值 区分奇数偶数2种情况
3. 众数 各个数值出现的次数 一般按照区间来划分
```



```
离散趋势

极差 min max的绝对值

平均差=|每个数据项的值-均值|的总和/数据项个数，数值小-离散小，但是异常值对其影响比较大（尤其是在样本量小的情况下）

标准差，放大离散程度  体现内部的离散程度   一般标准差是最常用的离散指标（股票、风控等）
```



```
分布形态：数据图表化后呈现出来的形态
平均值、中位数、众数----体现平均水平
极差、平均差、标准差-----体现一组数据样本          

高度----一般水平：均值
宽度-----离散程度    

正态分布：左右对称 ：身高、体重、天气、降雨量 （随着数据越多）
左偏分布（左高右低）：eg 考试成绩，死亡年龄、资产变化情况
右偏分布（右高左低）：eg 药物有效性、人类运动能力、财富分布  
```



```
判断异常值：

值/平均数 =倍数  根据倍数来观察是否存在异常值

异常值：与平均值偏差极大和极小的值，也叫做离群点；

处理异常值：

错误记录---修改正确
错误添加---删除
正确、真实---是否反映特殊事件---修改、调整或不做处理

错误数据---填充空值或填充样本平均值
正确、真实---根据实际情况调整（数值*需调整比率） 
```



![img](http://img.mukewang.com/climg/6048e2240001bc4e19201080.jpg)

```
数据分析的流程：

目标确定：描述性分析，预测性分析
数据获取：字段设计（平均销售额，销售总额，增减幅度），数据提取（销售管理软件，导入导出），互联网企业使用SQL从数据库提取

数据清洗：异常值的识别判定处理，空白值，无效值，重复值

数据整理：格式化（日期的处理，行列的格式化），指标计算（基础的计算，如平均值、总额）

描述分析：数据描述（数据的基本情况，数据总数，时间跨度，数据来源等），指标统计（分析实际情况的数据指标）。（变化、分别、对比、预测）

洞察结论：数据报告的核心，体现数据分析能力撰写报告 ：
报告背景，报告目的，数据基本情况，可视化图表，策略选择
```



---



# 3. 互联网数据分析框架



![image-20220323205501775](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220323205501775.png)



### 互联网商业模式 

***

##### 互联网简介：

- 基本特征： 连接，技术，价值
- 普及率：逐年稳步上升
- 行业格局：企业，服务类型

##### 产品分类：

- 服务对象：ToB (企业，社团，政府：理性，明确的指标，效率>体验)，ToC (个人用户：感性，功能设计突出，突出人性)
- 运营平台：移动，PC，智能设备 (iwatch, ipad)
- 用户需求：交易 (Taobao, JD)，社交 (Weibo)，工具 (jetbrains)，平台 (阿里巴巴，腾讯)，游戏，内容 (抖音)

---

##### 行业分析：

- 以行业为分析对象：具有高度相似性，竞争性
- 企业相互作用关系：竞争，合作，供应商，服务商
- 产业本身发展：市场规模，需求，增速，未来潜力
- 联系，区域分布：产业链上下游，国家和城市分布

###### 行业分析流程和方法：

确立目标 -> 收集资料 -> **结构化分析** (**总量，细分，预测，竞争关系 (波特五力法)**) -> 内容呈现

Z.B.: **直播电商**:

- 发展背景 (过去): (更多详细行业报告可以Google, Baidu)
  - 宏观：时间线，背景 (为什么兴起, 满足了什么需求) [参照 10.4-5]
  - 微观：整体成交额，用户规模，对比其他方式的占比 [参照 10.4-5]
- 竞争分析 : 
  - **波特五力法**：
    - 潜在新进入者：新平台 
    - 供应方议价能力 (品牌，经销商，工厂) [和KOL，主播成反比。小主播就只能给什么条件接什么条件]：**主播，平台**
    - 同业竞争：[内容平台和电商平台存在合作博弈关系]
      - 电商+直播 (淘宝，京东) 
      - 内容+电商 (小红书，抖音，快手)

    - 买方议价能力：消费者 (选择直播平台，需求，价格，信息不透明)
    - 潜在替代产品 [alternative]：线下零售，实体店，智能化服务，图文形式带货，粉丝经济
- 生态分析 :
  - 产业图谱：
    - (上下游公司和产品，整体规模趋势，市场数据表现，上游:广告商利润，中游:主播销售额，下游:人均消费额)
    - 如何梳理产业链：**供应商** -> **(MCN, 主播)** -> **渠道 [JD, PDD] 电商 内容[Bilibili, Tiktok] 社交 [Wechat]** -> **用户**
    - 产业链平台 (win.d), 数据服务平台 (**新榜newrank.cn** [平台数据], **itrustdata.cn** [数据服务提供商])
- 趋势预测 (未来):
  - PEST分析法：
    - Politics: 政策，监管，处罚
    - Economy: 宏观经济，资金，经济状况 -> 消费行为，口红效应 [基础消费品]
    - Society: 人口因素，消费心理，生活方式，文化传统 -> 年龄段，性价比，品质，消费升级，国货 [战狼]
    - Technology: 5G，AR，个性化推荐，智能手机普及 -> 沉浸式用户体验




### 数据指标体系

***

#### [数据指标模型]

#### 用户维度的分析模型：

##### 生命周期模型：用户接触到离开产品的过程

- 导入期：引导用户完成注册
- 成长期：体验行为
- 成熟期：依赖行为
- 休眠期：一段时间未登录
- 流失期：长时间未登录

##### AARRR模型 [自上而下]：从产品营销角度，实现用户管理

- Acquisition: 获取用户
- Activation: 提高用户活跃度
- Retention: 维持用户留存率
- Revenue: 获取收入
- Referral: 自传播

##### RARRA模型: (由AARRR转变而来)

- Retention: 维持用户留存率 **[最重要，有回头客，建立用户群]**
- Activation: 提高用户活跃度
- Referral: 自传播
- Revenue: 获取收入
- Acquisition: 获取用户

##### RFM模型 (CRM系统)：用户为分析维度，从消费行为的角度采取差异化营销策略

更加准确的衡量客户价值和客户创造利润的能力, 并执行对应的营销手段.

![image-20220406203346409](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220406203346409.png)



##### 5W2H：提问方式，快速掌握事件本质

Z.B. ：创建电商用户画像

- why: 运营活动，营销方案
- what: 用户画像是什么
- who: 年龄，性别，工作，婚姻
- when: 时间，频次，金额
- where: 分布地点，聚集性
- How: 行为轨迹，支付方式
- How much: 消费水平，价位

##### 逻辑树：(决策树) 一步步拆解问题，得出解决方案

- 确保考虑的完整性
- 避免重复思考
- 识别关键问题
- 大问题分解小问题

![image-20220407161637704](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407161637704.png)

![image-20220407162041754](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407162041754.png)



##### A/B测试模型：(多个方案时，使用分组测试来筛选和确定最终方案)

![image-20220407161954940](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407161954940.png)





#### 企业战略分析模型: 

##### SWOT: 帮助企业在商业环境中找准自身定位，并在次基础上制定决策

- Strengths [内部有利因素]: SO增长型战略，ST多样化战略
- Weakness [内部不利因素]: WT防御性战略，WO扭转型战略
- Opportunity [外部有利因素]: 
- Threat [外部不利因素]: 

![image-20220407172059422](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407172059422.png)

![image-20220407172135151](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407172135151.png)



##### PEST:

![image-20220407172336450](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407172336450.png)

##### 波特五力法：[更多可参考直播电商行业分析报告]

![image-20220407172446094](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220407172446094.png)





#### :facepunch: 数据分析指标体系：[11.4 - 11.9.xlsx] :punch:

- 有机组成的统计指标
- 依据行业，业务属性而定
- 以**AARRR**模型为线索：拉新指标，活跃指标，留存指标，转化指标，传播指标 **[参考11.4数据指标体系]**
  - 拉新指标 [**参与用户数，新增用户数，获客成本**]：·B.S. 拼多多红包裂变，转发好友机制实现促活和拉新
    - 线上，线下广告，应用商店优化，电子邮件推送，社交媒体传播，朋友推荐计划
  - 活跃指标：
    - 潜在用户真正使用产品
    - 流失率高达90%
    - 激活时刻：**行为 = （动力-阻力）*助推 + 奖励**
      - 行为：引导用户完成行为
      - 动力：需求强度
      - 阻力：完成行为需要的成本
      - 助推：提示用户完成行为
      - 奖励：完成行为后，用户得到的反馈
      - B.S.: 抖音: 直接刷视频，不需要注册登录，简化操作成本
  - 留存指标：
    - 提高留存率手段：
      - 产品核心价值
      - 满足用户需求：
        - 核心，延伸，需求触发，被动
        - B.S.: 支付宝
          - 核心：收付款
          - 延伸：余额宝，理财
          - 需求触发：app推送，短信提示
          - 被动需求：年度账单，蚂蚁森林
  - 转化指标 [变现]：
    - 免费用户付费
    - 变现模式：广告变现，增值服务 [VIP会员]，电商变现 [平台使用费，营销推广费]，直播变现，数据变现 [可视化，数据支持，解决方案]，游戏变现，金融变现 [金融产品，支付通道]，
    - 商业模式：低成本规模化获客，高效率持续发现
    - 引导用户付费
  - 传播指标：
    - 自传播：
      - **社交货币**： [评价对方的要素 (他穿AJ)，用户彰显自我的需求]
      - **诱因**：一谈到什么就能想到什么，形象的绑定
      - **情绪**：高唤醒，大量传播 [疫情消息]
      - **公共性**：销量，评价，好评 [从中心理]
      - **实用性**：奖励机制，拉新返现，送存储空间 [百度网盘]
      - **故事性**：好奇，沉浸式，意外
    - 病毒/口碑传播



### 构建用户画像

---

#### 用户画像：

- is what: 用一组标签 [用户属性，兴趣偏好] 来形容用户特征, 各类描述用户数据的变量合集
- 用户分群：品质生活优享，经济实用，数码狂热，某粉狂热
- ![image-20220408185050468](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220408185050468.png)
- 作用：
  - 精细化运营：
    - 对不同用户角色采用不同的营销手段
    - 新产品，中高端，定价高
  - 营销手段：
    - 个性化推荐：针对性推送
    - 广告投发系统：微信朋友圈，用户群
    - 活动营销：微信社群
    - 内容推荐：头条推荐算法，兴趣偏好



#### 数据标签系统：[12.2.xlsx 基于用户数据标签和用户画像对用户进行分组]

- 个性化短信推送：1.提升销售额 2. 老用户找回 3.短信推送 4.标签定位 5.推送规则 6. 提取用户

  7. 完成推送 8. 优化迭代

  ![image-20220409214231558](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220409214231558.png)

![image-20220409210941649](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220409210941649.png)



##### 数据埋点：一种数据采集的方式 => 管理，统计带参数的URL

- UTM (Urchin Traffic Monitor)，可以理解为流量监控器，用于帮助监控流量的来源，系列参数:
  - source: 请求来源，类似referrer
  - medium: 用来标记Banner、CPC等广告形式
  - term: 用来标记广告关键词，主要用于SEM [Search Engine Marketing] 投放
  - campaign: 用来标记广告或运营活动的整体的名称
  - content: 用于A/B测试，标记同一广告间细微差别
- ![image-20220409220436599](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220409220436599.png)



##### 构建用户画像：

- 如何构建用户画像：
  - 用户价值模型：最近消费时间，金额，频数
  - 内容偏好模型：分发机制，评论，点赞，收藏，交互行为
- 基础用户画像 **[12.4用户画像标签系统.xlsx]**：人口属性，用户行为，消费习惯，特征偏好
- 可视化工具：神策，GrowingIO 



##### 构建商品画像：

- 根据消费对象，构建商品标签
- 基础商品画像 **[12.6商品画像标签系统.xlsx]**:  价格，库存，销售，交互行为



#### 用户画像应用分析：

---

##### RFM模型：

- R, F, M 指标将用户分成8类.
- ![image-20220410185932303](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220410185932303.png)
- RFM模型具体应用实例：**[12.7RFM模型实例应用(K-Means).xlsx]** 
  - KMeans: 计算分段阈值
  - 设计客户类型：如上图

- 输出分析报告：**[12.15案例5：基于RFM的用户精细化管理.ppt]**







---

​	

# 4. 销售，市场与运营数据分析

### 网站流量：

- 如何获取流量：
  - 别人的渠道：付费渠道，合作渠道，搜索引擎
  - 自己的渠道：Bilibili, TikTok, 快手，视频，图文，活动
  - 病毒渠道：分享，转发，邀请好友
- 流量数据指标：
  - 站外营销推广指标：衡量不同渠道的效果
  - 网站流量：数量指标 :arrow_right: 站外到站内
  - 网站流量：质量指标 :arrow_right: 留存指标
  - 流量指标：**[13.2流量指标.xlsx]**
- 分析模型：
  - 流量波动检测模型：异常数据告警
  - 渠道特征聚类模型：对投放渠道归类和分析
  - 流量预测模型：基于历史数据预测 多少投放量才能完成KPI




### 广告引流聚类分析：

- 数据分析：**[Ad_Performance.py]**
- 数据预处理：
  - 计算，合并相关性 -> 避免聚类算法重复计算 夸大特征表现
    - data.corr()
    - 热力图呈现
    - data.drop(['column'], axios=1)
    - 两个相关性高的变量只保留一个
  - 标准化：***[标准化比较的维度，固定的值，统一的分析标准，规范不同规模和量纲的数据]***
    - Z-score: x' = (x-mean)/std
      - 中心化，正太分布 [均值为0，方差为1]，会改变原有数据的分布形态
    - Min-Max: x'=(x-min)/(max-min)
      - 数据进行线性变换，数据落入0-1的区间
    - MinMaxScaler()
    - Fit_transform(matrix)
  - 特征数字化 (One-Hot编码)：定类数据 [性别，职位，学历] 转为数值型数据，参与运算
    - 0和1 -> False ,True
    - OneHotEncoder(matrix)
  - 平均轮廓系数：确定最佳K值 s(i) = (b(i) - a(i) ) / max{a(i),b(i)}
    - KMeans.fit_predict()
    - Metrics.silhouette_score()
  - 聚类结果分析：**[Ad_Performance.py]**
- 可视化：雷达图 **[Ad_Performance.py]**



### 漏斗分析模型：

- 描述序列的环节与环节, 以及**关键节点**的转化程度, 有上下关系, 有步骤关系的模型
- 价值：***通过对转化的检测与优化提升转化效率***
- 应用场景：
  - 运营过程，效率：找到薄弱环节，针对性提升
  - ![image-20220423114044966](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423114044966.png)

- 识别用户行为特征
- ![image-20220423122532194](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423122532194.png)
- 分析关键节点转化效率 VS 用户体验
- ![image-20220423122736565](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423122736565.png)
- B.S.: 活动链接的邮件：
  - 邮件发送成功数
  - 邮件打开数
  - 网页链接点击数
  - 填写表单数
  - 提交表单数
  - 参与活动数

- ***实例：用户下单流程***
  - 点击率，流失率判断流量来源的质量是否过关
  - ![image-20220423132404352](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423132404352.png)
  - 落地页质量低的特点 :red_circle:
  - ![image-20220423132725755](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423132725755.png)
  - 转化率越高说明内容质量越好
  - ![image-20220423132915994](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423132915994.png)
  - 搜索点击率 > 200 才算健康   高级筛选(Tag)
  - ![image-20220423133139335](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423133139335.png)
  - ![image-20220423133445780](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423133445780.png)
  - ![image-20220423133527195](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423133527195.png)
  - ![image-20220423133602748](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423133602748.png)
  - ![image-20220423133704862](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220423133704862.png)

- 用EXCEL绘制漏斗模型图：**[13.18构建漏斗模型.xlsx]**



### 分析消费行为：

- 用户画像：
  - ![image-20220424171630679](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220424171630679.png)
- ***消费动机*** **(important)** 满足客户某种需求，生理或者心理：
  - ![image-20220424171817299](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220424171817299.png)
- 消费行为：
  - 购买次数，购买总金额，客单价，Recency etc.
  - ![image-20220424172026203](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220424172026203.png)
- 消费者行为模式随互联网的发展而变化：
  - 从被动接受，到主动出击 (搜索引擎)
  - interaction, share 用户之间相互传播



---

## 用户消费行为分析：

![image-20220424193612931](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220424193612931.png)



### 消费特征分析：

- 趋势分析：**[14.4趋势：时间序列, 14.5趋势：变量关系, 14.6趋势：时间偏好]**
  - ![image-20220425175217372](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220425175217372.png)
  - ![image-20220425175328582](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220425175328582.png)
  - ![image-20220425174628635](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220425174628635.png)
  
- 个体分析：**[14.7-14.8.ppt]**
  - ![image-20220426123535083](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220426123535083.png)
  
- 相关指标：
  - 人，货，场 **[营销推广类]**：
  
  - ![image-20220428164124341](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428164124341.png)
  
  - ![image-20220428164145208](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428164145208.png)
  
  - ![image-20220426143351768](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220426143351768.png)
  
  - ![image-20220428163110243](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428163110243.png)
  
  - ```mysql
    SELECT
    	yr,
    	mt,
    	COUNT(
    	IF
    		(
    			t1.orders > 1,
    			t1.orders,
    		NULL 
    		) 
    	) AS a,
    	COUNT( t1.orders ) AS b, COUNT(
    	IF
    		(
    			t1.orders > 1,
    			t1.orders,
    		NULL 
    		) 
    	) / COUNT( t1.orders )
    FROM
    	(
    	SELECT YEAR
    		( InvoiceDate ) AS yr,
    		MONTH ( InvoiceDate ) AS mt,
    		CustomerId,
    		COUNT( DISTINCT InvoiceNo ) AS orders 
    	FROM
    		OnlineRetail 
    	GROUP BY
    		YEAR ( InvoiceDate ),
    		MONTH ( InvoiceDate ),
    		CustomerId 
    	) AS t1 
    GROUP BY
    	yr,
    	mt;
    	(TIME,'%Y-%m')
    ```
  
  - ![image-20220428163128663](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428163128663.png)
  
  - ```mysql
    SELECT DATE_FORMAT(m1,'%Y-%m'),COUNT(m1),COUNT(m2),COUNT(m2)/COUNT(m1) FROM
    (SELECT CUSTOMERID,DATE_FORMAT(INVOICEDATE,'%Y-%m-01') as m1 FROM OnlineRetail 
    -- WHERE DATE_FORMAT(INVOICEDATE,'%Y-%m') = '2011-01'
    GROUP BY DATE_FORMAT(INVOICEDATE,'%Y-%m-01'),customerid) A 
    LEFT JOIN
    (SELECT CUSTOMERID,DATE_FORMAT(INVOICEDATE,'%Y-%m-01') as m2 FROM OnlineRetail 
    -- WHERE DATE_FORMAT(INVOICEDATE,'%Y-%m') = '2011-02'
    GROUP BY DATE_FORMAT(INVOICEDATE,'%Y-%m-01'),customerid) B 
    ON A.CUSTOMERID = B.CUSTOMERID
    AND m1 = DATE_SUB(m2,INTERVAL 1 MONTH)
    GROUP BY m1;
    ```
  
    



### 用户分层与质量分析：

- ![image-20220428163159489](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428163159489.png)

- ```mysql
  SELECT 
  SUM(SALES)/9769872 AS '消费占比',
  COUNT(us)/4372 AS '用户占比',
  SUM(SALES)/COUNT(us) AS '客单价' FROM
  (SELECT CUSTOMERID AS us,ROUND(SUM(UNITPRICE * QUANTITY),2) AS SALES
  FROM OnlineRetail WHERE CustomerID IS NOT NULL 
  GROUP BY CUSTOMERID 
  ORDER BY SUM(UNITPRICE * QUANTITY) DESC LIMIT 874) T1;
  -- 判断质量较低的xxx个用户他们的总消费金额/总消费金额(80%的用户贡献了20%销售额)SELECT 
  
  SELECT SUM(SALES)/9769872 AS '消费占比',
  COUNT(us)/4372 AS '用户占比',
  SUM(SALES)/COUNT(us) AS '客单价' FROM
  (SELECT CUSTOMERID AS us,ROUND(SUM(UNITPRICE * QUANTITY),2) AS SALES
  FROM OnlineRetail WHERE CustomerID IS NOT NULL
  AND QUANTITY>0
  GROUP BY CUSTOMERID 
  ORDER BY SUM(UNITPRICE * QUANTITY) LIMIT 3000) T1;
  ```

- ![image-20220428163217134](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428163217134.png)

- ```mysql
  SELECT CustomerID, AVG(gap) as 平均购买周期 FROM(
  select CustomerID,time1,time2 ,datediff(time1,time2) AS gap 
  from(
  select
  CustomerID,
  InvoiceNo,
  InvoiceDate as time1,
  -- ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY InvoiceDate) AS rank1,
  LAG(InvoiceDate,1) OVER(PARTITION BY CustomerID) AS time2 --获取时间窗口，上下N行
  from OnlineRetail 
  WHERE CustomerID is not NULL
  GROUP BY InvoiceNo,CustomerID,InvoiceDate)a)b
  GROUP BY CustomerID HAVING AVG(gap) >0
  ORDER BY AVG(gap); 
  ```



---



# 预测销售额、调整运营策略

### GMV(销售额): 

- 设定企业与各部门KPI指标，并以此为目的分配资源

- ![image-20220428165033789](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428165033789.png)
- ![image-20220428165234374](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428165234374.png)
- **拆解GMV：**
- ![image-20220428171412827](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220428171412827.png)



### GMV预测模型：

- Excel: 数据建立图标，插入多项式回归；
- Python回归分析：**[predictive_model.py]**
  - ![image-20220501185824945](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220501185824945.png)
  - 多项式回归模型：LinearRegression(), coef_, intercept_
  - 可视化：趋势线，预测销售额
  - 输出预测报告：**[案例9：预测2020天猫双11销售额.pptx]**





### 商品分析：

- 基于商品基础数据，销售数据，选品，销售，库存，市场，促销活动
- ![image-20220502104406534](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220502104406534.png)
- **商品常用指标：**
  - ![image-20220502104553489](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220502104553489.png)
  - ![image-20220502104832377](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220502104832377.png)
  - ![image-20220502104907327](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220502104907327.png)
- **层次分析法AHP：**
  - 应用场景：![image-20220503155745136](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503155745136.png)
  - **构建层次结构：**![image-20220503160213458](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503160213458.png)
  - **构建对比矩阵：** **[15.12成对比较矩阵.xlsx]**
  - **方案判断矩阵：** **[15.13方案判断矩阵.xlsx]**
  - **计算权重得分：** **[15.14总得分.xlsx]**




### 运营策略分析：

- **运营**：以用户为中心，通过各种方式拉新，促活，提升留存与价值，以满足转化目标的一切行为活动
  - 红包车：骑车发红包，达成用户增长，转化以及单车调配的目的
  - ***基于业务需要设计采集的指标***
- 如何策划一场运营活动：
  - ![image-20220503191151379](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503191151379.png)
  - ![image-20220503191431637](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503191431637.png)
  - ![image-20220503191525845](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503191525845.png)
  - ![image-20220503191708870](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220503191708870.png)






---



# 基于数据驱动迭代产品设计

### 数据产品经理职能：

![image-20220505160443033](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220505160443033.png)



### 促活，提升用户留存：

- B.S.:大众点评：
  - 普通会员，特殊会员：提供等级成长机制，等级越高，能获得更多优惠，更多实惠.
  
- **用户活跃度分析模型 RFE：**
  - **Recency:** 最近一次
  - **Frequency:** 频率
  - **Engagements (深度):** 浏览时间，商品数，播放，点赞，转发
  
- RFE实例分析：**[16.3练习：RFE模型.xlsx]**

- **用户存留，价值分析：**
  - **Aha Moment**: 让用户第一时间发现产品的核心价值，提升用户留存率
  
  - B.S.: Weibo，新用户自动关注up，自动加载资讯让用户进行交互
  
  - 步骤：
    - 提出假设：列举新用户可能出现的行为
      - ![image-20220505182439302](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220505182439302.png)
    - 分组验证：验证每个行为对留存率的影响
      - ![image-20220505182707451](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220505182707451.png)
    - 设计优化：对关键因素进行优化设计
      - ![image-20220505182818657](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220505182818657.png)
    - 因果测试：持续监测，明确关系
      - ![image-20220505182917627](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220505182917627.png)
    
  - 用户留存率计算实例：3天，7天，10天，30天，60天，看消费日期 - 首次消费日期的结果落在哪一个区间 **[16.5练习：计算留存率.xlsx]**
  
    - ```mysql
      select InvoiceNo as '订单号', 
      CustomerID as '用户ID',time1 as '消费日期',time2 AS '首次消费日期',
      datediff(time1,time2)gap from(
      select
      CustomerID,
      InvoiceNo,
      InvoiceDate as time1,
      ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY InvoiceDate) AS rank1,
      FIRST_VALUE(InvoiceDate) OVER(PARTITION BY CustomerID ORDER BY InvoiceDate) AS time2
      from OnlineRetail 
      WHERE CustomerID is not NULL
      GROUP BY InvoiceNo,CustomerID,InvoiceDate)a;
      ```
  
    - **通过时间间隔，计算留存率：**
  
  - 用户生命周期计算实例：最后一次消费日期 - 第一次消费日期 **[16.6练习：计算用户生命周期.xlsx]**
  
  - 案例分析PPT：**[案例8：基于电商的用户消费行为分析.xlsx]**





### AB测试与功能迭代：

- AB测试基本流程：
  - 分析现状，建立假设：分析业务，确定优先级最高的地方，作出假设，提出优化建议
  - 设定观测指标：
  - 设计与开发：
  - 确定测试时长：
  - 确定分流方案：
  - 采集分析数据：
  - 确定方案，迭代优化：
- 假设检验：
  - 假设：H0原假设
  - 验证：H1备择假设
  - P值：判定假设检验结果的一个参数，具有一定主观性，阈值为0.05
  - 实例：**[ABtest_action.py]** **[案例13：网站主页改版.pptx]**
    - CTR(点击率)差异分布，正态分布 => H1-H0 >1, p值= 0.006



### 异常数据检测：

- 基于**孤立森林算法** **(IsolationForrest)**的异常检测：
  - 利用随机性和特征表现进行划分
  - 实例：**[Exception_Detection.py]**
    - IsolationForrest(), decision_function()[获取数据点的得分]
    - **随机森林 (Random Forrest)** 是有监督学习，**孤立森林**是无监督学习





### 撰写数据报告：

- ![image-20220509114344847](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509114344847.png)
- ![image-20220509114407283](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509114407283.png)
- ![image-20220509114502593](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509114502593.png)
- ![image-20220509114542235](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509114542235.png)
- ![image-20220509114804196](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509114804196.png)
- ![image-20220509115146045](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509115146045.png)

![image-20220509115208152](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509115208152.png)

![image-20220509115248497](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509115248497.png)

![image-20220509115402035](C:\Users\xu\AppData\Roaming\Typora\typora-user-images\image-20220509115402035.png)





### 演讲技巧：

- **听众是谁** => 他们想听什么
- **怎么讲** => 通俗易懂，实操性强，注重互动
- **准备讲稿** => 大纲，逐字稿，测试演练









