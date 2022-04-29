#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 


int main() {
    
    char command[256] = {'p', 'i', 'n', 'g', ' ', '\0'}; 
    
    char host[16]; 
    printf("please enter host for ping\n");
    
    gets(host); 
    
    printf("command: %s\n", command); 
    
    printf("host: %s\n", host); 
    
    strcat(command, host);
    printf("full command: %s\n", command); 

    system(command); 
    return 0; 
}