# CheckContentView

用于检查 iOS 项目中，自定义的 UITableviewCell、UICollectionViewCell 中子视图没有添加到 ContentView 的脚本，支持 OC、Swift

#### 实现思路

##### 首先确定哪些类是  UITableviewCell、UICollectionViewCell 

在 OC 语言的项目中，同时存在 h&m 文件，确定是什么类的时候，只需要打开 h文件就可以，同时校验是否继承自   UITableviewCell、UICollectionViewCell 

即符合 ：UITableviewCell、UICollectionViewCell  这样的语法结构

##### 确定没有添加到 ContentView 上

正常添加到 ContentView 上的语法规则是 self.contentView addSubview，如果调用的是 self addSubview 就是没有添加到 ContentView 上，由此确定



