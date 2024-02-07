#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>  // Include sys/wait.h for wait()
#include <unistd.h>

int main() {
    pid_t pid;
    
    // Create a child process using fork()
    pid = fork();
    if (pid < 0) {
        // Fork failed
        perror("Fork failed");
        exit(1);
    } else if (pid == 0) {
        // Child process
        printf("Child process with PID %d\n", getpid());
        execlp("/bin/ls", "ls", NULL);
        perror("exec failed"); // Print an error if execlp fails
        exit(1);
    } else {
        // Parent process
        wait(NULL);  // Wait for the child process to complete
        printf("Child Complete\n");
    }
    return 0;
}
