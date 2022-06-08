#include <stdio.h>
#include <string.h>
#define _GNU_SOURCE
#include <stdlib.h>

int main( int argc, char *argv[] ){
    char *filename = "auth.txt";
    int display;

    if(argc == 4){
        if (strcmp(argv[1],"register")==0){
            FILE *fp = fopen(filename, "a");
            if (fp == NULL)
            {
                printf("err 500 %s", filename);
                return -1;
            }
            char *arg1 = argv[1];
            char *email = argv[2];
            char *password = argv[3];

            fprintf(fp, "%s-238746-%s\n", email,password);


            fclose(fp);

            return 0;
        }
        else{
            char string[1000];
            if(strcmp(argv[1],"login")==0)
            {
                FILE *fp = fopen(filename, "r");
                char singleLine[150];
                char ch;
                
                do {
                    ch = fgetc(fp);
                    printf("%c", ch);
        
                
                } while (ch != EOF);
                
                fclose(fp);

                
            }
            else
            {
                
                printf("Error");
            }
        
        }
        
        
    }


    // open the file for writing
   
}