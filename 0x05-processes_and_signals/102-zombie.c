#include <unistd.h>
#include <stdio.h>

int infinite_while(void);

/**
 * main - program that creates 5 zombie processes.
 * Return: infinite while return.
 */
int main(void)
{
	pid_t pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			return (0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
	}
	return (infinite_while());
}

/**
 * infinite_while - function that creates an infinity loop
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
