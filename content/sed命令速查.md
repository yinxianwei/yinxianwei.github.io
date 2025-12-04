Title: sed 命令中文速查手册
Date: 2025-12-04

## 基础语法

```bash
sed [选项] '命令' 文件名
sed [选项] -f 脚本文件 文件名
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `-n` | 安静模式,仅显示经过sed处理的行 |
| `-e` | 执行多个sed命令 |
| `-f` | 从文件中读取sed命令 |
| `-i` | 直接修改文件内容(不加参数),`-i.bak`可创建备份 |
| `-r` 或 `-E` | 使用扩展正则表达式 |

## 基本命令

### 查找与打印

```bash
# 打印第5行
sed -n '5p' file.txt

# 打印第5到第10行
sed -n '5,10p' file.txt

# 打印包含"pattern"的行
sed -n '/pattern/p' file.txt

# 打印从第一个匹配到第二个匹配之间的行
sed -n '/start/,/end/p' file.txt

# 打印最后一行
sed -n '$p' file.txt
```

### 删除操作

```bash
# 删除第3行
sed '3d' file.txt

# 删除第3到第6行
sed '3,6d' file.txt

# 删除包含"pattern"的行
sed '/pattern/d' file.txt

# 删除空行
sed '/^$/d' file.txt

# 删除以#开头的行(注释行)
sed '/^#/d' file.txt
```

### 替换操作

```bash
# 替换每行第一个匹配
sed 's/old/new/' file.txt

# 替换每行所有匹配(全局替换)
sed 's/old/new/g' file.txt

# 只替换第2个匹配
sed 's/old/new/2' file.txt

# 替换并打印被修改的行
sed -n 's/old/new/p' file.txt

# 忽略大小写替换
sed 's/old/new/gi' file.txt

# 只在第5行进行替换
sed '5s/old/new/' file.txt

# 只在第5到第10行进行替换
sed '5,10s/old/new/g' file.txt

# 在包含"pattern"的行中进行替换
sed '/pattern/s/old/new/g' file.txt
```

### 插入与追加

```bash
# 在第3行前插入文本
sed '3i\新插入的文本' file.txt

# 在第3行后追加文本
sed '3a\新追加的文本' file.txt

# 在匹配行前插入
sed '/pattern/i\新插入的文本' file.txt

# 在匹配行后追加
sed '/pattern/a\新追加的文本' file.txt
```

### 修改行

```bash
# 替换第3行的内容
sed '3c\新的一行内容' file.txt

# 替换匹配行的内容
sed '/pattern/c\新的一行内容' file.txt
```

## 高级用法

### 使用正则表达式

```bash
# 删除行首空格
sed 's/^[ \t]*//' file.txt

# 删除行尾空格
sed 's/[ \t]*$//' file.txt

# 删除所有空格
sed 's/ //g' file.txt

# 匹配数字
sed -n '/[0-9]/p' file.txt

# 使用扩展正则(+, ?, |等)
sed -E 's/[0-9]+/NUM/g' file.txt
```

### 使用反向引用

```bash
# 交换两个单词的位置
sed 's/\(.*\) \(.*\)/\2 \1/' file.txt

# 给匹配的内容加括号
sed 's/[0-9]*/(&)/' file.txt

# 提取IP地址的某一段
echo "192.168.1.1" | sed 's/\([0-9]*\)\.\([0-9]*\)\..*/\1.\2/'
```

### 多命令组合

```bash
# 使用分号分隔多个命令
sed '1d; s/old/new/g' file.txt

# 使用-e选项
sed -e '1d' -e 's/old/new/g' file.txt

# 使用花括号组合命令
sed '/pattern/{s/old/new/; p}' file.txt
```

### 读写文件

```bash
# 将匹配行后追加文件内容
sed '/pattern/r other.txt' file.txt

# 将匹配行写入新文件
sed '/pattern/w output.txt' file.txt
```

### 保持空间操作

```bash
# h - 将模式空间复制到保持空间
# H - 将模式空间追加到保持空间
# g - 将保持空间复制到模式空间
# G - 将保持空间追加到模式空间
# x - 交换模式空间和保持空间

# 示例:删除重复的相邻行
sed '$!N; /^\(.*\)\n\1$/!P; D' file.txt

# 示例:倒序输出文件
sed '1!G;h;$!d' file.txt
```

## 实用示例

### 文本处理

```bash
# 在文件开头添加内容
sed -i '1i\标题行' file.txt

# 在文件末尾添加内容
sed -i '$a\结尾行' file.txt

# 给每行添加行号
sed = file.txt | sed 'N;s/\n/\t/'

# 删除HTML标签
sed 's/<[^>]*>//g' file.html

# 转换DOS格式到Unix格式
sed 's/\r$//' file.txt

# 转换Unix格式到DOS格式
sed 's/$/\r/' file.txt
```

### 配置文件修改

```bash
# 修改配置项的值
sed -i 's/^Port 22/Port 2222/' sshd_config

# 取消注释
sed -i 's/^#\(.*\)/\1/' config.txt

# 添加注释
sed -i 's/^\(.*\)/#\1/' config.txt

# 在特定行后添加配置
sed -i '/\[section\]/a\new_option = value' config.ini
```

### 日志分析

```bash
# 提取特定时间段的日志
sed -n '/2024-01-01/,/2024-01-31/p' log.txt

# 删除日志中的时间戳
sed 's/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9:]*//g' log.txt

# 统计错误日志
sed -n '/ERROR/p' log.txt | wc -l
```

## 注意事项

1. **备份文件**: 使用 `-i` 选项修改文件前,建议先备份:`sed -i.bak 's/old/new/g' file.txt`

2. **特殊字符转义**: 在正则表达式中,需要转义的字符:`^ $ . * [ ] \ /`

3. **分隔符**: 替换命令的分隔符可以改变,避免转义过多斜杠:
   ```bash
   sed 's#/path/to/old#/path/to/new#g' file.txt
   sed 's|old|new|g' file.txt
   ```

4. **元字符**: 基本正则和扩展正则的区别:
   - 基本: `\+`, `\?`, `\|`, `\(\)`
   - 扩展(加`-E`): `+`, `?`, `|`, `()`

5. **空格处理**: 在shell中使用sed时,注意引号的使用:
   - 单引号 `'` : 保持原样
   - 双引号 `"` : 允许变量替换

## 快速参考

| 命令 | 功能 |
|------|------|
| `p` | 打印 |
| `d` | 删除 |
| `s///` | 替换 |
| `a\` | 追加 |
| `i\` | 插入 |
| `c\` | 修改 |
| `r` | 读取文件 |
| `w` | 写入文件 |
| `q` | 退出 |
| `n` | 读取下一行 |
| `N` | 追加下一行到模式空间 |

---

