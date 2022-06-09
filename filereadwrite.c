#include <stdio.h>
#include <string.h>
#define _GNU_SOURCE
#include <stdlib.h>

char **split(char *string, char *seperators, int *count);

char* replaceWord(const char* s, const char* oldW,
                  const char* newW)
{
    char* result;
    int i, cnt = 0;
    int newWlen = strlen(newW);
    int oldWlen = strlen(oldW);
  
    // Counting the number of times old word
    // occur in the string
    for (i = 0; s[i] != '\0'; i++) {
        if (strstr(&s[i], oldW) == &s[i]) {
            cnt++;
  
            // Jumping to index after the old word.
            i += oldWlen - 1;
        }
    }
  
    // Making new string of enough length
    result = (char*)malloc(i + cnt * (newWlen - oldWlen) + 1);
  
    i = 0;
    while (*s) {
        // compare the substring with the result
        if (strstr(s, oldW) == s) {
            strcpy(&result[i], newW);
            i += newWlen;
            s += oldWlen;
        }
        else
            result[i++] = *s++;
    }
  
    result[i] = '\0';
    return result;
}



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

            fprintf(fp, "%s🇹🇷%s\n", email,password);


            fclose(fp);
            printf("200");
            return 0;
        }
        else{
            char string[1000];
            if(strcmp(argv[1],"login")==0)
            {
                char *arg1 = argv[1];
                char *email = argv[2];
                char *password = argv[3];
                FILE *fp = fopen(filename, "r");
                char singleLine[150];
                char ch;
                char* checkthething;
                char* checkthethingpassword;
                int emailexists =  0;
                int passwordexists = 0;
                
                do {
                    ch = fgetc(fp);
                    
                    char mystring[100] = "";
                    char str1[300] = {ch , '\0'};
                    char s[500] = "";



                    strcpy(s,str1);


                    

                    

                    int count_strings = 0;
                    char **split_strings = split(s, "🇹🇷", &count_strings);
                    
                    // print out the substrings, which should be each word of the sentence above
                    

                    for (int i = 0; i < count_strings; i++)


                        if (strcmp(split_strings[i],email)==0){
                            emailexists = 1;

                        }

                        else{
                            if (strcmp(split_strings[i],password)==0){
                                passwordexists = 1;
                            }
                            else{
                                NULL;
                                
                            }
                        }
                        

                        
                        
                    
                    
                    
                    // free the dynamically allocated space for each string
                    for (int i = 0; i < count_strings; i++)
                        free(split_strings[i]);
                    
                    // free the dynamically allocated space for the array of pointers to strings
                    free(split_strings);
                    
        
                
                } while (ch != EOF);
                if (emailexists == 1)
                {
                    if(passwordexists ==1){
                        printf("200\n");
                    }
                    else{
                        printf("403p\n");
                    }
                }
                if (emailexists==0){
                    printf("403e\n");
                }
                
                
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
char **split(char *string, char *seperators, int *count)
{
  // get the length of the string
  int len = strlen(string);
  
  // use count to keep a count of the number of substrings
  *count = 0;
  
  // We make one pass of the string to first determine how many substrings 
  // we'll need to create, so we can allocate space for a large enough array 
  // of pointer to strings.  The variable i will keep track of our current 
  // index in the string
  int i = 0;
  while (i < len)
  {
    // skip over the next group of separator characters
    while (i < len)
    {
      // keep incrementing i until the character at index i is NOT found in the 
      // separators array, indicating we've reached the next substring to create 
      if (strchr(seperators, string[i]) == NULL)
        break;
      i++;
    }
    
    // skip over the next group of substring (i.e. non-separator characters), 
    // we'll use old_i to verify that we actually did detect non-separator 
    // characters (perhaps we're at the end of the string)
    int old_i = i;
    while (i < len)
    {
      // increment i until the character at index i IS found in the separators 
      // array, indicating we've reached the next group of separator 
      // character(s)
      if (strchr(seperators, string[i]) != NULL)
        break;
      i++;
    }

    // if we did encounter non-seperator characters, increase the count of 
    // substrings that will need to be created  
    if (i > old_i) *count = *count + 1;
  }
  
  // allocate space for a dynamically allocated array of *count* number of 
  // pointers to strings
  char **strings = malloc(sizeof(char *) * *count);
  
  // we'll make another pass of the string using more or less the same logic as 
  // above, but this time we'll dynamically allocate space for each substring 
  // and store the substring into this space
  i = 0;

  // buffer will temporarily store each substring, string_index will keep track 
  // of the current index we are storing the next substring into using the 
  // dynamically allocated array above
  char buffer[16384];
  int string_index = 0;
  while (i < len)
  {
    // skip through the next group of separators, exactly the same as above
    while (i < len)
    {
      if (strchr(seperators, string[i]) == NULL)
        break;
      i++;
    }
    
    // store the next substring into the buffer char array, use j to keep 
    // track of the index in the buffer array to store the next char
    int j = 0;
    while (i < len)
    {
      if (strchr(seperators, string[i]) != NULL)
        break;
      
      buffer[j] = string[i];
      i++;
      j++;
    }
    
    // only copy the substring into the array of substrings if we actually 
    // read in characters with the above loop... it's possible we won't if 
    // the string ends with a group of separator characters!
    if (j > 0)
    {
      // add a null terminator on to the end of buffer to terminate the string
      buffer[j] = '\0';

      // calculate how much space to allocate... we need to be able to store 
      // the length of buffer (including a null terminator) number of characters 
      int to_allocate = sizeof(char) *
                        (strlen(buffer) + 1);
      
      // allocate enough space using malloc, store the pointer into the strings 
      // array of pointers at hte current string_index
      strings[string_index] = malloc(to_allocate);
      
      // copy the buffer into this dynamically allocated space 
      strcpy(strings[string_index], buffer);
      
      // advance string_index so we store the next string at the next index in 
      // the strings array
      string_index++;
    }
  }

  // return our array of strings  
  return strings;
}


