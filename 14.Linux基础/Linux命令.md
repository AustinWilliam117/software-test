## Linux命令

### 1. cd

- 
- 

### 2. pwd

- 

### 3. ls

### 4. mkdir

### 5. rmkdir

### 6. touch

​	touch [**-acm**] [**-t** *time*] *file*

1. `touch *`

   将目录中所有文件修改成相同时间和日期

2. `touch -m`

   只修改时间`touch -m -t 08311729 file1`(-t 具体时间日期)

3. <font color="red">`touch -a`</font>

   只修改访问时间`touch -a -t 200812211030 file2`

4. `touch newfile`

   创建多文件`touch newfile1 newfile2 newfile3 temp`

5. `touch -c(not create) file`

   更新访问时间不创建新文件`touch -c newfile1 newfile2 newfile3 temp`

### 7. vi