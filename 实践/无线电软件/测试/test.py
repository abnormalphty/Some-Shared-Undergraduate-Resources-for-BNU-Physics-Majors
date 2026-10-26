from jnius import autoclass

# 测试与 Java 类的交互
System = autoclass('java.lang.System')
System.out.println('Hello from Java!')
