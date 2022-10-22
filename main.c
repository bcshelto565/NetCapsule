#include <stdio.h>
#include <dirent.h>
#include <errno.h>
#include <unistd.h>
#include<stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
char* pwd(){
    char *buf;
    buf=(char *)malloc(100*sizeof(char));
    getcwd(buf,100);
    printf("\n %s \n",buf);
    return buf;
}

int check_directory_exits(const char *path){
    struct stat stats;

    stat(path, &stats);

    // Check for file existence
    if (S_ISDIR(stats.st_mode))
        return 1;

    return 0;
}

char* directory(int year,char *event_name,char * data){
    char* concat_name = (char*)malloc(1024);
    strcpy(concat_name,"root/");
    char year_str[20];
    sprintf(year_str,"%d",year);
    strcat(concat_name,year_str);
    if (check_directory_exits(concat_name)){
        printf("Direcoty exist");
    }
    else{
        printf("%s\n",concat_name);
        int ret = mkdir(concat_name, 0755);
    }
    return concat_name;
}
void create_file(char* dir_name,char* event_name,char * data){
    char *file_path = (char* )malloc(1024);
    strcpy(file_path,dir_name);
    strcat(file_path,"/");
    strcat(file_path,event_name);
    strcat(file_path,".html");
    printf("\n%s\n",file_path);
    FILE *fp = fopen(file_path, "w");
    fputs(data,fp);
    fclose(fp);
}

char* read_event(int year, char* event_name){
    char* concat_name = (char*)malloc(1024);
    strcpy(concat_name,"root/");
    char year_str[20];
    sprintf(year_str,"%d",year);
    strcat(concat_name,year_str);
    strcat(concat_name,"/");
    strcat(concat_name,event_name);
    strcat(concat_name,".html");
    FILE *f = fopen(concat_name, "r");
    fseek(f, 0, SEEK_END);
    long length = ftell(f);
    fseek(f, 0, SEEK_SET);
    char *buffer = (char *) malloc(length + 1);
    buffer[length] = '\0';
    fread(buffer, 1, length, f);
    fclose(f);
    return buffer;
}