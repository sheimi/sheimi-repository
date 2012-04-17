Software Design
===============

Chapter 0
---------

### What have we learned before

#### About Softwaer Design

+   The essential concepts
+   Technologies and methods
+   Notations
+   设计模式  设计理论，模块化，信息隐藏
+   设计模型  类图，行为图，部署图，构建图，
+   三层次    代码设计，中层，体系结构

###Course Outline

+   软件设计要素
+   设计结构设计
+   详细设计
+   大型软件初步
+   设计演化（重构）
+   软件设计的支持和评价


Chapter 1
---------

### Main Contents

+   What is Design
+   What is software design
+   Basics of Design Process

#### What is Design

+   [link](http://en.wikipedia.org/wiki/Design)
+   Design is the planning
+   applied arts and engineering
+   to design == develop a plan

#### What is software design

Software design is the activity of specifying the mature and composition
of software products that satisfy client needs and desire, subject to
constrants

consider the *aesthetic*, *functional* and ...

the aesthetic of design

+   简洁性：模块化和信息隐藏
+   一致性（概念完整性）：体系结构的风格
+   坚固（高质量）：最重要的是体现在体系结构上，设计模式所要解决的问题

审美考虑

+   用软件功能解决用户的问题是需求分析的价值
+   准则1：用“美”的方式实现功能，是设计的价值

设计的难度

+   事物的复杂性 VS 思维的有限性
  -   7 +- 2
  -   关注点分离与层次性（设计的关注点）
+   事物的复杂度 VS 载体的复杂度
  -   准则2：设计复杂度 = 事物复杂度 + 载体与事物失配(适配?)复杂度
      比如说数据库
  -   准则3：设计注重内部结构而不是外部表现
+   准则4：只有高层次设计良好，底层设计才可能良好：先需求分析、后体系结构、详细设计、编码：
  +   高层设计的质量需要到最底层才能准确验证
  +   。。。
  +   测试就是评价各个设计的质量
+   准则5：只有写完并测试代码之后，才能算是完成了设计！
+   Product Design: RE
+   Engineering Design Low/Mid/High:SE
...


#### Basic of Design Process 

设计方案，约束，需求，环境，资源，技术。。。

满足与决策，选择性，顺序影响，不可逆

Chapter 2
---------

### 设计的层次

+   低层设计：代码设计 (关注把有限的语言的类型变成无穷的ADT)
+   中层设计：模块与类设计 （减少片段间的依赖，====> 完全独立）
+   高层设计：体系结构设计

#### 底层设计：代码设计

+   1950s
  +   第一代语言：硬件问题，指令的指令码太多了
  +   第二代语言：对于一些存储的处理，寄存器，逻辑
+   1960s
  +   第三代语言：类型与函数：第一次复杂系统分割，对于局部的类型。。。，促进了复用。问题：类型的有限性，算法的有限性，隔离了OS
  +   都是用编译器来解决
+   1970s
  +   函数与类型的成熟：形式化方法
  +   数据结构 + 算法 = 程序
+   底层设计（原始类型 + 算法 => 抽象数据类型）
+   质量：数据结构合理医用，算法可靠、高效、易读
+   屏蔽数据结构和算法的实现细节
+   抽象层，结构层 / 精华层，实现层
+   代码设计
  +   犯法和函数内部代码进行设计
  +   常见设计
+   内部结构：算法和数据类型的组合，外部：抽象类型

#### 中层设计：模块与类的设计

+   程序的分割
  +   1970s：模块
  +   1980s：OO
  +   模块，模块化，信息隐藏，面向对象，原则、模式
+   模块划分
  +   掩盖内部结构，提供抽象和接口
+   模块化
  +   评价（简洁性，可观察性）
  +   目标：完全独立性（理解、使用和复用，开发，修改），可是不可能完全独立
  +   方法：实现尽可能独立（低耦合，高内聚）
  +   模块与对象间的联系
      -   调用(2)
          *   Data Coupling
          *   Stamp Coupling
          *   Control Coupling
          *   Content Coupling(Hybrid of data and control elements)
      -   共享参数(N - 1) ^ 2
      -   继承
      -   组合（聚合）
      -   依赖，重载
      -   Common Environmen: (Principle 1: Global Variables Consider Harmful)
      -   Information Cohesion (From module to object)
      -   Connection to other modules (explicit, ...)(Principle 2: To bve Explicit)
      -   业务逻辑的重复，简单代码的重复
      -   变量访问
  +   联系的要素
      -   度数（多少个参与联系），内部的复杂
      -   接口，内部，接口最好
      -   传递信息的复杂度，需要
      -   理解所需的信息度，越少越好
  +   Cohesiveness
      -   Coincident Binding
      -   Logic Binding: Binding by Similarity of Logic
      -   Temp.. 
      -   Procedure Binding by the same time
      -   Communicational Binding: Binding by the same Data
      -   Sequential Binding: Binding by the same problem
      -   Functional Binding: Binding by the same goal （修改的相同性）（Goal: 满足用户的一条需求）（问题：有可能修改不是由用户发起的，不是由需求带来的）
  +   Four Kinds of Component coupling
      -   Whole variable
      -   ...
      -   ...
      -   ...
  +   The worst coupling: Implicit
  +   The law of Demeter
      -   You can play with yourself
      -   You can play with your own toys 
      -   ...
      -   ...
  +   Inheritance Coupling(LSP)Liskov Substitution Principle 
      -   Modifying without and rules and restricts(BAD GUY)
      -   Refinement Inheritance Coupling
      -   Extension Inheritance Coupling
  +   Principles from Modularization
      -   Global Variables Consider Harmful
      -   To be Explicit
      -   Do not Repeat
      -   Programming to Interface
      -   Design by Contract


信息隐藏

+   模块化方法1： 按照处理流程，每个功能一个模块
+   模块化方法2： 信息隐藏，Each module has one or more "secrets"，需求
+   每个模块实现了一个重要的决策，需求内部发生变化，需求的实现发生变化
  +   需求
  +   变化
  +   例子，策略模式（需求，针对需求的实现，两个secret，需要单独下来）（针对单个行为是多变的）
  +   OCP，Extend is superior to modify，Extension：坚固性，Modify：简洁性
  +   准则：每个最基础的模块只有一个secret
  +   准则：每个secret只位于一个最基础的模块
  +   准则：secret需要被隐藏
+   模块化 = 按功能设计
  +   ...
+   信息隐藏 = 模块化 + 可修改性
  +   给出功能接口，隐藏功能实现的细节
  +   ...
+   为每一个模块书写一个规格说明书
  +   模块承担的功能
  +   对外接口
  +   主要秘密(模块需求决策 0 ~ N)，来源于需求规格说明
  +   次要秘密 来源于可修改性
+   controll违反面象对象，层次比其他对象高
+   创建对象的时候的if else 是没有办法避免的，它没有多多态
+   多态，运行时注册，dll（替换）。。。

理想的对象

+   耦合
  +   内部耦
+   单一职责

...


体系结构
--------

### 为什么要高层设计

+   Programming in the Small
+   名称匹配, 导入导出（问题）
  +   Inside 接口（独立，区别对待）
+   详细设计的不足
  +   载体失配(适配?)（无法描述可靠性，性能）
  +   无法实现交互信息本地化（信息隐藏的局限性），Inside
  +   无法有效抽象部件的整体特性
  +   接口定义缺乏结构性（交互的规则，如果A调用是B必须调用）
  +   不能有效适应大型软件的特殊开发方法

### Programming in the large

+   载体复杂度过大
+   超出导入导出的关系
+   需要从根本上超越导入导出
+   不考虑导入到处，名字匹配
+   Module Itself with Quality  property -> Component
+   interactions of Component -> Connector
  +   Structure
  +   None(Programming Mechanisms) implementation Considerations
+   Configuration 
+   SA (内部：模块、进程、物理、网络节点，外部：功能、质量，考虑 Conponent, Connector, Configuration)
  +   模块 -> OO -> 方法片段(DS + AG)
+   Components are the locus of computation and state
+   Connectors are the locus of relations among components
  +   Connector deserve first-class
+   概要设计（意识)   SAD（方法学：关键：Connector）
+   Abstract specivication vs implementation 

#### Component

+   Elements that encpsulate processing and data in a system's architecture are refered to as software components
+   A software component is an architectural entity that
  +   ...
  +   ...
  +   ...
+   Port 
  +   Reqired Interface
  +   provide... Interface
  +   rules
  +   property
+   ACME（体系结构的语言）

#### Connector

+   role(ruls property provide require interface)
+   Primitive connectors
  +   Procedure Call
  +   Shared variable
  +   Message
  +   Pipe
  +   Event
  +   ...
+   Explicit connectors
  +   Adaptor
  +   Intermediate
  +   intermediate

#### Configuration

+   an ...
+   Provided interface >= Required Interface


