# Dev Ops
## Web stack debugging

### Background context
The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).  

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.  

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.  

Let’s start with a very simple example. My server must:  

*   have a copy of the /etc/passwd file in /tmp  
*   have a file named /tmp/isworking containing the string OK  
Let’s pretend that without these 2 elements, my web application cannot work.  

Let’s go through this example and fix the server.  

### Installing Docker
For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.  

*   Mac OS
*   Windows
*   Ubuntu 14.04 (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)
*   Ubuntu 16.04
