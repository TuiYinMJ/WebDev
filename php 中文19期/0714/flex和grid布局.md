# flex 布局

## 基本概念

- 弹性容器：拥有 display:flex/inline-flex 属性的元素
- 弹性项目：弹性容器的子元素
- 主轴：弹性项目排列时的参考轴线，有水平和垂直
- 交叉轴：与主轴垂直的布局参考线

## flex 容器属性

- display
- flex-flow：下面属性的简写
  - flex-direction：设置主轴方向，row 和 column
  - flex-wrap：设置项目是否换行
- place-content：容器在主轴剩余空间上项目之间进行分配
  - start
  - end
  - center
  - space-between 项目间距相等两端对齐
  - space-around 项目间距相等分散对齐
  - space-evenly 项目间距均匀分布
- place-item：项目在交叉轴上的对齐方式
  - start
  - end
  - center
  - stretch 项目拉伸占据剩余空间

## flex 项目属性

- flex: 放大因子 收缩因子 计算宽度

```css
/* 默认flex 不让放大 允许收缩 width */
flex: 1 1 auto; 允许放大和缩小
flex: 2 1 auto; 放大两倍 允许收缩
flex: 0 1 auto; 不允许放大 允许收缩
flex: 0 0 auto; 不允许放大 不允许收缩 失去弹性
```

- order，数值越小越靠前显示，默认是 0

# grid 布局

## 基础术语

- 容器：grid 容器，display:grid;
- 项目：容器子元素

```css
display: grid;
/* 模板列 */
/* grid-template-columns: 10em 10em 10em; */
/* grid-template-columns: repeat(3,10em); */
grid-template-columns: repeat(3, 1fr);
/* fr平分n等份 */
/* 模板行 */
/* grid-template-rows: 10em 10em 10em; */
/* grid-template-rows: repeat(3,10em); */
grid-template-rows: repeat(3, 1fr);
```

若超过画的网格，则会出现在隐式网格中

- grid-auto-rows:100px; 设置隐式网格
- grid-auto-flow:row; 设置隐式网格的排列方向
  - column
- gap:垂直间隙 水平间隙，行与列的间隙

用于子元素：

- grid-row:1/2;默认放的位置
- grid-column:1/2;默认放的位置

```css
grid-row: 1 / span 2;
/* 从1开始 跨2格 */
grid-column: 1 / span 2;
/* 从1开始 跨2格 */
```

- grid-area:行开始/列开始/行结束/列结束
  - 设置单元格的区域，也可以在结束上用 span 跨行
