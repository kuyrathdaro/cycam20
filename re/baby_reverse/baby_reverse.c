#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_flag(){
    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    FILE *fp;
    char flag[136];
    fp = fopen("flag.txt", "r");
    if(fp == NULL){
        puts("Cannot read flag file");
        exit(1);
    }
    fgets(flag, 128, fp);
    printf("%s", flag);
    fclose(fp);
}

int main(){
    puts("                                ____   ___  ");
    puts("  ___ _   _  ___ __ _ _ __ ___ |___ \\ / _ \\ ");
    puts(" / __| | | |/ __/ _` | \'_ ` _ \\  __) | | | |");
    puts("| (__| |_| | (_| (_| | | | | | |/ __/| |_| |");
    puts(" \\___|\\__, |\\___\\__,_|_| |_| |_|_____|\\___/ ");
    puts("      |___/                                 ");
    puts("\n");

    char code[136];
    printf("Please enter your secret code:\n");
    scanf("%s", code);
    if(strcmp(code, "1337hacker") == 0){
        puts("Access granted");
        print_flag();
    } else {
        puts("Access denied");
    }
  return 0;
}
