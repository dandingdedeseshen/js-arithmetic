#include <stdio.h>
#include <windows.h>
#include <stdlib.h>

// 求阶乘之和
// int retSum(){
//    int a = 1;
//    int sum = 0;
//    int MAX = 11;
//    // 通俗
//    // do
//    // {
//    //    int ret = 1;
//    //    for(int i = 1; i <= a; i++){
//    //       ret *= i;
//    //    }
//    //    sum += ret;
//    //    a ++;
//    // } while (a <= MAX);
//    // 优化每次只多乘一个数
//    int ret = 1;
//    do
//    {
//       ret *= a;
//       sum += ret;
//       a ++;
//    } while (a <= MAX);
// }

// 简单查找
// int find(){
//    int arr[] = {1,2,3,4,5,6,7,8,9,10};
//    int n = 0;
//    int len = sizeof(arr)/sizeof(arr[0]);
//    scanf("%d",&n);
//    for(int i = 0; i < len; i ++){
//       if(arr[i] == n){
//          printf("%d",i);
//          return 0;
//       }
//    }
//    printf("NOT FOUND!!!");
//    return 0;
// }

// 从两边遍历字符串
// int operateStr(){
//    char str1[] = "hello world!!!!";
//    char str2[] = "###############";
//    int len = sizeof(str1)/sizeof(str1[0]);
//    int left = 0;
//    int right = len - 1;
//    for(int i = 0; i < len / 2; i++){
//       Sleep(1000);
//       system("cls");
//       str2[left + i] = str1[left + i];
//       str2[right - i] = str1[right - i];
//       printf("%s\n",str2);
//    }
// }

// sizeof和strlen的区别
int diff(){
   char str[1] = "1234567890";
   printf("%d\n",sizeof(str));
   printf("%d\n",strlen(str));
}

int main()
{
   diff();
   // vscode调试临时使用防止弹窗关闭 没有啥意义
   int asd = 0;
   printf("执行完毕可以关闭窗口啦!");
   scanf("%d",&asd);
   return 0;
}