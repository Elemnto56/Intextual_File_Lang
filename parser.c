#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s filename.itx\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("Error: Cannot open file %s\n", argv[1]);
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), file)) {
        // Remove trailing newline character
        line[strcspn(line, "\n")] = '\0';

        // Ignore empty lines
        if (strlen(line) == 0) {
            continue;
        }

        // OUTPUT (print statement)
        char input[10];
        for (int i = 0; i <= 6; i++) {
            input[i] = line[i];
        }

        if (strcmp("output", input)) {
            char temp_output[100];
            for (int i = 7; i < line[strlen(line) - 1]; i++) {
                if (line[i] == ';') {
                    break;
                }
                temp_output[i - 7] = line[i];
            }

            char temp_two_output[100];
            char final_output[100];
            char *ptr = &temp_output[0];
            if (strcmp("\"", ptr)) {
                for (int i = 1; i < temp_output[strlen(temp_output) - 1]; i++) {
                    if (temp_output[i] == '"') {
                        break;
                    }
                    temp_two_output[i - 1] = temp_output[i];
                    for (int i = 0; i < temp_two_output[strlen(temp_two_output) - 1]; i++) {
                        final_output[i] = temp_two_output[i];
                    }
                }
                printf("%s\n", final_output);
                /*Debugging*/
                printf("Quote Parsed: %s\n", temp_two_output);
                printf("Removed output: %s\n", temp_output);
            }
        } else {
            printf("Error");
        }

        // This comment is here to remind you of the location of line's while loop
    }

    fclose(file);
    return 0;
}
