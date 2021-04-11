> 2021届全国物联网设计大赛
>
> ![image-20210411155729528](/home/qdl/.config/Typora/typora-user-images/image-20210411155729528.png)



> **报名链接**

- http://iot.sjtu.edu.cn/show.aspx?info_lb=36&info_id=2812&flag=2





## 实验环境

> **硬件支持**

- HiLens Kit 多模态AI开发套件

多模态AI开发套件，支持通过端云协同实现图像、视频、语音等多种数据分析与推理计算，可广泛用于智能监控、智慧家庭、AI教育、智慧工业、智慧门店等应用场景。

购买链接：https://account.huaweicloud.com/usercenter/?region=cn-north-4#/ordercenter/hardware?cloudServiceType=hws.service.type.hilenskit&resourceType=hws.resource.type.hilens.kit



> **软件支持**

- **HiLens Studio（一个Web无需下载）**

```
登录华为HiLens管理控制台，在左侧导航栏中选择**“技能开发 > HiLens Studio”。弹出“HiLens Studio公测版本升级”对话框。
```





> **开发文档**

- 华为Hilens：
	- https://support.huaweicloud.com/usermanual-hilens/hilens_02_0102.html
- 控制台：
	- https://console.huaweicloud.com/hilens/?region=cn-north-4&locale=zh-cn#/dashboard
- 华为ModelArts：
	- https://support.huaweicloud.com/productdesc-modelarts/modelarts_01_0001.html





## 基本流程

| 流程           | 说明                                                         | 详细指导                                                     |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 连接端侧和云侧 | 首先，连接您购买的HiLens Kit，并将HiLens Kit注册到华为HiLens平台，连接端侧与云侧。 | [HiLens Kit注册流程](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0048.html)[智能边缘系统注册设备](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0051.html)[使用SSH注册设备](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0081.html) |
| 开发技能       | 使用HiLens Studio开发技能，开发者可以新建技能项目，在HiLens Studio编写和调试技能代码，针对HDMI输出的技能，在HiLens Studio中还可以运行技能并查看输出数据。 | [开发模型](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0025.html)[新建技能项目](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0087.html)[导入/转换本地开发模型](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0098.html)[编写/调试逻辑代码](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0088.html) |
| 安装技能       | 在HiLens Studio中编辑完技能代码，可以直接把技能安装到设备上。 | [安装技能](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0090.html) |
| 启动技能       | 把技能安装至设备后，可以直接在HiLens Studio中启动技能，查看技能运行效果。 | [启动或停止技能](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0091.html) |
| 发布技能       | 针对已经调试好的技能，可以在HiLens Studio中发布技能至华为HiLens平台技能市场，供其他用户使用。 | [发布技能](https://support.huaweicloud.com/usermanual-hilens/hilens_02_0089.html) |