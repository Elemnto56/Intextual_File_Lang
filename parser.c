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
            // Assuming `line[]` already holds the full input line
            // and "output" has already been confirmed

            char temp_output[100];
            char temp_two_output[100];
            char final_output[100];

            // Step 1: Extract everything after "output" into temp_output[]
            memset(temp_output, 0, sizeof(temp_output));
            for (int i = 7, j = 0; line[i] != ';' && line[i] != '\0'; i++, j++) {
                temp_output[j] = line[i];
            }
            temp_output[strlen(temp_output)] = '\0';  // Ensure null termination

            // Step 2: Strip outer quotes and store into temp_two_output[]
            memset(temp_two_output, 0, sizeof(temp_two_output));
            int j = 0;
            for (int i = 1; i < strlen(temp_output); i++) {
                if (temp_output[i] == '"') {
                    break;
                }
                temp_two_output[j++] = temp_output[i];
            }
            temp_two_output[j] = '\0';

            // Step 3: Copy to final_output[]
            memset(final_output, 0, sizeof(final_output));
            for (int i = 0; i <= strlen(temp_two_output); i++) {
                final_output[i] = temp_two_output[i];
            }

            // Step 4: Print clean result
            printf("%s\n", final_output);

        } else {
            printf("Error");
        }

        // This comment is here to remind you of the location of line's while loop
    }

    fclose(file);
    return 0;
}
