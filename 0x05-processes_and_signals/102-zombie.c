#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Causes an infinite loop with a 1-second interval delay.
 *
 * Return: Always 0 (infinite loop).
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */

int main(void)
{
	pid_t child_pid;
	int zombie_count;

	for (zombie_count = 0; zombie_count < 5; zombie_count++)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			wait(NULL);
		}
		else if (child_pid == 0)
		{
			exit(0);
		} else
		{
			perror("Fork failed");
			return (1);
		}
	}
	infinite_while();

	return (0);
}
